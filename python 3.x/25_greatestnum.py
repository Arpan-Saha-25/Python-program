# timestamp = 6:36 min (continuing)

def greatestnum(num1,num2,num3):
    if(num1>num2):
        if(num1>num3):
            return num1
    else:
        if(num2>num3):
            return num2
        else: return num3
q = int(input("Enter the number 1 =")) 
w = int(input("Enter the number 2 ="))
e = int(input("Enter the number 3 =")) 
f = greatestnum(q,w,e)
print("Greatest number is : ", f)