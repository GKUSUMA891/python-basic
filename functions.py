#function:starts with def keyword,line end with colon.
'''a=20
def text():
    global a
    a=40
    print(a)
    return
text()
text()'''

a=50  #global
def m1():
    global a   #using global keyword
    a=30
    print(a)
    return
def m2(a):       #
    print(a)
    return
m1()     #fun calling
m2(90)
m1()
#GLOBAL VAR 1
a="appa"
def parent():
    print(a+" is my energy booster")
    return
parent()
#GLOBAL VAR 2
x="college"
def fun():
    global y
    y="school"
    print(y+" days are best days")
    fun()
    
#LOCAL VARIABLE 1
def sibling():
    name="prema"
    print(name + " is my sibling")
    return
sibling()
#LOCAL VARIABLE 2
def function():
    a=10
    b=30
    c=a+b
    print(c)
    return
function()
    
    


