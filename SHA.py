import hashlib

text = input("Enter message: ")

# Generate SHA hash
result = hashlib.sha256(text.encode())

print("Original message:", text)
print("SHA-256 Hash:", result.hexdigest())