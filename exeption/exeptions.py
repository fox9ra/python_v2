'''
#test2
print("This line is executed")

class EvenLengthMixin:
	def even_length(self):
		return len(self) % 2 ==0

class MyList(list, EvenLengthMixin):
	pass

ml = MyList([1,'abc',12,4,17,3])
ml.sort()
print(ml)
'''

'''
try:
	x = [1,2,"hello",7]
	x.sort()
	print(x)
except TypeError:
	print("I have Error")

print("YYY")
'''

def divide(x, y):
	try:
		result = x / y
	except ZeroDivisionError:
		print("division by Error")
	else:
		print("result is", result)
	finally:
		print("finally")

divide(2,1)
#result is 2.0
#finally
divide(2,0)
#division by Error
#finally
divide(2,[])
#finaly 
#Traceback...
