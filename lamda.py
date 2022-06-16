#anonymous function:
#lamda function
#lamda keyword use
#lambda num:num*num
#in projects small small calculations we have use

'''result=lambda num:num*num
print(result(6))

addition=lambda add:add+add
print(addition(8))

big = lambda no1, no2:no1 if no1>no2 else no2
print(big(7,5))

addion=lambda no1, no2:no1+no2
print(addion(79,65))'''

#lambda functions
#filter
#map
#reduce

#nested functions:

def outer():
    print("im outer function")
    def innur():
        print("im innur function")
    print("now i call innur function")
    innur()

outer()

print(__name__)
