text = input("Enter message: ").upper()

a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
b = "QWERTYUIOPASDFGHJKLZXCVBNM"

# Encryption
enc = ""

for ch in text:
    if ch in a:
        enc += b[a.index(ch)]

print("Encrypted:", enc)

# Decryption
dec = ""

for ch in enc:
    dec += a[b.index(ch)]

print("Decrypted:", dec)