print("Hello world \n ")
dict_1={ "as":"जैसा","I":"मैं","his":"उसके","with":"साथ","abrogate":"रद्द","some":"कुछ"}
a = 1
while a in range(1,4) :
    #while a in range(1,4) : 
    a = int(input("Enter 1 for keys ,2 for values , 3 for all \n "))
    if a == 1 :
        print("\n ", dict_1.keys())
    elif a == 2 :
        print("\n ",dict_1.values())
    elif a == 3 : print(dict_1)
    else :
        print("------------ Out of range ----------")
        break
    b = input(" \n \t Do u want to continue Y or N \t ")
    
    if b == "Y" or b == "y" :
        print()
    
    else : 
        break