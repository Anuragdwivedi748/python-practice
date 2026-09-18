#practice of IO
#with open("practice.txt","w") as f:
#    f.write("hii everyone\n my name is sant")
#    f.write("\n i am learning java")

#replace java to python

with open("practice.txt","r") as f:
    data=f.read()#change java to python
new_data =data.replace("java","python")
print(new_data)
#now override in file
with open("practice.txt","w") as f:
    f.write(new_data)