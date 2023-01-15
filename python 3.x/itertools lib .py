from itertools import count,takewhile 
#for i in count(3):
#    print(i)
#    if i>=11:
#        break
    
print("--------------------")

num=[1,2,4,6,7,8,9]
m=takewhile(lambda x:x%2==0 ,num)
print(list(m))