file1= open(r'E:\python_beginning\prog_of_py\schoolprog.dat','w')
l1 = []
n = int(input("Enter the no. of entries :"))
for i in range(n):
    data = input("Enter the name roll and marks =")
    data.split(" ")
    l1.append(data)

l1.append(file1)
print(l1)
file1.close()