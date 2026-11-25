# RSA Encryption and Decryption

p = 3
q = 11

n = p * q
phi = (p-1) * (q-1)

e = 3
d = 7

data = 5

# Encryption
encrypted = pow(data, e, n)

print("Encrypted:", encrypted)

# Decryption
decrypted = pow(encrypted, d, n)

print("Decrypted:", decrypted)