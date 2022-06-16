'''#single inheritence
class tatasteel:
    def __init__(self, age, salary):
        self.age=age
        self.salary=salary

class employee(tatasteel):
    def __init__(self, empid,name,age,salary):
        super().__init__(age, salary)#super class constrctor access panna mudiyum
        self.empid=empid
        self.name=name

def __str__(self):#whenever print function internally print function called __str__function
    return 'Name={}\n salary={}\n age={}\n empid{}\n'.format(self.name, self.salary, self.age, self.empid)

emp1=employee(1, "prabu", 31, 45000)
print(emp1)
#note:
#if print an object, memory ref of the object will be print_directory
#in python everything is object 
#hence, if i print anaything in python, memory ref will get print_directory

#multilevel inheritence:

class grandparent:
    def agriculture(self):
        print("did agriculture")
class parent(grandparent):
    def techer(self):
        print("now working techer")

class child(parent):
    def engineer(self): 
        print("now working software engineer")

c1=child()
c1.engineer()
c1.techer()
c1.agriculture()

#hierarchy inheritence:

class honda:
    def automobile(self):
        print("world largest automobile company")
class bike(honda):
    def shine(self):
        print("Honda shine")
class car(honda):
    def city(self):
        print("honda city")

c1=car()
c1.automobile()
c1.city()
c1.shine()#car class object cannot acces in bike method, same bike method not acces car method


#multiple inheritence

class father:
    def painter(self):
        print("father is good apainter")
    def goingtojob(self):
        print("father is painter")
class mother:
    def tailor(self):
        print("mother is good tailor")
    def goingtojob(self):
        print("mother is tailor")
class child(father, mother):#priority wise take same name method two parent class
    def studying(self):
        print("child is studying")
        #father.goingtojob(self)

c1=child()
c1.studying()
c1.tailor()
c1.painter()#more then one parent only one child
c1.goingtojob()#both parent class have same function name(goingtojob), python take priority wise for child class inhert(father, mother).
father.goingtojob(self)

class prabu:
    m=80
    def __init__(self):
        self.j=40
class kavi(prabu):
    def m1(self):
        print(super().m)#class varible we can access use super()
        print(self.j)#super class instance varible we can axccess use self

k=kavi()
k.m1()'''

class super():
    h=90
    def __init__(self):
        self.j=200
        print("hi im super class")

    def dis(self):
        print("super class method")

class sub(super):
    def __init__(self):
        super().__init__()
        super().dis()

    def subfun(self):
        print(super().h)
        print(self.j)

cl=sub()
cl.subfun()
#we have use super() call static,class methodds and class varible and constrctors in super class

#super()-->super class-->class level varible and instance variable access panna mudiyum

#super()-->from child class constrcutor and child class instance method, using

#super()===>accessing all types of 