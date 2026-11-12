with open("student.txt","w") as f:
    f.write("Python File Handling")

with open("student.txt","r") as f:
    print(f.read())