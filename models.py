#modeules- core strength
# modules nothing but python files 
#1. varaible, functions call, print, arguments, return, function define, predefind function

def fun(n, f):
    #pass skip and move to forward
    s=n+f
    print(s)
fun(10,20)

#reuse modules
#import one - one module alrady availble file name
#one.biggest(100,200)--->one already file and biggest function and (100,200) arguments for function

#build in modules

#cmd-->help('modules')->lis show

import math
n=math.factorial(5)
print(n)
m=math.remainder(5, 2)
print(m)
print(math.sqrt(100))
print(math.cos(50))
print(math.ceil(5.2))
print(math.floor(5.2))

print(math.pi)
area=(math.pi * 7 * 7)
print(round(area,2))

from math import pi
area1=(pi * 7 * 7)
print(area1)

#eval() ---> string input chnage mathamatical expression
val=input("enter ur expression")#5*2+10-3/4
eva=eval(val)
print("eval", eva)

#command line arguments

import sys


no1, no2, no3=12,34,56
print(no1, no2, no3, sep=":")
print(no1, no2, no3, end=":")

print("\n raja", end="*")
print("ravi")

#formated string:

# %i %d %f %s

no1, no2, no3=10,20,30
print("no1 on value %d" %no1)#int type
print("no1 on value %i" %no1)#int type

name="prabu"
print("hi, name")
print("hi %s" %name)

print("no1 value %d and no2 values %d"%(30,40))

value=3.14
print("values is %f"%value)




