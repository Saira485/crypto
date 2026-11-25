DA = 4
DB = 3

PA = f"{DA}G"
PB = f"{DB}G"

KA = f"{DA * DB}G"
KB = f"{DB * DA}G"

print("Alice public key:", PA)
print("Bob public key:", PB)

print("Alice secret key:", KA)
print("Bob secret key:", KB)