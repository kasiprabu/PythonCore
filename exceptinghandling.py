#Error: deveploper error
#syntax error
'''no1=int(input("Enter the number"))#10
no2=int(input("Enter the number"))#0
print(no1/no2)

#exception is runtime error
#whenever ecxeption occur the coresponding ecxeption object wil be given /thrown to the end user
#ecxetion can have sepertae class avialble(ioecxeption. divisiablezero)
#every ecxeption in python is a class
#all exception classes are child /sub classes of baseexception
#druning rruntime if ecxeption occurs, pythin will throw us the exception class  and stops the programm immediately
#
try: 
    no1=int(input("Enter the number: "))#10
    no2=int(input("Enter the number:"))#0

    print(no1/no2)#risky code
except ZeroDivisionError:#u know name of exception use name or use only ecept only
    print("its seems like zero")
except ValueError:
    print("incorrect the value")
print("hi")

def exhand():
    try:
        no1=int(input("Enter the number: "))
        no2=int(input("Enter the number: "))
        print(no1/no2)
    except ZeroDivisionError:
        print("something wnet wrong")
        exhand()
    except:
        print("pls check")
        exhand()
exhand()

#finally-- always run with exception or without exception

def exhand():
    try:#try block
        no1=int(input("Enter the number: "))
        no2=int(input("Enter the number: "))
        print(no1/no2)#risky code
    except ZeroDivisionError:#handling code
        print("something wnet wrong")
        #exhand()
    except:
        print("pls check")
        #exhand()
    finally:#cleanup code
        print("finsih the program")

exhand()

#os._exit(0)-->python virtual mavhine down agidum so finally block not wotking 
#nested try possible to handle

try:
    n1=int(input("Enter the first number: "))
    n2=int(input("Enter the second number: "))
    try:
        print(n1/n2)
    except ZeroDivisionError:
        print("Pls check the number")
    finally:
        print("n1 and n2 values given")
except ValueError:
    print("corect the values")
finally:
    print("value is correct and check")

    #else part:

try:
    print('try block')
    print(100/2)
except:
    print("Exception occured")
else:#exception not occured use else
    print("exception not occured")
finally:
    print("program end successfully")'''

#customize or userdefind exception
#customize exception crete use raise keyword

class InsufficientBalanceException(Exception):
    def __init__(self, msg):
        self.msg=msg

balance=300
#try:
amount=int(input("Enter the amount: "))
if amount>balance:
    raise InsufficientBalanceException("check your balance")#this line gpoing line 88
#except InsufficientBalanceException:
    #print("im user defind exception handling area")

#anonymous object 

class InsufficientBalanceException(Exception):
    def __init__(self, msg):
        self.msg=msg

balance=300
try:
    amount=int(input("Enter the amount: "))
    if amount>balance:
        raise InsufficientBalanceException("check your balance")#this line gpoing line 88
except InsufficientBalanceException:
    print("im user defind exception handling area")


