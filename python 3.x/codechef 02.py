#  who is taller 
t = int(input())
for i in range(t):
    m=list(map(int,input().split()))
    if m[0]>m[1]:print("A")
    else: print("B")
#My very 1st contest ---codechef
m=list(map(int,input().split()))
print(m[0]-m[1],m[0]-(m[1]+m[2]))

