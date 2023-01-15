result = {"a":240, "b" : 140 ,"c":350,"d":250,"e":370}
li_std = list(result.keys())
li_re= list(result.values())
#print(li_re)
#[240, 140, 350, 280, 370]
for i in li_re:
    if i>=250:
        k=li_re.index(i)
        print("tum pass ho gaye")
        print(li_std[k]," has greater than 250 marks, ",)


            
        


        