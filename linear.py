a = [10, 20, 30, 40, 50]
x = int(input("Enter element: "))

for i in range(len(a)):
    if a[i] == x:
        print("Found at position:", i+1)
        break
else:
    print("Not Found")