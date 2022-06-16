'''#class creation

class student:
    #This class is about studentdocumentation string
print(student.__doc__)
help(student)#what are items availble in class we use

#ex2:
class SuperMarket:
this is supermarket

bread=SuperMarket()
bread.band="abc"
bread.price=24
biscut=SuperMarket()
shampoo=SuperMarket()
rice=SuperMarket()
print(bread.band)
print(bread.__dict__)#bread object all properties we see use __dict__


#ex3: Constrctor
#once object creted automatically iniitiated
#its building in a class
#this is special function
#automatcially is getting called ot invoke the automatically  whenever we create object
#initilizing object specific information use constrctor
#default constrctor is invisible
#self variable
#multiple copies will be maintained

#class specific variable:
    #only one copy will be maintaned
    
class supermarket:
    manifact="PK Super market"#class specific vaiable
    marketer="PKS"#class specific vaiable
    def __init__(self, bname, bprice):#formal parameter #object pathi inital value kodupathu
        self.brand=bname
        self.price=bprice
        print("checkme")#constrctor working sample

bread=supermarket("tiger",5)#actual parameter
print(bread.brand)
biscut=supermarket("mgold",10)
print(supermarket.manifact)#class specific variable access use classname
print(supermarket.marketer)
bread.manifact="goodday"#object vachi class variable la access panna mudiyam, andha object value change agum
print(bread.manifact)

class customer:
    def deposit(self, dposit):
        print("prabu u doposit amonut", dposit)

prabu=customer()
print(prabu.deposit(500))#its al local variable, i use only one function

class test:
    a=100
    def __init__(self):
        self.b=40

t=test()
print(t.b)#40
print(t.a)#100
t.a=777
print(t.a)#777
print(test.a)#100

#functions/methods
#types of methods



#1.instance methods[sample]--->instacne or object both are same--->
    #whereever use self varible use pannitho athellam instance menthods
#2. class methods
#3. static methods


#instance methods
#whereever use self varible use pannitho athellam instance mentthods
class student:
    def __init__(self, name, marks):
        self.name="prabu"
        self.mark=90

    def display(self):#this is instance methods
        print("hi", self.name)

prabu=student('prabu', 600)
prabu.display()

#class methods
#inside function definition, class specific varible only are used
#@classmethod decorter using
#cls variable used
#can call class name by using class name or object reference.

class office:
    noofholidays=10
    @classmethod
    def checkholiday(cls, branch):
        print('this year our',branch,'has', cls.noofholidays)
office.checkholiday('chennai')

#static methods
#utility methods
#use @staticmethod decorader used

class calculator:
    @staticmethod
    def add(no1, no2):
        print('result is',no1+no2)

calculator.add(100,200)

# class method                           #static method
#@class method                            @staticmethod
#arguments cls                            no cls, no self
#class level varibles                     local level variable used


class
object
constructor
types of varible(object(instance), class, local)
types pf methods -instance, class, staticmethod
decorders used @classmethod, @staticmethod'''










