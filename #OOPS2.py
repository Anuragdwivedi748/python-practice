#OOPS2
#Constructor
#class Student:
#    name="karan"
#    def __init__(self,):
#        print("adding new student")
#s1=Student()

class Student:
    def __init__(self,fullname,marks):#constructor
        self.name = fullname
        self.marks = marks
        print("adding new student")

    def welcome(self):
        print("welcome student")

s1=Student("karan",98)
print(s1.name,s1.marks)
s1.welcome()
s2=Student("arjun",95)
print(s2.name,s2.marks)