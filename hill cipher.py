text = input("Enter message: ").upper()

# Add X if odd length
if len(text) % 2 != 0:
    text += "X"

# Encryption
enc = ""

for i in range(0, len(text), 2):
    a = ord(text[i])-65
    b = ord(text[i+1])-65

    enc += chr((3*a+3*b)%26+65)
    enc += chr((2*a+5*b)%26+65)

print("Encrypted:", enc)

# Decryption
dec = ""

for i in range(0, len(enc), 2):
    a = ord(enc[i])-65
    b = ord(enc[i+1])-65

    dec += chr((15*a+17*b)%26+65)
    dec += chr((20*a+9*b)%26+65)

print("Decrypted:", dec)