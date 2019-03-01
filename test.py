'''
n = int(input())
c=0
for i in range(n):
	c+=int(input())

print(c)
########
x=[1,2,3]
print(id(x))
print(id([1,2,3]))
#########
x=[1,2,3]
y=x
print(y is x)
print(y is [1,2,3])

#####
x = [1, 2, 3]
y = x
y.append(4)

s = "123"
t = s
t = t + "4"

print(str(x) + " " + s)
print(type(x))
print(type(4))

x=5
print(id(5))
print(id(x))
'''
a = []

def foo(arg1, arg2):
  a.append("foo")

foo(a.append("arg1"), a.append("arg2"))

print(a)