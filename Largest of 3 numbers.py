n1 = int(input("Enter the 1st number: "))
n2 = int(input("Enter the 2nd number: "))
n3 = int(input("Enter the 3rd number: "))

if n1 > n2:
	if n1 > n3:
		print("Number 1 is the largest")
	else:
		print("Number 3 is the largest")
else:
	if n2 > n3:
		print("Number 2 is the largest")
	else:
		print("Number 3 is the largest")