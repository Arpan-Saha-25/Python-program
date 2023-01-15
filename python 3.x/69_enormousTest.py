(n,k) = map(int,input().split(' '))
l=[]
if k<=pow(10,7):
    for i in range(n):
        t=int(input())
        l.append(t)

    count = 0
    for j in range(len(l)):
    
        if l[j]%k==0:
            count= count+1

print(count)
