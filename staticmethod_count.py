class student():
    n = 0
    def __init__(self):
        student.n+=1
    @staticmethod
    def print1():
        print("No of objects: ",student.n)

s = student()
s1 = student()
s2 = student()
student.print1()
