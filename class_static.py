class student:
    var = 10
    @classmethod
    def print(cls):
        cls.var+=1

s1=student()
print(s1.var)
s1.print()
print(s1.var)