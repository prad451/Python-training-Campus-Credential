#string functions

a ="Hello Everyone!"
b = "  I love python"

print(a.upper()) #print string in uppercase 
print(a.lower()) #print string in lowercase
print(a.capitalize()) #convert first letter to uppercase
print(a.islower()) #return true if given string is in lowercase
print(a.isupper()) #return true if given string is in uppercase
print(a.strip()) #remove leading and trailing spaces
print(b.strip())
print(a.replace("el","b")) #replace specific string
print(b.split()) #The split() method splits a string into a list. You can specify the separator, default separator is any whitespace
print(a.split(","))
print(a.count('E'))#return count of specific charactor
print(a.count('e'))
print(a.count('el'))
print(a.count('e',0,6))#return count of specific string in specified range
print(a.find('o')) #return index of first occurance of specific string
print(a.find('o',0,5)) #return index of first occurance of specific string in specified range
print(b.find('o',6,11)) #return -1 if string is not found
print("  Mr.been" == "Mr.been") #true if both string matches exactly(consider space)


#string concatenation
print(a+b)
print(a+","+b)

#escape characters
#x = ""India" is my country" #it give syntax error
x = "'India' is my country"
print(x)
y = "All Indians are \n \t 'brothers' and 'sisters'"
print(y)
z = '''All Indians are \n 
    \t brothers and sisters'''
print(z)




 





