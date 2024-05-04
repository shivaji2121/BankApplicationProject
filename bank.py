from random import randint
from abc import ABC,abstractmethod
import sys
import datetime
class util:
    history=[]
    @staticmethod
    def generateAccountNumber():
        ano=""
        for i in range(12):
            ano=ano+str(randint(0,9))
        return ano
    @classmethod
    def addEntry(cls,msg):
        util.history.append(msg)
    
    @staticmethod
    def createAccount(accountType):
        if accountType=="Savings":
            name=input("Enter your name: ")
        else:
            name=input("Enter your name: ")
            
        balance=eval(input("Enter initial balance: "))
        while balance<0:
            balance=eval(input("Initial balance should not be Negatie/Minus,Please enter vaid value: "))
        if accountType=="Savings":
            account=SavingsAccount(name,balance)
        else:
            account=CurrentAccount(name,balance)
            
        util.addEntry("{}-{} Account Created with A/C NO:{} and With Balance-{}".format(datetime.datetime.now(),accountType,account.account_number,account.balance))
        print("Congratulations, Your {} Account created Successfully with A/C No:{} ".format(accountType,account.account_number))
        return account
class Account(ABC):
    BANKNAME="SHIVAJI"
    def __init__(self,name,balance,min_balance):
        self.account_number=util.generateAccountNumber()
        self.name=name
        self.balance=balance
        self.min_balance=min_balance


# Savings account ......
class SavingsAccount(Account):
    def __init__(self,name,balance):
        super().__init__(name,balance,0)
    # balance enquriy.....
    def bEnquiry(self):
        print("Hello {},Balance in Your Savings Account,ends with xxxxxxxxx{}- Balance is Rs:{}/-".format(self.name,self.account_number[9:],self.balance))

class CurrentAccount(Account):
    def __init__(self,name,balance):
        super().__init__(name,balance,-1000)
        
    def bEnquiry(self):
        print("Hello {},Balance in Your Current Account,ends with xxxxxxxxx{}- Balance is Rs:{}/-".format(self.name,self.account_number[9:],self.balance))


print("Welcome to {} Bank".format(Account.BANKNAME))
print("Do You Want To Open Savings or Current Account: ")
print("s-SavingsAccount\nc-CurrentAccount: ")
option=input("Enter your choice: ").lower()
count=1
while option not in['s','c']:
    if count>=3:
        print("Sorry, Max number of attempts reached,Try after sometime")
        sys.exit()
    option=input("select a valid option[s|c]: ").lower()
    count=count+1
if option=='s':
   account=util.createAccount('Savings')
else:
   account= util.createAccount('Current')
# print(util.history)

while True:
    print("---------------------------------------------")
    print("b - Balance Enqury\nd - Deposit\nw - Withdraw\nm - Mini Statement\ns - Detailed Statement\ng - Get Account Information\ne - Exit")
    option=input("Choose your option: ").lower()
    
    while option not in['b','d','w','m','s','g','e']:
        option=input("Choose your option is invalid,Choose Correcrt Option[b|d|w|m|s|g|e]: ").lower()
        if option=='b':
            account.bEnquiry()
    