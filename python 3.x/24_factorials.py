def factorial_iter(n):
    product = 1 
    for i in range(1,n):
        product = product * (i) 
    return product

print(factorial_iter(4))
print(factorial_iter(5))
print(factorial_iter(6))
print(factorial_iter(7))
print(factorial_iter(8))

def factorial_recursive(n):
    if n == 1 or n == 0:
        return 1
    else:

        return n*factorial_recursive(n-1)

print("\n" , factorial_recursive(4))