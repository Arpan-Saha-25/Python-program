''' MAking A fizzbuzz program '''
n = int(input())
l = []
for i in range(n):
    l.append(i+1)
    print(i+1)
    

#print("l = " ,l)
for j in range(n) :
    if l[j]%3 ==0: print("Solo")
    elif l[j]% 5==0:print("Learn")
    else: continue

