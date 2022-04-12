                             ###########List#############
'''1.Lists are used to store multiple items in a single variable.
   2.List items are changeable(Mutable), and allow duplicate values.
   3.List items are indexed, the first item has index[0],the second item has index[1] and so on...
   4.Lists are written with square brackets.
   5.List can have any datatype in it.'''

#defination
a=[23,'Poonam','Pradnya',5.6,50]
print(a)
print(type(a))

#Accessing Elements of list
print(a[2])

#Change the element of the list
a[1:4] = [1,2,3,7,[12]]
a[0] ="abc"
a[2:4] = [12,13,14,15,16,[25,26]]
print(a)

#special functions
mylist = [4,5,6,'Pradnya',[456,'Poonam',6.7,['Pradnyam']],34]
print(mylist)
print(type(mylist))
print(mylist[4][3][0])
print(mylist[4][2])

#1.copy() : Returns copy of the list
mylist1 = ['Sanchita','rohini','sanchU','Ruhi']
x = mylist1.copy()
print(x)

#2.reverse() : Reverse the order of the list
mylist.reverse()
print(mylist)

mylist1.sort()
print(mylist1)

mylist1.sort(reverse=True,key=str.lower)
print(mylist1)

#3.count():Returns the number of elements with the specified value
print(mylist.count(6)) 

#4.adding an elements using append
mylist1.append("Poonam")
print(mylist1)

#5.adding an elements using insert
mylist1.insert(0,"Pradnya") #add element at given index
print(mylist1)

#6.adding an elements using extend
mylist1.extend("DYP") #it add given string into list by seperating each character
print(mylist1)

mylist1.extend(mylist) #it concatenate lists
print(mylist1)

#7.removing element from lists
lst = [4,5.6,'hjhd',[456,'sdfkdj',6.7,['type']]]
lst.remove(5.6)
print(lst)

x = lst.pop(1) #it removes value at specified index and returns that value and by default it will remove and returns last value
print(x)

mylst = [4,5,'hello',[34,68,[44,5,'mumbai']]]
del mylst[1] #remove  index specified element and return remaining list
print(mylst)

mylst.clear()#clear the list and return empty list
print(mylst)

#to change the old substring to new substring
ml = [4,5,'hello',[34,68,[44,5,'mumbai']]]
ml[2] = 'Hello'
print(ml[2].replace('hello','Hello'))
print(ml)






