#dynamically typed programming lanauge
#duck typing programming lanauge
# never mention datatypes before varibles explicity in python
#based on the data we provide, python will automatcically assign corresponding datatype
#all datatypes called class ex <class 'int'>
# 14 inbuild data types
#int
#float
#complex
#bool
#str
#bytes
#bytearray
#range
#list
#set
#frozenset
#tuple
#dict
#None

no=10
print(type(no))

result=True
print(type(result))

value=9.0687687
print(type(value))

name="prabu"
print(type(name))

name1='prabu'
print(type(name1))

name="prabu"
print(id(name)) #id is adderss of action

name="prabu"
print(len(name))

no=123.5546454747
print(no)
print(round(no))
print(round(no,2))
print(round(no,3))

#num=123
#print(len(num)) #length only working string only not a numbers

#int datatype

#decimal form
#binary form
#octal form
#hexadecimal form

#all above form run will show in decimal

#binery: #o and 1 only allowed
no=0B0101
print(no)

#octal:

#num=O077
#print(num)

#hexa decimal

nrs=0X123
print(nrs)

#Float datatype

nofloat=1.65446524
print(nofloat)
print(type(nofloat))

no2=7.7e3 #e3 means 10 power 3
print(no2)

#complex datatype:

#real part + imaginary part

com=5+10j
print(com)
print(type(com))

com1=10+3j

total=com+com1
print(total)

print(com1.real)
print(com1.imag)

#boolean data type

#bool=True or False

n=10
b=20
print(n>b)#False
print(n<b)#True
print(n==b)#False
print(n!=b)#True

#T and F should capital letters

present=False
print(present)
print(type(present))

print(True+True) #1+1=1
print(False+False)#0+0=0
print(True+False)#1+0=1

#String datatype

#word/paragraph
#single/double quotes is string

#triple quotes use for string inside quote
#python special """

sen="""prabu's good boy, he said good "hi" """
print(sen)


name="prabu"
city="namakkal"
print(name+city) #concat without space
print(name, city)#conactwiths space

name="prabu"
pin=64654564
#print(name+pin)#type mismatch str+int
print(name, pin)

#string functions

#negative indexing avilable----->right -1 -2 -3
#forward indexing ---0 1 2 3 4 / backward indexing or negative indexing----1 -2 -3 -4
#left 0 1 2 3
#right -1 -2 -3


#slice:
name='rajarajacholanprint'
print(name[0:5])#first 5 letter
print(name[7:])#after 7 letter to end 
print(name[:4])#start first letter to 4
print(name[4:8])#4th letter to 8th


name12='abcdefghijklamanopqrstuvwxyz'
print(name12[0:5])
print(name12[-1:])
print(name12[5:10])
print(name12[-1:2])
print(name12[-1:-5])
print(name12[-5:-1])

#slice function:

name23='shajahadadas'
print(name23[::])
print(name23[1:10])
print(name23[1:10:2])
print(name23[6:1:-1])

alpah='abcdefghijklmnopqurstuvwxyz'
print(alpah[-26:-1])
print(alpah[-26:-1:4])
print(alpah[:-1:])

#string reverse
print(alpah[::-1])

print(alpah[0:-5])
print(alpah[10:1-2])
print(alpah[::4])

name='tub'
print(name*3)#3 times tub wil print '+' not use corresponding example but '*' use