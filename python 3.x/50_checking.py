#write opearation
file1=open(r'E:\python_beginning\prog_of_py\namemarks1.dat' , "w")
list1=[]
for i in range(5):
 name=input("enter name of student :")
 list1.append(name+'\n')
file1.writelines(list1)
file1.close()
#reading operation
file1=open(r'E:\python_beginning\prog_of_py\namemarks1.dat' , "r")
str1=file1.read()
print("the data present in the file is \n")
print(str1)
file1.close()
