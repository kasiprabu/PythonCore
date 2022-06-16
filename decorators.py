from ast import arguments
from inspect import Parameter


'''decorator:
1. nested function
2. functions as a Parameter
3. functions as a ReferenceError
4. function return another function


#1. nested function

def outerfunction():
    msg1="welcome to"
    def innurfunction():
        msg2="python"
        outer=msg1+msg2
        return outer
    return innurfunction


obj=outerfunction()
print(obj())

#functions as a Parameter

def functionone():
    print("im first function")
def secondfunction(ref):
    ref()
    print("im second function")
    

secondfunction(functionone)

#decorators:
1. function decorators 
2. class decorators

Function decorators:

1. single decorators
2. multiple decorators

1. with arguments
2. without argument

we didnot touch function, but we change that functionality

#1. Single decortors

def changefunc(ref):
    def process():
        upps=ref()
        return upps.upper()
    return process
    
@changefunc
def originalfun():
    return "python programming"

print(originalfun())


#2. multi decortors

def changefunc(ref):
    def process():
        upps=ref()
        return upps.upper()
    return process

def splitfunc(ref):
    def process():
        upps=ref()
        return upps.split()
    return process
    
@splitfunc
@changefunc
def originalfun():
    return "python programming"

print(originalfun())'''

#2. decortors with arugument

def outerfun(str):
    def uppersting(ref):
        def process():
            val=ref()
            return  str + val.upper() 
        return process
    return uppersting



@outerfun(" super lanuage")
def orifun():
    return "python programming"

print(orifun())
