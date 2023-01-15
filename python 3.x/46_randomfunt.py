import random 
print(random.random())
print(random.randint(0,10))
print(random.uniform(0,10))

file1= open('E:\python_beginning\prog_of_py\poems.txt','r')

'''d1=file1.read()
print(d1)
print("\n")'''

'''d2=file1.read(45)
print(d2)
print("\n")'''

'''d3=file1.readline()
print(d3)
print("\n")'''

d4=file1.readlines()
print(d4)
print("\n")

str= len(d4)
print("Lines present",str)
file1.close()
