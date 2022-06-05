####Function defination(function declaration)#####
'''def function_name(arguments):
       Body/logic
'''
y=10
z=12
def myFunction(y,z):
    return y+z
x=myFunction(y,z)
print(x)

#DocString
#print(myFunction.__doc__)

'''Function Call'''
#t,v = 8,9
#myfunction(t,v) # When function is returning nothing
# x = myfunction(t,v) # When function is returning Some values
# print(x)



'''Arbitrary Arguments, *args ###########'''
'''
1. If you do not know how many arguments that will be passed into your function,
    add a * before the parameter name in the function definition.
2. It will create a tuple of values.    
'''

def addition(t,*numbers):
    sum = 0
    for i in numbers:
        sum += i
    return t, numbers
print(addition(2,3,4,5))


'''Keyword Arguments, **kwargs'''
'''
1. You can also send arguments with the key = value syntax.
2. It will create a dictonary of key-value pairs.
'''

def averageMarks(**marks):
    average = 0
    for i in marks.values():
        average += i
    average = (marks['ravi']+marks['sangeeta']+marks['anmol'])/3
    average /= len(marks)
    print(marks)
    return average
print(averageMarks(ravi=30,sangeeta=78,anmol=80))



'''Passing list or other datatype as an input'''
ls = [2,3,4,5]
MyTuple = (3,4,0)

def MyFunction(ls,mytuple):
    for i in ls:
        print(i)
    for i in MyTuple:
        if i>2:
            print(i)
MyFunction(ls,MyTuple)



'''Scope (Local and Global Variables)'''
'''Local Variables : are those which are defined inside a function and its scope is limited to that function only.
                     It cannot be accessed anywhere outside the function. '''
                     
def myfunction():
    s="This is local variable"
    print(s)
myfunction()

def myfunction():   #will give error as "NameError: name 's' is not defined" because i have use local variable outside the function
    s="This is local variable"
myfunction()
print(s)

'''Global variables : are those which are defined outside any function and 
                      which are accessible throughout the program i.e. inside and outside of every function'''

def myFun():
    print("Inside the Function", s)
# Global scope
s = "This is global variable"
myFun()
print("Outside the Function", s)


def myfun():
    print("This is global variable")
s=20
print(f"I had {s} rupees")
myfun()
def another():
    print(f"I have {s} rupees")
another()
print(f"I am currently having {s} rupees")


'''We only need to use the global keyword in a function if we want to do assignments or change the global variable.
   global is not needed for printing and accessing.'''
   
a = 1
# Uses global because there is no local 'a'
def f():
    print('Inside f() : ', a)
 
# Variable 'a' is redefined as a local
def g():
    a = 2
    print('Inside g() : ', a)
 
# Uses global keyword to modify global 'a'
def h():
    global a
    a = 3
    print('Inside h() : ', a)
 
 
# Global scope
print('global : ', a)
f()
print('global : ', a)
g()
print('global : ', a)
h()
print('global : ', a)


