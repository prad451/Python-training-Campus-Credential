#set
''' 1. Set items are unchangeable(Immutable), and do not allow duplicate values and unordered.
    2. Sets are written with curly brackets.. '''
    
myset = { 2, 2, 3.4,   'tuple',  True ,  ('hi',6.7)}
print(type(myset))

myset2 = {9,54,20}

# Add items to the set
myset.add('abc')
print(myset)

myset.update(myset2)
print(myset)

# Remove Item from the set
myset.remove(2)
print(myset)

myset2.discard(54)
print(myset2)

myset.pop()
print(myset)



st= {10,9,54,9,60,9,5,19,14,15,9}
st.clear()
print(st)