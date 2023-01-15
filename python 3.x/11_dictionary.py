print('''
*****************Welcome to my code*******************
''')
mydict= {"01":"arpan","02":"bee","03":"cat","04":"danger"}

print(mydict)
#to show only keys of dict.
print(mydict.keys())
#to show the type of keys
print(type(mydict.keys()))
#to show only values of dict.
print(mydict.values())

print(mydict.items()) #prints all the (keys,values) of the dictionary in the form of LISTS in tuples

print(mydict)
updatedict = {"05":"elf","06":"fan"}
mydict.update(updatedict)           #updates the dictionary by adding(key,values) pairs
print(mydict)

print(mydict.get("01"))
print(mydict["01"])
''' difference between above two statements '''
print(mydict.get("07"))    #it can help to get values directly but if there is not such key then it returns "none"
print(mydict["07"])        #it can help to get values directly but if there is not such key then it throws an '''error'''

'''other py dict methods : https://docs.python.org/3/tutorial/datastructures.html '''
