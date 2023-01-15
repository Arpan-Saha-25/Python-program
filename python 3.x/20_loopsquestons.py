i = 45 #int(input("Enter the number : "))
print("number is " , i)
#j =0
print("Multiplication Table of " , i)
for j in range(1,11):

    print(str(i)+ "  *  " + str(j) + " = ",i * j)
    j = j+1

print("\n")
#  question 2

a = 441#int(input("Enter a number :  "))
print("Number = ", a )
#for ch in range(1,10):
if a % 2 == 0 :
    print("No. this number is not a prime number")
else: 
    print("yes , it is a prime number.")

prime = True
for i in range(2,a): 
    if a%i == 0:
        prime = False
        break

if prime==True: 
    print ("Yes, it is a prime number")
else:
    print("It is not a prime number.")

#q5 : sum of n natural no.

n = int(input(" \n Enter a number to print n natural no.s: "))
sum2=0
while n>0:
   sum2 = sum2 +  n
   n-=1
print(sum2)
