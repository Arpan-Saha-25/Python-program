file1 = open(r'E:\python_beginning\prog_of_py\namemarks.dat',"w")
l1 = []
for i in range(2):
    name=input("Enter the name of the student ")
    l1.append(name+'\n')
    
file1.writelines(l1) 
file1.close()

file1 = open(r'E:\python_beginning\prog_of_py\namemarks.dat',"r")
pr=file1.read()
print(pr)
file1.close()