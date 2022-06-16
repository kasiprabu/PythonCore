#text file and binary file
#text file, pdf file, image, audio, video -binary file

'''mode:
r-->read
w--->write
a--->append
r+---->read and write
w+---->write and read
a+---->appending
x----->exclusive(file exists)

file=open("C:\python\intro.txt",'w')
print(file.name)#C:\python\intro.txt
print(file.mode)#w
print(file.readable())#False
print(file.writable())#True
print(file.closed)#False
file.close()
print(file.closed)#True

#file write

f=open("C:\python\intro.txt", 'w')
f.write("prabu kasi\n")
f.write("salem")
f.close()

#list in file handling

f=open("C:\python\intro1.txt",'w')
ll=['prabu\n','kavitha\n','ramkumar\n', 'ravi\n']
f.writelines(ll)#write multiple line in file
f.close()

#reading files:
f=open("C:\python\intro.txt",'r')
con=f.read(10)#file read#10 how many charcter want we read
f.close()
print(con)
print(type(con))

#linebyline read
f=open("C:\python\intro.txt",'r')
content=f.readline()#curser move to stating possition#line by line
print(content)
f.close()

f=open("C:\python\intro.txt",'r')
content=f.readlines()#curser move to stating possition#line by line
for i in content:
    print(i)
    print(type(i))#i is type str
print(content)
print(type(content))
f.close()
#readline-->retuern in string
#readlines--->return list

#python file handling:
with open("C:\\python\\text.txt","w") as file:
    file.write("acac")
    file.write("asd")

#filename avialble or not

import os, sys
fiename=input("Enter the file name: ")
if os.path.isfile(fiename):
    f=open(fiename,'r')
    con=f.readline()
    print(con)
else:
    print("file is not present")

import os, sys
fiename=input("Enter the file name: ")
if os.path.isfile(fiename):
    f=open(fiename,'r')
    lcount=wcount=ccount=0
    for line in f:
        word=line.split()
        wcount+=len(word)
        ccount+=len(line)
        lcount+=1
    print("line count: ", lcount)
    print("word count: ", wcount)
    print("char count: ", ccount)
else:
    print("file not present")

#binary data:
#image

inputfile=open("C:\python\duck.png",'rb')
output=open("C:\python\duck1.png", 'wb')
byte=inputfile.read()
output.write(byte)

#csv file reading and writing
import csv
with open("student1.xsls","w", newline='') as file:
    pen=csv.writer(file)#wriyer object
    pen.writerow(["SID","SNAME","SADDRESS"])
    count=int(input("Enter no of students: "))
    for i in range(count):
        sid=int(input("Enter the student ID: "))
        sname=input("Enter the student name: ")
        sadd=input("Enter the student address: ")
        pen.writerow([sid,sname,sadd])

        #read:
import csv
with open("student.csv","r", newline='') as file:
    pens=csv.reader(file)#wriyer object
    output=list(pens)
    for line in output:
        for eachword in line:
            print(eachword, end=' ')
        print()
'''
#folder creation

from copyreg import pickle
import os
#os.mkdir("C:\python\one1")
#os.makedirs("xyz/XYZ/z")
#os.rmdir("C:\python\one")
os.removedirs("C:\python\xyz")

#pls refer to internet
#pickling and unpickling:
#pickle.dump(s1,f)-->pickle
#pickle.load(f)--->unpickling


    
        



