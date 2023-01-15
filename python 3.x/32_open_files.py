f = open(r'E:\python_beginning\prog_of_py\sample.txt')
data = f.read()
#data = f.read(5) #edit kiya h toh do baar print nhi hoga

print(data)

data = f.readline()
print(data)
f.close()