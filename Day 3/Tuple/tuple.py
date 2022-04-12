
########### Tuple ##################
''' 1. Tuples are used to store multiple items in a single variable.
    2. Tuple items are unchangeable(Immutable), and allow duplicate values.
    3. Tuples are written with round brackets. '''

mytuple = (2,5.6,'hh',[3,4],(4,5))
print(type(mytuple))

# Unpacking

i,*j,t,m = mytuple
print(i,j,t,m)

#adding an element into Tuples
mytuple2 = ('wagh',) #declare single element tuple
print(mytuple2)
print(mytuple+mytuple2)

x = list(mytuple)
x.append(20)
mytuple = x
print(mytuple)

print(mytuple.count(2))#Returns the number of times a specified value occurs in a tuple

print(mytuple.index('hh'))#Searches the tuple for a specified value and returns the position of where it was found
