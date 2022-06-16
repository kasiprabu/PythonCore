#iter()
#function and yield keywoard
#geneator local varible store the values
#iterator not generate local varible
#itreator better then geneator the memory allocation
'''my_list=[1.2,34,4,5]
my_list=iter(my_list)
print(my_list)
print(next(my_list))
print(next(my_list))
print(next(my_list))
print(next(my_list))

#its is an object
#number of values present itreator
#***list, dict, tuple itrable object, thease all items in called itrator
#iterator represented in python __iter()__ or __next__() and iter()

mytuple=("banana", "apple", "orange")
it=iter(mytuple)
print(it)
print(next(it))
print(next(it))
print(next(it))

#itrate in string
fruit="banana"
fru=iter(fruit)
print(fru)
print(next(fru))
print(next(fru))
print(next(fru))
print(next(fru))

#itreator use loop
for i in fruit:
    print(i)

    itrable:
    list, tuple, set , dict all is itrable
    ex: a=[1,2,3]
    for i in a:
        print i

x=[1,2,3,4,5,6,7]
it=iter(x)
print(it)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
try:
    print(next(it))
except StopIteration:
    print("this itretion is over")'''

#generators:

#its create iterator 
#yield keyword base itreator

def square1(n):
    for i in range(n):
        yield i**2

var=square1(3)
it=iter(var)
print(it)
print(next(it))
print(next(it))
print(next(it))
try:
    print(next(it))
except StopIteration:
    print("this is over the generator")






