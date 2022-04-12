# Dictionary 
''' 1. Dictionaries are used to store data values in key:value pairs.
    2. A dictionary is a collection which is changeable(mutable) and does not allow duplicate Keys.
    3. Dictionaries are written with curly brackets, and have keys and values.
    4. For keys we can have only non-iterable data types
    5. For values we can have any data type. '''
    

mydict = {1 : 'hello','hello' : 4,3.4 : [2,3,[4,5],(2,3)],'key' : True,'key' : 4,True : {1 : 'word',2 : {3 : 'foo'}}}
print(type(mydict))
print(mydict)

#access a particular element of dictionary
print(mydict[True][2][3])
print(mydict[3.4][2][0])

#Updating values
mydict[3.4]=[5,4]
print(mydict)

mydict.update({"keyss":True})
print(mydict)

# Adding an item to dict
mydict[7] = 85
print(mydict)

# Removing an item from dict

mydict1 = {1 : 'hello','hello' : 4,3.4 : [2,3,[4,5],(2,3)],'key' : 4}
mydict1.popitem()# removes the item that was last inserted into the dictionary
mydict1.pop(1)#removes the specified item from the dictionary
print(mydict1)

mydict1.clear()
print(mydict1)

#del mydict1
#print(mydict1)

# Special Methods
print(type(mydict.keys()))#return type of keys
print(mydict.values())#return values in dictionary
print(mydict.items()) #return items

for i in mydict.items():
    m,n = i
    print(m,n)
    
    

