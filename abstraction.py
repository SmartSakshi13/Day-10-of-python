# It only shows necessary Information

from abc import ABC,abstractmethod

class shape(ABC):
	@abstractmethod
	def area(self):
		pass
class square(shape):
	def __init__(self,s):
		self.s = s
	def area(self):
		return self.s * self.s

sq = square(5)
print(sq.area())

'''

	ABC = abstract base class

'''
