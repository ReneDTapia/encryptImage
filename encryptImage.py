import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def getKey(keysize):
    return os.urandom(keysize)

def getIV(blocksize):
    return os.urandom(blocksize)

def encrypt_image(filename, key, iv):
    BLOCKSIZE = 16
    encrypted_filename = "encrypted_" + filename
    with open(filename, "rb") as file1:
        data = file1.read()
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(data, BLOCKSIZE))
    with open(encrypted_filename, "wb") as file2:
        file2.write(ciphertext)
    return encrypted_filename

def decrypt_image(encrypted_filename, key, iv):
    with open(encrypted_filename, "rb") as file:
        ciphertext = file.read()
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    decrypted_filename = "decrypted_" + encrypted_filename
    with open(decrypted_filename, "wb") as file:
        file.write(plaintext)
    return decrypted_filename

KEYSIZE = 16
BLOCKSIZE = 16
filename = "arrow.png"
key = getKey(KEYSIZE)
iv = getIV(BLOCKSIZE)
encrypted_filename = encrypt_image(filename, key, iv)
decrypted_filename = decrypt_image(encrypted_filename, key, iv)

