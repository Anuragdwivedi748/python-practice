#oops3 practice
#crete account class with 2 attribute - balance and account no
#create method for debit, credit and printing the balance
class account():
    def __init__(self, bal,acc):
        self.balance = bal
        self.account_no=acc
    #debit
    def debit(self,amount):
        self.balance =-amount
        print("Rs",amount,"was debited")
    def credited(self,amount):
        self.balance +=amount
        print("Rs",amount,"was credited")
        print("totalbalence",self.get_balance())
    def get_balance(self):
        return self.balance


acc1 = account(10000,345)
acc1.debit(100)
acc1.credited(110)
acc1.get_balance()