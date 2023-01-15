#class 11th finals practicals exam practice
name = "world" #input("Enter  the name : ")
print("Hello from ",name)
print("thanks for visiting")
print (" \n __------________________-----------_______________--______----------_______-----")

p = 10000#int(input("Enter the values of the principal amt. = \t "))

r = 12 #int(input("Enter the values of the rate of interest = \t "))
t = 2 #int(input("Enter the values of the time period =\t "))

si= (p*r*t)/100
print(" \n simple interest of the following values = ",si)

#program 2
eng =  90 #int(input(" \n enter your marks in English = "))
maths = 100# int(input("enter your marks in Maths= "))
bio =   91#int(input("enter your marks in Biology = "))
print(eng , maths , bio)
total = eng + maths + bio
percentage =(total / 300) * 100

print("\t total marks obtained =  ", total)
print(" \tTotal percentage obtained = " , percentage)

if percentage >= 90 : print("---- > > > Grade A+")
elif percentage >= 80 : print ("---- > > > Grade B")
elif percentage >= 70 : print ("---- > > > Grade C")
elif percentage >= 60 : print ("---- > > > Grade D")
elif percentage >= 50 : print ("---- > > > Grade E")
else : print("You need improvement.")

variable = "Shilpi OP" #str(input("enter a string : "))
string = "Variable %s is a string " %(variable)  
print (string ) 

a = None
if a is None :
    print ("Yes")
else : print("no")

a = [234,45,3526,1454]
print(45 in a)
print(45 not in a )
#else is optional 
num1 = int(input("Enter number 1 : "))
num2= int(input("Enter number 2 : "))
num3 = int(input("Enter number 3 : "))
num4= int(input("Enter number 4 : "))
dict25 = {}
if (num1 > num2): a = num1
else: a = num2
if (num3>num4): b = num3
else : b = num4
if (a>b) : print("-------> Greater  ",a)
else :     print("-------> Greater  ",b)

#pass = gothrough forward of code

 