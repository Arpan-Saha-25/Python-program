# using loop 
i = int(input("Enter the number : "))
n1= 0
n2= 1
sum = 0
if i<1:print("Please enter a natural number.")
else:
    for j in range(i):
        print(sum,end=" ")
        n1 = n2
        n2= sum
        sum = n1+n2

print("\n -----------------------------------------------")       
#using recursion 
def fibo(n):
    if n==0: return 0
    if n==1: return 1
    else :
        return(fibo(n-1)+fibo(n-2))
    
#i = int(input("enter nth term :"))
for j in range(i):
    print(fibo(j),end=" ")

