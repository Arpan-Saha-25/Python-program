maths = int(input("Enter marks in maths : "))
english = int(input("Enter marks in English : "))
phy = int(input("Enter marks in Physics : "))
total = maths + english + phy
per = (total*100)/300
print("percentage === ",per)
if(per>=91 and per<=100):
    print(" grade obtained is : A")
elif(per>=81 and per<=90):
    print(" grade obtained is : B")
elif(per>=71 and per<=80):
    print(" grade obtained is : C")
elif(per>=61 and per<=70):
    print(" grade obtained is : D")
elif(per>100):
    print('******** invalid input ********** ')

else:
    print(" grade obtained is : FAIL ")
