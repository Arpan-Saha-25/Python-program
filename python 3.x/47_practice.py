'''file1 = open(r'E:\python_beginning\prog_of_py\students.txt','w')
for i in range(5):
    name= input("Enter the std name = ")
    file1.write(name)
    file1.write("\n")
file1.close()
'''
file2 = open(r"E:\python_beginning\prog_of_py\students_name.txt","w")
n = int(input("Enter the no. of students ="))
for i in range(n):
    name = input("Enter the name = ")
    file2.write(name)
    file2.write("\n")

file2.close()