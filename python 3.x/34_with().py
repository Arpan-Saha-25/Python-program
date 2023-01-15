# TIMESTAMP : 7:25:50

'''isme open krne ke baad 
    close krne ki zarurat 
    nhi hoti'''
    
with open('another.txt','r') as f:
    a=f.read()

with open('another.txt','w') as f:
    a=f.write(" Ye wala print hoga !!!! ")

print(a)