'''
def h():
    print("- H")
    print("- 12")
    print("H - end")

def f():
    print("- F")
    g(h)
    print("F - end")

def g(a):
    print("- G - ",a)
    a()
    print("G - end")

print("\nMODULE")
g(f)
'''
def s(a, *vs, b=10):
   res = a + b
   for v in vs:
       res += v
   return res
print(s(0, 0, 31))
print(s(11, 10))
print(s(11, 10, b=10))
print(s(21))
print(s(11, b=20))
print(s(b=31))
print(s(11, 10, 10))
print(s(5, 5, 5, 5, 1))
