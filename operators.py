#relational operators

#> >= < <==-->applicable sting use

name1='prabu'
name2='kavi'
print(name1>name2)  #lexicographical order-dictionary

#escape statements
print("hi hw r u")
print("hi \t hw r u")
print("hi \n hello")
print("I\"m fine")

#constants
#python not avialble constsnts, but python write capital letters

#assignmnt operators
#+= -= *= /= //= %= **=

no=10
no+=6
print(no)

no1=5
no1*=5
print(no1)

#ternary opertor/conditional opertors

n1, n2 ,m3=45, 56,78#single line multiple assign not possible
print(n1)

#memership operators

#in not in

word="today is friday"
print('t' in word)#true
print('w' in word)#false
print('h' not in word)#true

#operator chaning:

print("chain", 100<200>300)

#bitwise operators

# & | ` >> <<
print(4&5)
print(4|5)
print(4^5)

print(40>>2)
print(40<<2)

#logical operators


#and or not


#replacement operator:

#{} placeholder

name='prabu'
city='attur'
acno=12345
print("hi {0} your accno is {1} and you are from {2}".format(name, acno, city))
print("hi {a} your accno is {b} and you are from {c}".format(a=name, b=acno, c=city))
print("hi {} your accno is {} and you are from {}".format(name, acno, city))




