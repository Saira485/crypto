text = input("Enter message: ").upper()
key = int(input("Enter key: "))

# Encryption
enc = ""

for ch in text:
    enc += chr((ord(ch)-65+key)%26+65)

print("Encrypted:", enc)

# Decryption
dec = ""

for ch in enc:
    dec += chr((ord(ch)-65-key)%26+65)

print("Decrypted:", dec)