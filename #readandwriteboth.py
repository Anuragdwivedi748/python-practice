#readandwriteboth.py
#f=open("demo.txt","r+")#starting override
#f.write("abc")
#f.close()
f=open("demo.txt","w+")#open in truncate mode
print(f.read())
f.write("abc")
f.close()