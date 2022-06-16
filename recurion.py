#recursion
#function calling itself
#recursive
#curve writting
#function of statements recursion
#block:
#if while for write is block of ststement
#funtion call again and again
#when function true only that time its runngaian again
#conditions:
#function must use
#not use looping condition
#if staement use for stop recursion 

'''example 1:
def getusernamepassword(username, password):
    if username != 'abc':
        print("incorrect username")
        username=input("enter the username")
        password=input("enter the password")
        getusernamepassword(username, password)
    elif password != 'abc':
        print("incorrect password")
        username=input("enter the username")
        password=input("enter the password")
        getusernamepassword(username, password)

username=input("enter the username")
password=input("enter the password")
getusernamepassword(username, password)

#example 2:
def additions(b):
    print(b)
    b+=1
    if b<=10:
     additions(b)

additions(1)

#addtion of digits
#factorial
#GcD
#LcM
#fibbonacci

#example3:

fact=1
for i in range(1,6):
    fact=fact*i
    print(fact)

def fact(num):
    if num==1:
        return 1
    else:
        return num * fact(num-1)
result=fact(7)
print(result)'''

#example3:
#sum of digits

def sumofdiguts(number):
    if number==0:
        return 0
    else:
        rem=number%10
        no=number/10
        total=rem +sumofdiguts(no)
        return total
result=sumofdiguts(1543) 
print(result)

print(__name__)

#need to use recussion

#palindrome
#armstrong
#reverse a string
#reverse a sentence
