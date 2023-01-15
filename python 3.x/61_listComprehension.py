'''
Objective : WAP to take a number as input, and output a list of all those numbers
below that number , that are a multiple of both  3 and 5. 
'''

x = int(input("enter no. : "))
l = []
for i in range(x):
	if i%3==0 and i%5==0:
		l.append(i)

print(l)
