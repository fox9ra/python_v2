#ex 1.5.1 копилка

class MoneyBox:
	def __init__(self, capacity=0, val=0):
		self.capacity = capacity
		self.val = val

	def can_add(self, v):
		if self.val + v > self.capacity:
			return False
		else:
			return True

	def add(self, v):
		if MoneyBox.can_add(self,v) == True: #проверка что можно добавить монетки
			self.val += v
			return True
		

	def print_val(self):
		print(self.val, self.capacity)

x = MoneyBox(15)
x.add(5)
x.add(9)
x.add(3)
x.print_val()


'''
#good from stepik
class MoneyBox:
    def __init__(self, capacity):
        self.count_coin = 0
        self.capacity = capacity

    def can_add(self, v):
        return self.count_coin + v <= self.capacity

    def add(self, v):
        if self.can_add(v):
            self.count_coin += v
'''