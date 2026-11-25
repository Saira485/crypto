from Crypto.Cipher import DES

key = b'12345678'
data = b'HELLO123'

cipher = DES.new(key, DES.MODE_ECB)

encrypted = cipher.encrypt(data)

print("Encrypted:", encrypted.hex())

decrypted = cipher.decrypt(encrypted)

print("Decrypted:", decrypted.decode())

# pip install pycryptodome