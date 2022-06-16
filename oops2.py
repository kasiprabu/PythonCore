'''import sys
class customer:
    bankname="AXIS Bank"
    def __init__(self,name, accno, balance=0):
        self.name=name
        self.accno=accno
        self.balance=balance

    def deposit(self, amount):
        self.balance=self.balance + amount
        print("successfully deposited you amount", amount)
        print("current balance is now", self.balance)
    def withdrown(self, amount):
       self.balance=self.balance - amount
       print("successfully withdrawn you amount", amount)
       print("current balance is now", self.balance)

print("welcome to ", customer.bankname)#class varible access classname
cname=input("Enter the name: ")
accno=int(input("Enter the account number: "))
prabu=customer(cname, accno)
while True:
    print("D - deposit, W - withdraw, S-stop")
    choice=input("Eneter your choice: ")
    if choice=='D':
        amount=int(input("Enter the deposit amount: "))
        prabu.deposit(amount)
    elif choice=='W':
        amount=int(input("Enter the withdrawamount: "))
        prabu.withdrown(amount)
    else:
        sys.exit()

        #inheritence:
        #an object of one class behaving as an object another one class.
        #HAS-A Relationship
        #IS-A Relationship
        #composition

#has a relationship

class engine:
    milege=50
    def __init__(self):
        self.patrol=True
    def enginestart(self):
        print("engine smooth strart")

class car:
    def __init__(self):
        self.engine=engine()
    def drive(self):
        print(self.engine.patrol)
        self.engine.enginestart()

swift=car()
swift.drive()

#is a relationship
# child parent relationship
#aggregation 

class reservebank:
    name="reservebank of India"
    def __init__(self):
        self.mbalance=200
    def deposit(self):
        print("deposit the amount")
    def withdraw(self):
        print("withdraw the amount")
    @staticmethod
    def loan():
        print("this is loan section")
    @classmethod
    def fd(cls):
        print("this is fixed deposit section")

class BoT(reservebank):
    pass


attur=BoT()
attur.deposit()
attur.withdraw()
attur.loan()
attur.fd()

#note parent class all method(constrctor, instance method, static method, class method) everting acces in chuld class

class vasanthandco:#parent class or superclass
    add="chenni"
    def __init__(self):
        self.ho_offer=1000

class vasanthandcomadurai(vasanthandco):#child class or sub class
    add="madurai"
    def __init__(self):
        super().__init__()#im accessing immediate super class, parent class constrctor access pannikalam
        #super class instance vaiable acces pana use poron
        self.bo_offer=500

prabu = vasanthandcomadurai()
print(prabu.bo_offer)
print(prabu.ho_offer)
print(prabu.add)


class humanbeing:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def readbook(self):
        print("human being read the book")

class employee(humanbeing):
    def __init__(self, name, empid, salary):
        super().__init__(name, 60)
        self.name=name
        self.empid=empid
        self.salary=salary
    def dowork(self):
        print("doworking")
    def emp_details(self):
        print(self.name)
        print(self.empid)
        print(self.salary)
        print(self.age)

emp1=employee("raja",1,45000)
emp1.dowork()
emp1.emp_details()
emp1.readbook()'''

#multilevel inheritence

class Reservebank:
    def deposit(self):
        print("welcome to deposit")
    def withdrawn(self):
        print("welcome to withdrawn")
class SBI(Reservebank):
    def educationloan(self):
        print("welcome education loan")
        
class cooerativebanck(SBI):
    def agriloan(self):
        print("welcome to agri loan")
        print("above all section availble in cooertive bank")
v1=cooerativebanck()
v1.deposit()
v1.withdrawn()
v1.educationloan()
v1.agriloan()

#highrachy inheritence