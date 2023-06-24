# import os 


# if(not os.path.exists("data")):
#     os.mkdir("data")
    
# for i in range(0,101):
#     os.mkdir(f"data/day{i+1}")
  
f=open('1.py','r') 
text=f.read()
print(text)
f.close()


t=("pooja",'govind','magar')
p=list(t)
p[2]="wagh"
t=tuple(p)
print(t)


i=1
while i<=100:
    print("wagh")
    i=i+1
    
    
i=1
while i<=10:
    print(6,'*',i,'=',6*i)
    i+=1    
    
print(list(range(2,11,2)))

name="pooja"
for  var in name:
    print(var)
    
for val in range(1,20):
    print(val)
    
l=[1,2,3,4,5]
for var in (l):
    print(var+1)    
    
    
l1=[10,20,30]
l2=[40,50,60]
for x in l1:
    for y in l2:
        print(x,y)
        
        
        
# name=int=(input("enter the name"))
# for char in name:
#     if char=='j':
#         break
#     print(char,end="")
    
#concatenation
str1="hi pooja"
str2=" what are you doing"
str3=(str1+str2)
print(str3)    


str4= "pooja"
print(str4)
# del str4   #delete
# print(str4)    



l=[2,2,3,3,3,3,4,5,6,2,3,3,3]
l1=l.count(2)
print(l1)



s="poojawagh"
print(list(enumerate(s)))

# name=input("enter string")
# print("orginal string is:",name)
# r_name=""
# count=len(name)
# while count>0:
#     r_name=r_name+name[count-1]
#     count=count-1
# print('reversed string is:',r_name)    


name=("my name is pooja")
print("reversed string is:",name)
r_name=""
count=len(name)    #len of string
while count>0:
    r_name=r_name+name[count-1]    # orginal string last count concatenate
    count=count-1    # second last count use  decrement
print("reversed string is:" ,r_name)    



str=("python is awesome langauage")
print("reverse string is:",str)
s_name=""
for char in str:
    s_name=char+s_name
print("reverse string is:",s_name)    



l=['p','y','t','h','o','n']
s=''.join(l)
print(s)


name=("poojawgh")
name1=("poojawagh")
print(name>name1)
print(ord('a'),ord('g'))

# while True:
#     num1=int(input("enter first number"))
#     num2=int(input('enter second number'))
#     print("1.Addition\n2.Substraction\n3.multiplication\n4.divison")
#     choice=int(input("choose from above"))
#     if choice==1:
#         print("addition is:",num1+num2)
#     elif choice==2:
#         print("substraction is :",num1-num2)     
#     elif choice==3:
#         print("multiplication is:",num1*num2)
#     elif choice==4:
#         print("division is:",num1/num2)    
        
#     else:
#         print("invalid choice")
#     ans=input("do you want to continue?(y/n):")
#     ans=ans.lower()
#     if ans!="y":
#         break
         
l1=[10,20,30,"pooja",2,3]
print(l1*3)      

l1=[10,20,30,"pooja",2,3]
for i in l1:
    print(i)
    
    
l=["pooja","wagh","magar"]
l.insert(2,"govind")    
print(l)



l=[100,200,230,130,2330,12]
l1=l[0]
for i in l:
    if i>l1:
        l1=i
print(l1)        


t=(10,20,3)
print(t*3)

data=(100,200,(1,2,3),300)
print(data[2][2])

t1=(10,20,30)
t2=(100,)
print(t1+t2)
        
 
s=set([10,20,40,'pooja',4.5])
print(s)   

a={10,20,10,30,40,10,30}
b={10,20,30,50,60}
print(a|b)

a={10,20,10,30,40,10,30}
b={10,20,30,50,60}
print(a.union(b))

# import math 
# num=int(input("enter a number"))
# fact=math.factorial(num)
# print(f"factorial of {num} is {fact}")


# num=int(input("enter a number "))
# result=1
# for i in range(num,0,-1):
#     result=result*i
# print(f"factorial of {num} is {result}")    


d={'name':'pooja','roll ': 101}
print(type(d))
print(d)


stu=dict([('name','pooja'),('roll',123)])
print(stu)
print(type(stu))


t1=(1,2,3)
t2=(4,5)
print(t1+t2)


# s=(input("enter a some string "))
# i=0
# for x in s:
#     print("the character present at positive index{} and at negative index{} is {}".format(i,i-len(s),x))
#     i=i+1


s="govind"
i=1
for x in s:
    print(" the character present at  positive index {} and at negative index{} is {}".format(i,i-len(s),x))
    
a = "Robert Brett Roser"
a = a.split()
b = a[0][0]+". "+a[1][0]+". "+a[2] 
print(b)
   
   
a = ['a','e','i','o','u','A','E','I','O','U',' ']
b = "Hello, have a good day"
for i in b:
  if i not in a:
    b = b[:b.index(i)]+b[b.index(i)+1:]
print(b)       