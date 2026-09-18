#forloop2 practice
#num=[1,4,9,16,25,36,49,64,81,100]
#for i in num:
 #   print(i)

# search an num
num=[1,4,9,16,25,36,49,64,81,100]
x=49
idx=0
for i in num:
    if(i==x):
        print("found",idx)
    idx += 1