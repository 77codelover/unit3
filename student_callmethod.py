class student:
    def __init__(self):
        self.name = "Harsh"
        self.age = 22
        self.marks = 89
    def print(self):
        print("Name : ",self.name)
        print("Age : ",self.age)
        print("Marks : ",self.marks)
s = student()
s.print()