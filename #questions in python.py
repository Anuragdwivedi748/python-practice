#questions in python

#i=1
#while i<=100:
 #   print(i)
  #  i+=1

#number from 100 to 1
#i=100
#while i>=1:
 #   print(i)
  #  i-=1

#print multiplication table of a number n
#n=3
#i=1
#while i<=10:
 #   print(n*i)
  #  i+=1

#print the eliment of the following list using a loop while loop
#num=[1,4,9,16,25,36,49,64,81,100]
#idx = 0
#while idx < len(num):
 #   print(num[idx])
  #  idx += 1
num=(1,4,9,16,25,36,49,64,81,100,36)
x=36
i=0
while i < len(num):
    if(num[i]==x):
        print("found",i)
    else:
        print("not found",i)
    i+=1