class motor:
	def __init__(self,name):
		self.name = name
		self.speed = 0

	def set_speed(self,value):
		self.speed = value
		print(f" {self.name} speed set to {value}")

m1 = motor("Left motor")
m1.set_speed(50)
