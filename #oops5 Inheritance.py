#oops5 Inheritance
class car:
    @staticmethod
    def start():
        print("car started..")
    @staticmethod
    def stop():
        print("car startsd..")
class Toyotacar(car):
    def __init__(self,name):
        self.name = name
car1 = Toyotacar("fortuner") 
car2 = Toyotacar("innova")
print(car1.name,car2.name)       
print(car1.start())