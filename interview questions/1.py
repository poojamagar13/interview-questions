list1=[10,20,30,40,50]
list1.reverse()
print(list1)


l2=[10,20,30,40,50,60]
l3=l2[::-1]
print(l3)


l4=[10,20,30]
l5=list(reversed(l4)) 
print(l5)

l1=[]
list2=[1,2,3,4]
for i in range(len(list2)-1,-1,-1):
    l1.append(list2[i])
print(l1)   


import re

def isvalidEmail(email) :
    regex="^[A-Z0-9.%+-]+@[A-Z0-9]+\.[A-Z]{2,}$"
    if len(email)>7:
        if re.match(regex,email,re.IGNORECASE) is not None:
            return True
if isvalidEmail("poojawagh@gmail.com"):
    print("valid Email Address")
else:
    print("invalid Email Address")    
    
    
def isvalidEmail(email) :
    regex="^[A-Z0-9.%+-]+@[A-Z0-9]+\.[A-Z]{2,}$"
    if len(email)>7:
        if re.match(regex,email,re.IGNORECASE) is not None:
            return True
if isvalidEmail("poojawaghgmail.com"):
    print("valid Email Address")
else:
    print("invalid Email Address")    
    
h="hi pooja"    
print(h)
        