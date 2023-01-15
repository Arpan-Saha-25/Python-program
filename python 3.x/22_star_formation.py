''' printing star formation '''

n =4
for i in range(4):
    print("*" * (i+1))

print("\n \t ")

for j in range(4,0 ,-1):
    print("*" * (j))


# Q.2
'''
print the following pattern : 
   *
  ***
 *****
'''
n = 3
for i in range(3):
    print(" " * (n-i-1),end ="")
    print("x" * (2*i+1),end="")
    print(" " * (n-i-1))


n = 3
print("*" * 3 , end ="")
print("*    *",end="")
print("*" * 3 , end ="")


