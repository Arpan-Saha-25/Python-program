content= True
i = 0
with open("E:\python_beginning\prog_of_py\logtry.txt","r") as f:
    
    while content :
        i+=1
        content = f.readline()

        if "python" in content.lower() :
            print(content)
            print("Yes, it is present")
            print("-->> line : ",i)    
