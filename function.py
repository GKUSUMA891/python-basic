#FUN FORMAT()
#EXAMPLE:

a="i'm working in {fcompany},i'm a{fname}.".format(fcompany="thundersoft",fname="fresher")
b="my first company is {0},it is {1}.".format("thundersoft","awsome")
c="i'm working in {},i'm a{}.".format("thundersoft","fresher")
print(a)
print(b)
print(c)

#TYPE():
a=100
print(type(a),a)
b=12.5
print(b)
print(type(b))
c=complex(2,8)
print(c)
print(type(c))
c=(2,8)
print(c)
print(type(c))
#TYPE CASTING:
'''d=20
float(d)
e=34.6
int(e)
print(int(e))'''

#ID FUN():gives memory location/address of the value
x=10
y=8+2
z=12-2
v=2*5
w=7+3
print(x)
print(id(x))
print(id(y))
print(id(z))
print(id(x)-id(y))
print(id(v))
print(id(w))
m="mango"
print(m)
print(id(m))
