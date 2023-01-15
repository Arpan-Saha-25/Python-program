i = input("Enter comment : ")

keys = set(["spam","money","subscribe","like","comment","share","$","win","pray",])
censored = set(["nigga","noob","nulla","palty"])

if i in keys: 
    print (i)
    print(" ******************* This is a SPAM COMMENT. *******************")

else : print(" ✌✌✌ALL GOOD comments  ")
