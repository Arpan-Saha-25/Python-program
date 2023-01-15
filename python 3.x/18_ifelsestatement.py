marks = 69#int(input("Enter the marks \n"))
print("Your marks is 69.")
if marks >=90:
    grade= "EX"
elif marks >=80:
    grade= "A"
elif marks >=70:
    grade= "b"
elif marks >=60:
    grade= "c"
elif marks >=50:
    grade= "d"
elif marks <50:
    grade= "Fail"
else : print("''RESULT NOT FOUND'")
print(grade)

text = str(input("Enter the text :    \t "))
t1=text.lower()
print (" Your text is %s" %t1)
ch = "arpan"
if ch in t1 : print("YES , it contains ur name.")
else : print("Your name is not present")

