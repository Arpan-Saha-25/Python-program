
T = int(input())
l=[]
for i in range(T) :
    str=input()
    A= int(str.split()[0])
    B=int(str.split()[1])
    sum = A+B
    l.append(sum)
    
for i in l:
    print(i)
''' 
    
#new 
T = int(input())
for i in range(T):
    A,B = map(int,input().split(' '))
    ans = A +B
    print(ans)
    '''