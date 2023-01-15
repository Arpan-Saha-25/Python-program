text = "subscribe to my channel "  #input("Enter the text = ")
print (" Your text is ", text)

spam = False

if ("make a lot of money" in text ):
    spam = True
elif("buy now" in text) :
    spam = True
elif("click " in text) :
    spam = True
elif("subscribe" in text) :
    spam = True
else : spam = False

if(spam):
    print("this text is spam")
else : print("This text is not spam.")

#wap to check whether the string contains 
# atleast 10 characters ???

name = 'Arpan Saha'
b = name.replace(" ",'')
a = len(name)
if a < 10 : print("THe string contains less than 10 characters")
else : print( " String contains atleast 10 char.s")

names=["rohit",'shubham' , 'harry' , 'krishna']
name = str(input("Enter the name = "))
if name in names: print("Your name is persent in the list")
else : print("your name is not in the list.")

