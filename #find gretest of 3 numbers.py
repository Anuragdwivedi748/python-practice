#find gretest of 3 numbers
num1=int(input("enter a num1:"))
num2=int(input("enter a num2:"))
num3=int(input("enter a num3:"))

if(num1>num2 and num1>num3):
    print("num1 is greatest")
elif(num2>num1 and num2>num3):
    print("num2 is greatest")
else:
    print("num3 is greatest")