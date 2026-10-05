# 1. Print plus star pattern

n = int(input("Enter the number of rows: "))

for i in range(n):
    for j in range(n):
        if i == n // 2 or j == n // 2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()



# 2. Print hollow square

n = int(input("Enter the number of rows: "))

for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


# 3. Print number pyramid

n = int(input("Enter the number of rows: "))

for i in range(1, n + 1):

    # Print spaces
    for j in range(n - i):
        print("  ", end="")

    # Print increasing numbers
    for j in range(1, i + 1):
        print(j, end=" ")

    # Print decreasing numbers
    for j in range(i - 1, 0, -1):
        print(j, end=" ")

    print()



# 4. Print 0 and 1 pattern

n = int(input("Enter the number of rows: "))

for i in range(n):
    for j in range(n):
        if (i + j) % 2 == 0:
            print("1", end=" ")
        else:
            print("0", end=" ")
    print()


# 5. Print circle pattern

print("    *")
print("  *   *")
print(" *     *")
print("*       *")
print("*       *")
print(" *     *")
print("  *   *")
print("    *")