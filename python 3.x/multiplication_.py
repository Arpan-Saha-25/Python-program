#multiplication tables 

j=1
m=int(input("Enter the number upto you want tables:"))
for i in range(1,m+1):
    for k in range(1,11):
        a = i * k
        print(i,"*",k,"=",a)
    print(" \n \n ")
