text = input("Enter message: ").upper()
key = input("Enter key: ").upper()

# Encryption
enc = ""

for i in range(len(text)):
    enc += chr((ord(text[i]) + ord(key[i % len(key)]) - 130) % 26 + 65)

print("Encrypted:", enc)

# Decryption
dec = ""

for i in range(len(enc)):
    dec += chr((ord(enc[i]) - ord(key[i % len(key)])) % 26 + 65)

print("Decrypted:", dec)