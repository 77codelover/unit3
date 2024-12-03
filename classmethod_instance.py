class student:
    marks = 10
    @classmethod
    def print(cls,name):
        print(f"{name} has {cls.marks} marks")
student.print("Ajay")
student.print('aditya')