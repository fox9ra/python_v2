class Counter:
	def __init__(self):  # обнуление функцией __init__
		self.count = 0

	def inc(self):
		self.count += 1

	def reset(self):
		self.count = 0

Counter #class object
x = Counter() #создание конструктора класса
x.inc()
print(x.count)
Counter.inc(x) # равносильно вызову x.inc()
print(x.count)
x.reset()
print(x.count)