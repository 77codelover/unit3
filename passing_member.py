class Emp:
    def __init__(self,id,name,sal):
        self.id = id
        self.name = name
        self.sal = sal
    def print(self):
        print(f"ID: {self.id}, Name: {self.name}, Salary: {self.sal}")

class myclass:
       @staticmethod
       def myfunc(e):
           e.sal += 1000
           e.print()
e = Emp(101,"Ramesh",1200.75)
myclass.myfunc(e)