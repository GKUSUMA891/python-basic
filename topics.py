#variables:
xyz=10
name=20
print(name)
print(xyz)
print(xyz +30)
print(name+xyz)
x=y=z=100
print(x)
print(y)
print(z)
m,n,o=200,300,400
print(m)
print(n)
print(o)
x="apple"
print("sweetest fruit is:" +x)
print("sweetest fruit is:",x)
name1="thunder"
name2="soft"
print(name1+name2)
print(name1 *3)

'''x=20
y="children"
print(x+y)'''#string+int gives error

#my Name="string" #camel
#My Name1="python"  #pascal
#print(my Name)
#print(My Name1)
#print("hello world",python)
     

Name=["kavya","thunder","soft"]
x,y,z=Name
#a,b,c="venki"
print(x,y,z)
print(x)
print(y)
'''print(z)
print(a)
print(b)
print(c)'''
#def function
a="thunder"
def add():
    print("working company is:",a)
add()
print("hello world","python")
#print("hello world",python)

#if condition
a=30
age=60
if age>a:
    print("major:",age)
else:
    print("minor:",age)
'''#user inputs
print("enter first element")
x=int(input())
print("enter second element")
y=int(input())
if(x==y):
     print("both are equal")
else:
    print("both are not equal")'''

#sum
a=30
b=40
sum=a+b
print(sum)
'''#local var:
x=80
def add():
    global g
    g=90
    print("age is:",g)
    add()'''

l,m,n,o=10,20.3,"thunder","trust"
print(l,m,n,o)
print(l)
print(m)
print(n)
print(o)
print(id(l))#id
print(id(m))
print(id(n))
print(id(o))
print(type(l))#type
print(type(m))
print(type(n))
print(type(o))
print(tuple(n))
print(list(n))
print(set(n))
#swapping with temp
abc=900
xyz=680
temp=abc
abc=xyz
xyz=temp
print(abc)
print(xyz)
#global
def m1():
    a=30
    print(a)
    return
def m2():
    print(a)
    return
m1()
m2()
#global var 1:
'''def m1():
    a1=30
    print(a1)
    return
def m2():
    a1=50
print(a1)
m1()
m2()'''
def a1():
    xyz=20
    print(xyz)
    return
def a2(xyz):
    print(xyz)
    return
a1()
a2(567)


maxi=123
maxi1=123
if(maxi and maxi1):
  print("maxi and maxi1 are equal")
else:
  print("maxi and maxi1 are not equal")

b1="venki"
b2="gal"
b3=["kushi","prema","manu","deekshi"]
if(b1 in b3):
    print("b1 present in list b3")
else:
    print("b1 not present in list b3")
if(b2 not in b3):
    print("b2 not present in list b3")
else:
    print("b2  present in list b3")
#operators
a=20
b=70
c=57
d=35
e=0
e=(a+b)*c/d
print(e)

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)

if(a==b):
    print("a is equal to b")
else:
    print("a is not equal to b")
if(a!=b):
    print("a is not equal to b")
else:
     print("a is equal to b")
a=12
while a>0:
  print("a is:",a)
  a=a-2
#list
list=[]
print(list) #empty[]
list1=[1,2,3,4,5]#number[]

print(list1)
list2=[1,2,"string",3,4.5,5]#mixed[]
print(list2)

list3=[1.3,2.5,3.50,4.79,5.78]  #float[]
print(list3)
#print(delete(list3))

a=["list1","mango","trust","apple",10,20,30,40]
a.append("python")
print(a)
a.remove(a[5])
print(a)
a.insert(5,"hi all")
print(a)
a.pop(1)
print(a)
a=[12,34,56,]
a.clear()
print(a)
a=[10,20,30,40,"hello",4.5]
a.index(40)
print(a)
a12=[10,20,30,40,50,60]
max(a12)
print(max(a12))
print(min(a12))
print(len(a12))
print(a12.index(40))
print(a12.index(60))


name1="kuswumagowda"
print(name1[1])   #index
for i in name1:
    print(i)
name1.capitalize() #Kusumagowda

string="hi {},good {}"
str=string.format("all","evening")#format

a=[1,2,"string",3,4.5,5]
b="mango"
print(id(a))
print(id(b))
print(id(a)+id(b))
print(tuple())
print(tuple(a))

print(len(a))
print(len(b))

a.append(123)
tuple1=[10,20,30]
tuple2=["thunder","soft","logic"]
print(tuple1)
print(tuple2)

s={"mango","venki","prema","chaithra"}
"mango" in s    
print(s)         
"kusuma" not in s  
print(s)             
st1={10,20,30,"mango","venki",(1,2,3),"prema","chaithra"}      #len()
print(len(st1))
c1={10,20,30,40,60,70}
#max(c1)
print(max(c1))  #max()
print(min(c1))   #min()
print(len(c1))   #len()
#print(sum(c1))   #sum()




