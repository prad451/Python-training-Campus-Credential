#Python string

#single line string
s1 = "india"
print(type(s1),s1)

#multiline string
s2 = '''Python is high level programming language
        Guido van Rossum is a creator of python'''
        
print(type(s2),s2)

#accessing single element in a string
print(s1[2])

#print length of string
#while printing lenth of string it will gives length by including spaces
print(len(s1))
print(len(s2))

#string slicing
s1 = 'india'
print(s1[0:5])
print(s1[:])
print(s1[2:])
print(s1[5:7]) #index is out of range
print(s1[-4:-1])


