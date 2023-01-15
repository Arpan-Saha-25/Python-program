a = {1,2,3,4,5,6,7}
print(a)
print(type(a))

#printing a null set(expected)
b={}
print(type(b))

#printing a null set(reality)
c= set()
print(c)
print(type(c))

#adding values to empty set 
c.add(12)
c.add(13)
c.add(14)
c.add(15)
c.add(12)
print(c)

# c.add([1,2,3,4])        #you cannot add a dict/list to a set
c.add(  (1,2,3,4)   )   #you can add a tuple to a set as it is immutable 
print(c)

print(len(c))
c.remove(15)
print(c)
