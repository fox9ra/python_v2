#ex 1.5.2 test class buffer

class Buffer:
	def __init__(self, buf=[]):
		self.buf=buf

	def add(self,*a):
		self.buf.extend(a)
		
	def get_current_part(self):
		print(self.buf)


buf = Buffer()
buf.add(1, 2, 3)
buf.get_current_part()
buf.add(4, 5, 6)
buf.get_current_part()