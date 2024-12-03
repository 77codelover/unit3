class student:
    def setname(self,name):
        self.name=name
    def getname(self):
        return self.name
    
    def setage(self,age):
         self.age=age
    def getage(self):
        return self.age
    
n = int(input("how many students: "))
i = 0
while i<n:
    s = student()
    name = input("Enter name: ")
    s.setname(name)
    age = int(input("Enter Age:"))
    s.setage(age)
    print(s.getname())
    print(s.getage())
    i+=1