class Student:
    def __init__(self,name):
        self.name = name
    def display(self):
        print("Name:",self.name)
s1=Student("Arya")
s1.display()