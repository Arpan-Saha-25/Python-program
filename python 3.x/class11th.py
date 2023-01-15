print(1.76*12)
p = 10000
r = 2
t =2
simInt = (p*r*t)/100 
print(simInt)
a = 14212
b= 213124
#a= int(input("ENter the no." ))
#b= int(input("Enter the 2nd no."))
sum = a + b 
print("result of sum : ",sum)

if a >= 10 :
     print(" \n greater than or equal 10  [¢]")
else : print("⌂")

#odd even
a= 24#int(input("ENter the no." ))
b= 67#int(input("Enter the 2nd no."))
if a%2 ==0:
    print(a,"is even.")
else: 
    print(a,"is odd.")
if b%2 ==0:
    print(b,"is even.")
else :
    print(b,"is odd.")
if a%2==0 and b%2==0:
    print("both are even.")
else : print("both are odd.")

age= 18#int(input("ENter your age :'"))
if age>= 18:
    print ("----------> eligible")
else :
    print ("ineligible")

a = "Arpan Saha"
print(a[0:4])
print(a[0:])
print(a[:4])
print(a[4:6])
print("length",len(a))
print(a.lower())
print(a.upper())
print(a.replace("a"," lol "))
print(a.split(" "))
#using for loop 
for i in range(1,6):
    print("yessss " , i)
for i in range(6,1,-1):
    print("yessss " , i)
for i in range(5):
    print("0p " , i)
for i in range(1,6,3):
    print("3 jump liya " , i)

a=["elephant",'monkey','croc',"hippo"]
print(a[1][3])
print(a[1][2])
print(a[0][0])

for i in range(1,6):
    for r in range(1,i+1):
        print("*",end=" ")
    print("\n")
print("------------------")
for i in range(5,0,-1):
    for a in range(i+1,1,-1):
        print("*",end=" ")
    print("\n")

#functions

for e in range(6):
    a = 34 #int(input("Enter a no. : "))
    w = 35 #int(input("Enter 2nd no. : "))
    sum1= a+ w
    print(sum1,e)

def addition():
    a = 2#int(input("Enter a no. : "))
    w = 3 #int(input("Enter 2nd no. : "))
    sum1= a+ w
    print(sum1)

addition()
addition()
print("hdsgf")
addition()
print("hdsgf")
addition()
print("khatam ok tata bye bye !!!!")

def sum2():
    a = 2 #int(input("Enter a no. : "))
    w = 3 #int(input("Enter 2nd no. : "))
    sum1= a + w
    print(sum1)
def multiply():
    a= 4
    b= 3
    print(a*b)

sum2()
multiply()
print("theek hai α")
multiply()
sum2()
sum2()
multiply()
