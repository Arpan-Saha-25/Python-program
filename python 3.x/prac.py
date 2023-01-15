#a1= int(input("================ \n enter the numbers :- \n 1. "))
#a2= int(input(" \n 2. "))
#a3= int(input(" \n 3. "))
#a4= int(input(" \n 4. "))
#a5= int(input(" \n 5. "))

#s= {a1,a2,a3,a4,a5}

#print(" \n Unique numbers are : " , s )

a ={113,"113"} 
print("\n",a)

s = { 20,20.0,'20'}
print(s)
print(len(s))

favlang={}
y = input("enter your fav. lang. sumit= \n")
q = input("enter your fav. lang. sourav= \n ")
w = input("enter your fav. lang. suraj= \n ")
r = input("enter your fav. lang. nageshwar= \n ")
t = input("enter your fav. lang. Arpan= \n ")

favlang["Sumit"] = y
favlang["Sourav"] =q
favlang["Suraj"] =w
favlang["nageshwar"] =r
favlang["Arpan"] =t

print(favlang.keys())
print(favlang.values())