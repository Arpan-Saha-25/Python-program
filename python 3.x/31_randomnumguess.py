'''
▓ Number guessing Game ▓
'''
import random
b=random.randint(2,99)

print("______Total chances to give correct answer is '6'______ \n ")

for i in range(1,7):
    a=int(input("Enter the chosen number (b/w 1 to 100) = "))
    if a==b:
        print("kangraculations !!!! You guessed right .")
        break
    elif a<b:
        if i==6 :
            print("You lost (⌣́_⌣̀) ") 
            print("The correct number was ",b)
            break
        print("Enter a greater number !!! ")
    elif a>b:
        if i==6 :
            print("You lost (⌣́_⌣̀) ") 
            print("The correct number was ",b) 
            break
        print("Enter a smaller number !!")

