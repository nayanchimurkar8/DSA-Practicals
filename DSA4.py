n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

search = int(input("Enter number to search: "))

found = False

for i in range(n):
    if arr[i] == search:
        print("Element found at position", i + 1)
        found = True
        break

if found == False:
    print("Element is not present in the array.")