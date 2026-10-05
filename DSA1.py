n = int(input ("Enter a number of element: "))
array = []
for i in range(n):
    num = int(input("Enter the element :" + str(i+1)))
    array.append(num)
array_sum = sum(array)
print("sum of array is :" +str (array_sum))
