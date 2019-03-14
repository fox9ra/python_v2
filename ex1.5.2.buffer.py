#ex 1.5.2 test class buffer

class Buffer:
	def __init__(self):
		self.buf=[]

	def add(self,*a):
# в цикле добавляем переменные из *a по одному
		for i in a: 
			self.buf.append(i)
#проверяем если длинна стала равна 5 то выводим и очищаем список
			if len(self.buf) == 5:
				print(sum(self.buf[:5]))
				self.buf = []
		
	def get_current_part(self):
		return self.buf


buf = Buffer()
buf.add(1, 2, 3)
buf.get_current_part() # вернуть [1, 2, 3]
buf.add(4, 5, 6) # print(15) – вывод суммы первой пятерки элементов
buf.get_current_part() # вернуть [6]
buf.add(7, 8, 9, 10) # print(40) – вывод суммы второй пятерки элементов
buf.get_current_part() # вернуть []
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1) # print(5), print(5) – вывод сумм третьей и четвертой пятерки
buf.get_current_part() # вернуть [1]

'''
#stepik 
class Buffer:
	def __init__(self):
		self.l=[]
	def add(self, *a):
		self.l.extend(a)
		while len(self.l)>=5:
			print(sum(self.l[:5]))
			del(self.l[:5])
	def get_current_part(self):
		return self.l
'''