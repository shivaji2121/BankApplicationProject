# modules importing.........
from random import randint
from abc import ABC,abstractmethod
import sys
import datetime



# All methods and useful things are here...
class Util():
    history=[]
    @staticmethod
    def generateAccountNumber():
        acc_no=""
        for i in range(12):
            acc_no=acc_no+str(randint(0,9))
        return acc_no
    
    @classmethod
    def addEntry(cls,msg):
        Util.history.append(msg)
        
        
    @staticmethod
    def createAccount(accountType):
        if accountType=='Savings':     
            name=input('Enter Your Name: ')
        else:
            name=input('Enter Company Name: ')
            
        balance=float(input("Enter Your Initial Balance: "))
    
        while balance<0:
            balance=eval(input('Initial Balance Should not be Negative/Minus,Please Enter valid value: '))
        if accountType=='Savings': 
            account=SavingsAccount(name,balance)#here we are creating OBJECT of SAVINGS ACCOUNT CLASS
        else:
            account=CurrentAccount(name,balance)
        Util.addEntry('{} - {} Account Created With A/C NO:{} and with Initial Balance-{}'.format(datetime.datetime.now(),accountType,account.account_number,account.balance))
        print('Congratulations,Your {} Account Created Successfully with A/C NO:{}'.format(accountType,account.account_number))
        return account
    
    
    @classmethod
    def getdetailedStatement(cls):
        print(cls.history[0])
        print('Your Last {} Transactions are '.format(len(cls.history)-1))
        print('#'*50)
        for transaction in cls.history[1:]:
            print(transaction)
            
            
    @classmethod
    def miniStatement(cls):
        print(cls.history[0])
        if (len(cls.history)-1)<=5:
            print('Your Last {} Transactions are '.format(len(cls.history)-1))
            print('#'*50)
            for transaction in cls.history[1:]:
                print(transaction)
        else:
            print('Your Last 5 Transactions are ')
            print('#'*50)
            for transaction in cls.history[-5:]:
                print(transaction)


# Account class like main class....
class Account(ABC):
    BANKNAME='SBI'
    def __init__(self,name,balance,minimum_balance):
        self.account_number=Util.generateAccountNumber()
        self.name=name
        self.balance=balance
        self.minimum_balance=minimum_balance
        
    # deposit method....
    def deposit(self):
        amount=float(input('Enter Amount to Deposit: '))
        while amount<0:
            amount=float(input('Inavalid Account,Enter Valid Amont to Deposit: '))
        self.balance+=amount
        Util.addEntry('{} - Account Credited(Deposit) With Amount:{}'.format(datetime.datetime.now(),amount))
        print("After Deposit,Your account Balance: ",self.balance)
    
    # deposit method....
    def withdraw(self):
        amount=float(input('Enter Amount to Withdraw: '))
        while amount<0 or amount%100!=0:
            amount=float(input('Amount should be Positive and Multiples of 100,Enter Valid Amount to withdraw: '))
        if self.balance-amount >=self.minimum_balance:
            self.balance-=amount
            Util.addEntry('{} - Account Debited With Amount:{}'.format(datetime.datetime.now(),amount))
            print("After Withdraw,Your account Balance: ",self.balance)
        else:
            print("Sorry,Insufficient Funds")
        
    @abstractmethod
    def balanceEnquiry(self):pass
    
    @abstractmethod
    def getAccountInfo(self):pass
    
    

# Child class of Account....SavingsAccount
class SavingsAccount(Account):
    def __init__(self,name,balance):
        super().__init__(name,balance,0)
        
    
    # balance enquiry...
    def balanceEnquiry(self):
        print('Hello {},Balance in your Savings Account,ends with xxxxxxxxx{} is:RS {}/-'.format(self.name,self.account_number[9:],self.balance))
    
    # Account Information...
    def getAccountInfo(self):
        print("-----Your Savings Account Information-----")
        print("Account Number: ",self.account_number)
        print("Customer Name: ",self.name)
        print("Current Balance: ",self.balance)
        print()


# Child class of Account....CurrentAccount
class CurrentAccount(Account):
    def __init__(self,name,balance):
        super().__init__(name,balance,-1000) 


    # balance enquiry...
    def balanceEnquiry(self):
        print('Hello {},Balance in your Current Account,ends with xxxxxxxxx{} is:RS {}/-'.format(self.name,self.account_number[9:],self.balance))
    

       # Account Information...
    def getAccountInfo(self):
        print("-----Your Current Account Information-----")
        print("Account Number: ",self.account_number)
        print("Customer Name: ",self.name)
        print("Current Balance: ",self.balance)
        print()



# main program.....
print("Welcome to ",Account.BANKNAME)
print("Do You Want to Open Savings or Current Account")
print("s - Savings Account: \nc - Current Account: ")
option=input("Choose Your Option: ").lower()
count=1
while option not in ['s','c']:
    if count>=3:
        print("Sorry,Maximum attemps Reached please try later")
        sys.exit()
    option=input("Enter a valid option[s|c]: ")
    count=count+1
if option=='s':
    
  account=Util.createAccount('Savings')
   
else:
    
    account=Util.createAccount('Current')

print(Util.history)

while True:
    print('b - Balance Enquiry\nd - Deposit\nw - Withdraw\nm - Mini Statement\ns - Detailed Statement\ng - Get Account Information\ne - Exit')
    option=input('Choose Your Option: ').lower()
    while option not in['b','d','w','m','s','g','e']:
        option=input('Your option is invalid,Choose Correct Option[b|d|w|m|s|g|e]: ').lower()
    if option=='b':
        account.balanceEnquiry()
    elif option=='g':
        account.getAccountInfo()
    elif option=='d':
        account.deposit()
    elif option=='w':
        account.withdraw()
    elif option=='s':
        Util.getdetailedStatement()
    elif option=='m':
        Util.miniStatement()
    elif option=='e':
        print("Thanks for using SBI Bank Applicaton")
        sys.exit()
    else:
        print("Invalid Option,Choose Correct Option")
        option=input("Enter Valid Option: ").lower()
        
        
 