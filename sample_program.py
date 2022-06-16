'''

mark=int(input("enter the you marks\n"))
if mark>=90:
    print("A+")
elif mark>=80:
    print("A")
elif mark>=70:
    print("B+")
elif mark>=60:
    print("B")
else:
    print("")

#below progam make some nested loop not working 

no1=int(input("enter the first nmber\n"))
no2=int(input("enter the second number\n"))
no3=int(input("enter the third number\n"))

if no1>=no2:
    if no1>=no3:
        print(no1, "number one big")
elif no2>=no3:
    if no2>=no1:
        print(no2, "number two big")
elif no3>=no1:
    if no3>=no2:
        print(no3, "number two big")

#correct one

n1=int(input("enter the first nmber\n"))
n2=int(input("enter the second number\n"))
n3=int(input("enter the third number\n"))

if no1>=no2 and no1>=no3:
    print(no1, "number one big")
elif no2>=no3 and no2>=no1:
    print(no2, "number one big")
elif no3>=no2 and no3>=no1:
    print(no3, "number one big")

#iterative statement:
mind=8
while True:
    guess=int(input("enter your choice 1 to 10\n"))
    if guess==mind:
        print("correct")
        break
    elif guess>mind:
        print("you guess to large")
        break
    elif guess<mind:
        print("your guess is to small")
        break


#multiple if is while
#+ + + -->*
count=1
while(count<=5):
    print(" ",count, end='')
    count=count+1

#empty print statemnt new line

count=100
while(count>=1):
    if count%5==0:
        print()
    print(" ",count, end='')
    count-=1


#range:
for num in range(5):
    print(num)

for num in range(1,5):
    print(num)
for num in range(1,5,2):
    print(num)

for num in range(10,1,-2):
    print(num, end=" ")

#table format
no=1
for num in range(3, 90, 3):
    print(no, " * 3 = ", num)
    no+=1
'''

#factorial program

x=list(range(2,8,2))
#res=x[-1]+x[1]
#print(res)
print(x)
