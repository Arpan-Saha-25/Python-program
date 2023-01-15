#write operation
no=int(input("Enter how many students in the class"))
file1=open(r'E:\python_beginning\prog_of_py\namemarks1.dat' , "w")
for i in range(no):
    
    roll=int(input("enter roll no :"))
    name=input("enter name :")
    mark=int(input("enter marks :"))
    rec=str(roll)+","+name+","+str(mark)+'\n'
    file1.write(rec)
file1.close()
#reading operation
file1=open(r'E:\python_beginning\prog_of_py\namemarks1.dat' , "r")
str1=file1.read()
print("the class records are \n")
print(str1)
file1.close()
