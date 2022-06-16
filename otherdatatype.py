#byte 8 bit 2 power 8
#256 value maximum
#
#byte value cannot change, once assigned could not change

value=[90,45,78,43,89]
print(value)
print(type(value))
value=bytes(value)
print(value)
print(value[0])
print(value[-1]) 

total=0
for no in value:
    print("pp:", no)
    total=total+no
print(total)

#odd or even numbers

input=int(input("enter the number\n"))#input function automatcally considerd String only
print(type(input))
if input%2==0:
    print('even number')
else:
    print('odd number')

    numcheck=[45,67,54,23,97]
    for n in numcheck:
        if n%2==0:
            print(n, 'even number')
        else:
            print(n, 'add numbers')