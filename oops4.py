'''#duck typing example

class bike:
    def fill(self):
        print("fill the petrol")

class lorry:
    def fill(self):
        print("fill the diesel")

class ecar:
    def fill(self):
        print("fill the power")

def charbge(obj):
        obj.fill()

b=bike()
l=lorry()
c=ecar()

list=[b,l,c]

for obj in list:
    charbge(obj)

    #operator overloding

class book:
    def __init__(self, pages):
        self.pages=pages

    def __add__(self, another):#this function run based on line 39
        return self.pages + another.pages
    

thirukurl=book(100)
naladiyar=book(200)
print(thirukurl+naladiyar)

class book:
    def __init__(self, pages):
        self.pages=pages

    def __mul__(self, another):#this function run based on line 39
        return self.pages * another.pages
    

thirukurl=book(100)
naladiyar=book(200)
print(thirukurl*naladiyar)

+-->object.__add__(self, another)
- -->object.__sub__(self.other)
* -->__mul__(self, other)
/ -->div
// -->floordiv
% -->mod
** -->pow
+= -->iadd
-= -->isub
*= -->imul
/= -->idiv
//= -->ifloordiv
< --> __it__
<= -->__le__
#multiple class use operator overloading
class mobiles:
    def __init__(self, brand, price, offer):
        self.brand=brand
        self.price=price
        self.offer=offer

    def __gt__(self, other):#this method works on line no 79 based on
        return self.price>other.price
    def __add__(self, other):
        return m1.offer + cc.offer
class creditcard:
    def __init__(self, brand, offer):
        self.brand=brand
        self.offer=offer


m1=mobiles("nokia", 10000, 500)
m2=mobiles("samsung", 15000, 1000)
cc=creditcard("vivo", 1000)
print(m1>m2)
print(m1+cc)

#method overloading:

#same method name with different number of arguments
#method overloading last definiation only take 

class Test:
    def caculate(n01, n02):
        print("AAAA")
    def caculate(no1, no2, no3):
        print("BBB")
t=Test()
#t.caculate(10,20)
t.caculate(10,20,30)

#how solve above problem

class Test:
    def calculate(self, *no):#method overloading handle *
        total=0
        for i in no:
            total=total+i
        print(total)
t=Test()
t.calculate(10,20)
t.calculate(10,20,30)

#constrctor overloading:
class supermark:
    def __init__(self, *content):
        print("constructir chcek")

c1=supermark("soap", 20, 4)
c2=supermark("rice", 60)

#method overridding:

#same method different class(parent, child) callsed method overridding

class parent:
    def __init__(self):
        print("parent class constor")#child class object access parent class constuctor
    def study(self):#same name parent classed
        print("im a doctor")

class child(parent):
    def __init__(self):#child class constuctor presnet parent class constrctor not working, if we want parent clas constutor also use super keywoard
                print("child class constucor")
    def play(self):
        print("im playing")
    def study(self):#same method child class
        super().study()#parent class method access
        print("im a teacher")

c=child()
c.study()

#abtsrction:
#showing only the necrssary data and hiding unwanted

#defintion and implementation not defind is called 
#class with atleast one abstrct method.
#cant instantaite abstrct class 
#cant create object for 

#if we extend/inherit abstrct class and we dont override the absrct methods present in parent class, in the case child class is also considred as abstrct class and we couldn't instantiate create object for child class as well.

from abc import *
class Indian(ABC):#abatsct base class ilmana obejct create panalam
    @abstractmethod
    def havingbeakfast(self):
        pass

#one class all methods abstact means that is called interface

#globals() convert string into corresponding class name

from abc import *

class DBInterface(ABC):
    @abstractmethod
    def establishedDB(self): pass
    @abstractmethod
    def disconnectDB(self): pass

class OracleDB(DBInterface):
    def establishedDB(self):
         print("orcle Db Connection")
    def disconnectDB(self):
         print("orcle Db dizConnection")

class MYSQLDB(DBInterface):
    def establishedDB(self):
         print("MYSQLDB Db Connection")
    def disconnectDB(self):
         print("MYSQLDB Db dizConnection")

dbname=input("Enter the DB name: ")
classname=globals()[dbname]
c=classname()
c.establishedDB()
c.disconnectDB()
'''

#Encapsulation:
#Data binding
#all varibles 
#_ is protected
#__ is private
#outside class private varible not access
class Test:
    a=100
    _b=200
    __c=300
    def __init__(self):
        self.__no=1234

    def display(self):
        print(Test.a)
        print(Test._b)
        print(Test.__c)
t=Test()
t.display()
print(Test.a)
print(Test._b)
#print(Test.__c)#private varible not able access without class
print(t.__Test__no)#constrctor private vaible we can access outside class syntax
    




   






