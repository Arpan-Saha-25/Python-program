#WAP to calculate the factorial of a given 
# number using for loop 

# n! = 1*2*3*.......*n

a = int(input("Enter a number for which we need factorial :"))
factorial = 1
for i in range(1,a+1):
    factorial = factorial * i

print("The factorial of the number ",a," is ",factorial)

