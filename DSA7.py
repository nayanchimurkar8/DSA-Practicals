# Move all zeros to the end

n = int(input("Enter the number of elements: "))

arr = []

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

new_arr = []

for num in arr:
    if num != 0:
        new_arr.append(num)

for num in arr:
    if num == 0:
        new_arr.append(num)

print("Original array:", arr)
print("Array after moving zeros:", new_arr)