n = int(input("enter the no. element "))
arr = []

for i in range(n):
    arr.append(int(input("enter element:")))

arr.sort()
print("smallest=",arr[0])
print("second smallest=",arr[1])
print("second largest=",arr[-2])
print("Largest=",arr[-1])

