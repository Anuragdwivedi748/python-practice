#oops6
#class name same and object another store a name
#class person():
 #   name= "anonymous"
    
#    def changename(self,name):
#        self.name = name
#p1=person()
#p1.changename("rahul")
#print(p1.name)
#print(person.name
## for correct we use person at the place of self or use self.__class__

class person():
    name= "anonymous"
    
    def changename(self,name):
        person.name = name
p1=person()
p1.changename("rahul")
print(p1.name)
print(person.name)
