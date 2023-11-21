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

import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def getKey(keysize):
    return os.urandom(keysize)

def getIV(blocksize):
    return os.urandom(blocksize)

def file_exists(filename):
    return os.path.exists(filename)

def encrypt_image(filename, key, iv):
    BLOCKSIZE = 16
    if not file_exists(filename):
        raise FileNotFoundError(f"El archivo {filename} no existe.")
    encrypted_filename = "encrypted_" + filename
    with open(filename, "rb") as file1:
        data = file1.read()
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(data, BLOCKSIZE))
    with open(encrypted_filename, "wb") as file2:
        file2.write(ciphertext)
    return encrypted_filename

def decrypt_image(encrypted_filename, key, iv):
    if not file_exists(encrypted_filename):
        raise FileNotFoundError(f"El archivo {encrypted_filename} no existe para descifrar.")
    with open(encrypted_filename, "rb") as file:
        ciphertext = file.read()
    cipher = AES.new(key, AES.MODE_CBC, iv)
    try:
        plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    except ValueError as e:
        raise ValueError(f"Error al desencriptar {encrypted_filename}: {e}")
    decrypted_filename = "decrypted_" + encrypted_filename
    with open(decrypted_filename, "wb") as file:
        file.write(plaintext)
    return decrypted_filename

KEYSIZE = 16
BLOCKSIZE = 16
filename = "arrow.png"

if file_exists(filename):
    key = getKey(KEYSIZE)
    iv = getIV(BLOCKSIZE)
    try:
        encrypted_filename = encrypt_image(filename, key, iv)
        decrypted_filename = decrypt_image(encrypted_filename, key, iv)
    except Exception as e:
        print(f"Ocurrió un error: {e}")
else:
    print(f"No se encontró el archivo {filename}. Asegúrate de que el nombre y la ruta sean correctos.")
