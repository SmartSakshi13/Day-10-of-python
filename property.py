'''
Used to create getter/setter like real attributes

This is used to protect robot hardware values
'''
class Motor:
	def __init__(self,speed):
		self.speed = speed

	@property
	def speed(self):
		return self.__speed

	@speed.setter
	def speed(self,value):
		if value < 0:
			raise valueError("Speed cannot be negative")
		self.__speed = value

m = Motor(40)
print(m.speed)
m.speed = 20
print(m.speed)
#m.speed = -5
#print(m.speed)
