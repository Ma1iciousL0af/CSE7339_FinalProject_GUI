from Crypto.Cipher import AES
from Crypto import Random

BS = AES.block_size #16

def encryptFile(master, p_filename):
    #randomly generate key
    #random = Random.new().read(BS)

    #read plaintext file
    key = pad(master)
    p_text = readFile(p_filename)

    #perform AES encryption on data using random key
    if ".txt" in p_filename:
        e_text = encryptAES(key, p_text)
    if ".jpg" in p_filename:
        e_text = encryptAES_jpg(key, p_text)
    #write encrypted data to file

    writeFile(p_filename, e_text)

    #perform AES encryption on random key using master key
    #e_key = encryptAES(master, random)

    #return e_key

def decryptFile(e_filename,  master):
    #perform AES decryption on random key using master key
    #random = decryptAES(master, e_key)

    #read encrypted file
    e_text = readFile(e_filename)

    #perform AES decryption on encrypted file using random key
    if ".txt" in e_filename:
        p_text = decryptAES(master, e_text)
    if ".jpg" in e_filename:
        p_text = decryptAES_jpg(master, e_text)

    #write decrypted data to file
    writeFile(e_filename, p_text)

#perform AES encryption
def encryptAES(key, plaintext):
    iv = Random.new().read(BS)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted = iv + cipher.encrypt(pad(plaintext))
    return encrypted

def encryptAES_jpg(key, plaintext):
    iv = Random.new().read(BS)
    cipher = AES.new(pad(key), AES.MODE_CFB, iv)
    encrypted = iv + cipher.encrypt(pad(plaintext))
    return encrypted
#perform AES decryption
def decryptAES(key, encrypted):
    iv = encrypted[:16]
    cipher = AES.new(pad(key), AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(encrypted[16:]))
    return plaintext

def decryptAES_jpg(key, encrypted):
    iv = encrypted[:16]
    cipher = AES.new(pad(key), AES.MODE_CFB, iv)
    plaintext = unpad(cipher.decrypt(encrypted[16:]))
    return plaintext

def pad(s):
    return s + (BS - len(s) % BS) * chr(BS - len(s) % BS)

def unpad(s):
    return s[:-ord(s[len(s)-1:])]

def readFile(filename):
    myfile = open(filename, 'r+')
    mytext = myfile.read()
    myfile.close()
    return mytext

def writeFile(filename, data):
    myfile = open(filename, 'r+')
    myfile.truncate()
    myfile.write(data)
    myfile.close()

if __name__ == '__main__':
    password = "0000"
    txt_file = "include/test.txt"
    jpg_file = "include/test.jpg"
    encryptFile(password, txt_file)
    decryptFile(txt_file, password)
    jpg_key = encryptFile(password, jpg_file)
    decryptFile(jpg_file, password)
