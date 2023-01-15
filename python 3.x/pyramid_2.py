b=int(input("Enter A number : "))
for i in range(b,-1,-1):
    for j in range(b,i,-1):
        print(j,end=" ")
    print("\n")