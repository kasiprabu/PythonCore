#one shape to another one shape change is type casting
#converting one datatype can be change to another type

#INT:

no=88.98
print(int(no))#here float value change to int

print(int(True))
print(int(False))

#name="pk"
#print(int(name))string value we cannot use type casting

#FLOAT:

print(float(10))
print(float(True))
print(float(False))

doornum='10'
print(float(doornum))

#complex:
print(complex(10))
print(complex(5.4))
print(complex(True))
print(complex(False))
print(complex("12"))

print(complex(10,20))
print(complex(True, True))

#boolean:
#0 and empty apart from all is True
print(bool(0))#false
print(bool(1))#true
print(bool(1.5))#true
print(bool(0.3))#true
print(bool(5+4j))#true
print(bool("abc"))#true
print(bool("True"))#true
print(bool("False"))#true 
print(bool(""))#false

#String:

print(str(10))
print("price of the tra: " + str(10))

print(str(34.5)) 
print(str(5+10j))
print(str(True))
print(str(False))
print(str('boy'))

#14 data types
#fundamental data types

#IMMUTABL:

#all fundamenal data types are immutable[we cannot change]
#unchangable for memory addresss
#varaible value 10 and another one vaible value also 10, so python can both varible have same memory adress
#both varaible value different means memory address change
#once we change value of an identifier belongs to fundamental datatype
#it wont get changed in memory, insted of that a new memory location will be created and the new value will be updated there.


no=10
print(id(no))
no2=10
print(id(no2))
no2=30
print(id(no2))

ns=10
ns2=20
print(ns is ns2)

ns1=10
ns21=10
print(ns1 is ns21)#is ia check memeory address is same or not

print(ns1 == ns21)#== is identifiers(varaible) value is same or not 

print(ns1 is not ns21)

