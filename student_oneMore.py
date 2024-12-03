class student:
    def __init__(self,name='',age=14,marks=0):
        self.name = name
        self.age = age
        self.marks = marks

    def print(self):
        print("Name : ",self.name)
        print("Age : ",self.age)
        print("Marks : ",self.marks)

s = student("Aman",17,36)
s.print()
