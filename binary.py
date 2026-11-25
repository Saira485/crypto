a = [10, 20, 30, 40, 50]
x = int(input("Enter element: "))

low = 0
high = len(a)-1

while low <= high:
    mid = (low+high)//2

    if a[mid] == x:
        print("Found at position:", mid+1)
        break
    elif a[mid] < x:
        low = mid+1
    else:
        high = mid-1
else:
    print("Not Found")