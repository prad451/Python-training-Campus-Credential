########Operators#######
'''1. Arithmatic Operator '''
# Operator :- + , - , * , / , ** , // , %   :- Binary Operators.
a = 7
b = 5
print(a**7)  
print(a//2) # x = 3.4 floor : 3 and ceil :- 4
print(a/2)
print(a%2)
print(a+b+6+7)
print(a*b+b%a)
print(b/2)
print(b//2)
print(a**b+a-b*a//b%a/b)


'''2. Assignment operators'''
# Assignment operator :- = , += , -= , *= , /= , **= , //=
x = 6 
x += 4 # x = x +4 = 6+4 = 10
print(x)
x *= 2 # x = x * 2
print(x)
x **=2
print(x)
x //=4
print(x)



'''3. Bitwise operator'''
# Bitwise Operator :- & ,  | , << , >> , ^ , ~
# 5 = 101

# 64 32 16 8 4 2 1  


print(5 | 7)
# 101             =   4 +  0 + 1 =   5  =   4 + 1   = 101
# |
# 111              = 4 + 2 + 1 = 7
# ----
# 111 = 7     

print(4 & 7)
# 100             =   4 +  0 + 1 =   5  =   4 + 1   = 101
# &
# 111              = 4 + 2 + 1 = 7
# ----
# 100 = 4   

a = 5   # ==  101 
# Right Shift 0000 0101 = 0000 0010 =  0000 00001 = 0+ 0 + 1 = 1
a >>= 2
print(a)

#Left Shift  0000 0101  = 0000 1010 = 0001 0100 = 20
a <<= 2  #  1010
print(a)

#XOR:- odd :- 1 and even :- 0 
t = 5
v = 7
c = t ^ v 
# 101             =   4 +  0 + 1 =   5  =   4 + 1   = 101
# ^
# 111              = 4 + 2 + 1 = 7
# ----
# 010 = 2
print(c)


'''Comparison Operators''' 
## Comparison Operators :- == ,!=, < , > , <= , >= 
a = 4
print(a == 4)
print(a!= 4)
print(a > 6)   # 4 > 6 = False
print(a < 6)   # 4 < 6 = True , 4 < 4 = False
print(a <= 4)  # 4<= 4 = True
print(a >= 4)  # 4 >= 4 = True


'''Logical Operators'''
# Logical Operators :  and, or , not
# True = 1 and False = 0 
print(4 < 5 and 5 > 6)  ## If either one of the condition is false the output will be False else True
print(4 < 5 or 5 > 6)   ## Either one of the condtion shoud be true.
print(not(4 < 5 or 5 > 6))


'''Identity Operators'''
# Identity Operators : is , is not
mystring = 'hello'
m = "hello"
print(mystring is m)
print(mystring is not m)

c = 8888
d = c
h = 'e'
e = 8888
f= 8888
print(id(c),id(d),id(e),id(f))
print(c == e)
print(c is e)
print(c == d)
print(c is d)
c = 8888
c = 8880
print(c)
print(d)
print(id(c),id(d),id(e))
print(c == e)
print(c is e)
print(c == d)
print(c is d)
print('ee' is 'e' * 2)



'''Membership Operators'''
#Membership Operators : in , not in
m = "hello"
print('hellt' not in m)

lst = [4,'yu',6.7,[34]]
for i in lst:
    print(i)

if 4 in lst:
    print('present')




'''Space analysis of datatypes'''

a = [1,2,3]
print(a.__sizeof__())

b = '123'
print(b.__sizeof__())

c = (1,2,4)
print(c.__sizeof__())

d = {1,2,3}
print(d.__sizeof__())

e = 123
print(e.__sizeof__())

f = {1:1,2:2,3:3}
print(f.__sizeof__())

    