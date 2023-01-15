''' Loop is a things that repeats itself.
It has two types : for loop and while loop'''
i = 1
while i <= 100 :
    print(i)
    i += 1
print("\n")

fruits = ['banana','apple','mango']
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1
print("\n")

for ch in fruits: print(ch)
print("\n")
for i in range(8):
    print(i)
print("\n")
for i in range(1,8,2):print(i)

print("\n")

for i in range(10):
    if i == 5:
        continue
        #print(i)
    print(i)


