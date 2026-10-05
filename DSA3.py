n = int(input("Enter no of element:"))
arr = []
for i in range(n):
    arr.append(int(input("Enter element:")))
even = 0
odd = 0

for i in arr:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

print("Enter even:",even)
print("Enter odd:",odd)