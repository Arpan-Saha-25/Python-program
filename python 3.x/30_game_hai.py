'''
snake ,water ,gun game aka rock,paper,scissor
'''
import random

def gameWin(comp,you):
    if comp==you:
        return None
    elif comp == "s":       #snake
        if you == "w":
            return False
        elif you =="g": 
            return True
    elif comp == "w":       #water
        if you == "g":
            return False
        elif you == "s":
            return True
    elif comp=="g" :         #gun
        if you == "w":
            return False
        elif you == "s":
            return True        
       
print("Comp's turn : snake(s),water (w), gun(g)\n  ")
print("Done. \n ")
#made by invictus venum
#a= int(input("Enter a  character for : \n \t snake(s),water (w), gun(g)\n  =>> "))
randno = random.randint(1,3)
if randno ==1:
    comp = "s"
elif randno == 2 :
    comp = "w"
else: 
    comp = "g"

you = input("Your turn : snake(s),water (w), gun(g)  ")

a = gameWin(comp,you)
#made by invictus venum
print(f"Comp chose {comp} ")
print(f"You chose {you} ")

if a == None : 
    print("The game is tied !!!!")
elif a:
    print("You won !!!")
else : 
    print("You lose !!!")

#made by invictus venum