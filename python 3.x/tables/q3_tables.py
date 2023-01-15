n = int(input("enter range starting from :"))
m = int(input("enter range ending from :"))

for i in range(n,m+1):
    with open(f"E:\\python_beginning\\prog_of_py\\tables\\multiplication_tables_{i}.txt",'w') as f:
        for j in range(1,11):
            f.write(f"{i}x{j} ={i*j}")
            if j!= 10 : 
                f.write("\n")

print("Done")