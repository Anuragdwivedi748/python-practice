#OOPS 4
class student():
    def __init__(self,name):
        self.name = name
s1=student("ram")
print(s1.name)
del s1.name
print(s1.name)
