print("  ----------------------------------------------------------------------------")
maths = int(input(" \n Enter marks obtained in maths : "))
eng =    int(input(" \n Enter marks obtained in eng : "))
science = int(input(" \n Enter marks obtained in science : "))
sum_of_marks = maths+eng+science
print("----------------------------------------------------------------------------")
print("total marks obtained =",sum_of_marks," / 300 "  )
perc= (sum_of_marks/300 ) * 100
print("----------------------------------------------------------------------------")
if(maths<33 or eng<33 or science<33):
    print("You are failed in one subject.")
elif (perc >= 41): print("you are pass.")
else : print("YOU ARE FAIL.")
print("----------------------------------------------------------------------------")




