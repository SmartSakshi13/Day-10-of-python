class counter:
	def __init__(self,max):
		self.max = max
		self.current = 0
	
	def __iter__(self):
		return self
	def __next__(self):
		if self.current >= self.max:
			raise stopIteration
		self.current += 1
		return self.current

for i in counter(5):
	print(i)
