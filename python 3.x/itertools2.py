from tkinter import N


n = {1,2,3,4,5,6}
n= {0,1,2,3} & n  
print(n)
n = filter(lambda x:x>1,n)
print(list(n))