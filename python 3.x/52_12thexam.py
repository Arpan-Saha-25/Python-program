Book={1:'Thriller', 2:'Mystery', 3:'Crime', 4:'Children Stories'}
Library ={'5':'Madras Diaries','6':'Malgudi Days'}
print(Library.update(Book))

Library=Book 
Library.pop(2) 
print(Library) 
print(Book)


Library=Book.copy()
Library.pop(2) 
print(Library) 
print(Book)

list1=[1,2,23,3,3,69,4,7,4,0,5,7,5,5,1,6,6,]
print(list1)
