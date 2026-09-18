#OOPS3 Practice question
#create student class that takes name and marks of 3 subject as argument in constructorthen create a method to print the average
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def average(self):
        sum=0
        for val in self.marks:
            sum+=val
        print("hi",self.name,"your avg score is:",sum/3)

s1=Student("ram",[96,98,97])
print(s1.name,s1.marks)
s1.average()
s2=Student("shyam",[98,96,94])
print(s2.name,s2.marks)
s2.average()
s3=Student("bharat",[95,95,90])
print(s3.name,s3.marks)
s3.average()