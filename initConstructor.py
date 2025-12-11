# part 3 - _init_ constructor

# Thing of constructor as robot's birth

class robot:
	def __init__(self,name):
		self.name = name

r = robot("TurtleBot")
print(r.name)
