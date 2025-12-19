# build a custom iterable -  RangeIterator(start,end)

class RangeIterator:
	def __init__(self,start,end):
		self.start = start
		self.end = end

	def __iter__(self):
		self.current = self.start
		return self

	def __next__(self):
		if self.current <= self.end:
			value = self.current
			self.current += 1
			return value

		else:
			raise StopIteration

for i in RangeIterator(1,7):
	print(i)
