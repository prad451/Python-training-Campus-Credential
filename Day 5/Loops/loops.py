####loops####
#for loop:
'''for variable in range(startValue,endValue,incrementAmount):
     statement '''
## Assign the value to the variable
## Check the condition - (variable value is strictly less than end value)
## Execute whatever present in for loop
## Increment the value by whatever defined in for loop
## The condition in for loop is  "<" ,,, not <=



'''1. One parameter '''
## Default value :  start value == 0 and increment value == 1
for i in range(5):
    if i == 2:
      break
    print(i)

'''2. Two parameter '''
## Default value : increment value == 1
for i in range(3,6): 
   print(i)
   


'''1. One parameter '''
## Default value :  start value == 0 and increment value == 1
# for i in range(5):
#     # if i == 2:
#     #     break
#     print(i)

'''2. Two parameter '''
## Default value : increment value == 1
for i in range(1,50,5): 
   print(i)
   

#While Loop 
''' 
Initialize variable 
whilw Check the condition 
if true: 
    then go to while loop 
    increment the variable
'''

i = 0
while i < 4:
    print(i)
    i = i + 1


#break
i = 0
while i < 4:
    if i == 2:
      break
    print(i)
    i = i + 1

#continue
for i in range(9):
    print(i)
    if i == 3 or i ==7:
      continue
    