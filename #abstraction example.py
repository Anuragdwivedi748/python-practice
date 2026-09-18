#abstraction example
class car():
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clute = False
    def start(self):
        self.clute = True
        self.acc = True
        print("car started..")

car1 = car()
car1.start()