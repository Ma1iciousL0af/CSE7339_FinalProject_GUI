from Crypto import Random
from Crypto.Random import random
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
import os
from shutil import copyfile

def pad(s):
    return s + b"\0" * (AES.block_size - len(s) % AES.block_size)

def generateKey(password):
    #generate randomly generated key from master password
    salt = Random.new().read(8)
    iterations = 5000
    dkLen = 32
    key = PBKDF2(password, salt, dkLen = 32, count = iterations)
    return key

def encrypt (message, key, key_size=256):
    message = pad(message)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return iv + cipher.encrypt(message)

def decrypt(ciphertext, key):
    iv = ciphertext[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext[AES.block_size:])
    return plaintext.rstrip(b"\0")

def encryptFile(file_name, key):
    with open(file_name, 'rb') as file:
        plaintext = file.read()
    enc = encrypt(plaintext, key)
    with open(file_name + ".enc", 'wb') as file_out:
        file_out.write(enc)
    # copyfile(file_name+".enc", "encrypted")
    # copying file, intended for testing whether encrypt/decrypt was actually working
    os.remove(file_name) # remove old plaintext file
    if ".enc" in file_name + ".enc":
        os.rename(file_name + ".enc", file_name) #rename .enc file to the original filename
        #yes I tried doing the encryption in place, it was doing weird stuff. 


def decryptFile(file_name, key):
    with open(file_name, 'rb') as file:
        ciphertext = file.read()
        print "success"
    dec = decrypt(ciphertext, key)
    with open(file_name,'wb') as file:
        file.write(dec)

if __name__ == '__main__':
    password = '0000'
    key = generateKey(password)
    txt_file = "include/test.txt"
    jpg_file = "include/test.jpg"
    encryptFile(txt_file, key)
    decryptFile(txt_file, key)
    encryptFile(jpg_file, key)
    decryptFile(jpg_file, key)
