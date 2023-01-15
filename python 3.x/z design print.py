''' 
how to print in z-design in Python  
12345
   4
  3
 2
12345
'''
i = input("Enter text w/o whitespaces :")
n = len(i)
print(i)
for j in range(n):
    if n==len(i): 
        pass
    if n==1: 
        print(i)
        break
    else:
        print(" "*(n-1),end="")
        print(i[n-1],end='\n')
    
    n = n-1