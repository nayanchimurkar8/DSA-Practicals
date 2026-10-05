# Find all occurrences of a substring

text = input("Enter the main string: ")
substring = input("Enter the substring to search: ")

positions = []

for i in range(len(text) - len(substring) + 1):
    if text[i:i + len(substring)] == substring:
        positions.append(i)

if len(positions) > 0:
    print("Substring found at positions:", positions)
    print("Number of occurrences:", len(positions))
else:
    print("Substring not found")