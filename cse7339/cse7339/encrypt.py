from Crypto.Cipher import AES
from Crypto import Random

def encryptFile(master, p_filename):
    #randomly generate key
    random = Random.new().read(AES.block_size)
    print(random)

    #consider writing a function for this later
    #read plaintext file
    p_file = open(p_filename, 'r+')
    p_text = p_file.read()
    p_file.close()
    
    #perform AES encryption on data using random key
    e_text = encryptAES(random, p_text)

    #write encrypted data to file
    e_file = open(p_filename, 'r+')
    e_file.truncate()
    e_file.write(e_text)
    e_file.close()

    #perform AES encryption on random key using master key
    e_key = encryptAES(master, random)

##    return (e_file, e_key)
    decryptFile(p_filename, e_key, master)

def decryptFile(e_filename, e_key, master):
    #perform AES decryption on random key using master key
    random = decryptAES(master, e_key)
    print(random)

    #consider writing a function for this later
    #read encrypted file
    e_file = open(e_filename, 'r+')
    e_text = e_file.read()
    e_file.close()

    #perform AES decryption on encrypted file using random key
    p_text = decryptAES(random, e_text)

    #write decrypted data to file
    p_file = open(e_filename, 'r+')
    p_file.truncate()
    p_file.write(p_text)
    p_file.close()

    print(p_file)
    return p_file

#perform AES encryption
def encryptAES(key, plaintext):
    raw = pad(plaintext)
    iv = Random.new().read( AES.block_size )
    cipher = AES.new(pad(key), AES.MODE_CFB, iv)
    encrypted = iv + cipher.encrypt(raw)
    return encrypted

#perform AES decryption
def decryptAES(key, encrypted):
    iv = encrypted[AES.block_size]
    cipher = AES.new(pad(key), AES.MODE_CFB, iv)
    plaintext = unpad(cipher.decrypt(encrypted[16:]))
    print(plaintext)
    return plaintext

def pad(s):
    BS = 16
    return s + (BS - len(s) % BS) * chr(BS - len(s) % BS)

def unpad(s):
    return s[:-ord(s[len(s)-1:])]


if __name__ == '__main__':
  encryptFile("0000", "include/test.txt")
