#type coversion in python
# int, float , str ,bool, list ,tuple, dict , set
x = 45
print(type(x))

a = float(45)
print(type(a))

b = bool(1)
print(b)

c = str(10.32)
print(c)
print(type(c))

#list to tuple coversion
l = [2,5.6,'hh',[3,4],(4,5)]

t = tuple(l)
print(type(t))
print(t)

#tuple to list
tuple = (1,2,[3,'jk'],1+2j,45.05)
list1 = list(tuple)
print(type(list1))
print(list1)

mytuple = (3.4,2,  2, 3.4,3.4,   'tuple',  True ,  ('hi',6.7) )
mylist =  [3.4,2,  2, 3.4,3.4,   'tuple',  True ,  ('hi',6.7) ]
#list to set conversion
myset = set(mylist)
print(myset)
#tuple to set conversion
st = set(mytuple)
print(st)
#set to list
sl = list(st)
print(sl)



