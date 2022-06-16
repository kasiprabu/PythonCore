#compound datatype

#collective datatypes

#one object inside multiple objects

#group pf objects into a single enity

#list, tuple, dictionary

#list:
#======

#list of items

#insertion order is maintained

#duplicate object are allowed

#Heterogeneous object are allowed(all data types are allowed)

#list objects are mutable

#negative indexing are allowed


#list creation 1:

grocerry=[6]
print(type(grocerry))
print(len(grocerry))
print(grocerry)

#list creation 2:
marklist=[89,45,67,89,65]
print(marklist)

#string into list

name='prabu'
l=list(name)
print(l)

#range function use create list:
listr=list(range(9))
print(listr)

#split function
sentence="happy new year"
list=sentence.split()
print(list)

date='31-05-2022'
listdate=date.split('-')
print(listdate)

#list accessing

l=[10,20,'a', True]
print(l[0])
print(l[1])
print(l[2])
print(l[3])
print(l[-1])#negative indexing

#slice 
l=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(l[2:8:2])#[start:end:movenet]

la=[10,20,30,40,50]
for i in la:
    if i%20==0:
        print(i)

#hetrogeinous object
listy=[10,20,30,40]
listu=['a','b','c']
l3=listy+listu
print(l3)
print(type(l3))
print(len(l3))
print(l3*2)

#list can contain another list

l4=[listy, listu]
print(len(l4))

for i in l4:
    print(i)


#List comprehension

ll=[i**i for i in range(1,4)]
print(ll)

l1=[val for val in ll if val%2==0]
print(ll)

names=['raja', 'ravi', 'dinesh', 'kumar']#it takes every first index values
n=[name[0] for name in names]
print(n)
n=[names[0] for name in names]
print(n)
