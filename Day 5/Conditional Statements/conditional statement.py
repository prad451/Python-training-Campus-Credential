####conditional statements#####
##1.if-else

'''
if condition:
   statement
else:
   statement
'''

a=input("Enter first number : ")
print(a)
b=input("Enter second number : ")
print(b)

if a>b:
    print("a is greater than b")
else:
    print("b is greater than a")
    
##2.elif:else-if

'''
if condition:
    statement
elif:
    statement
else:
    statement
'''

marks=100

if marks==100:
    print("Student got out of marks!!")
elif marks>75:
    print("Student passed with distinction!!")
elif marks>65:
    print("Student passes with first class!!")
elif marks>55:
    print("Student passed with second class!!")
elif marks>35:
    print("Student passed with third class!!")
else:
    print("Student is failed!!")
    

