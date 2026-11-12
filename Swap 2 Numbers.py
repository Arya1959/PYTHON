x = int(input("Enter the 1st number: "))
y = int(input("Enter the 2nd number: "))
print(f"x: {x}, y: {y}")
x = x + y
y = x - y
x = x - y
print(f"Swapped, x: {x}, y: {y}")