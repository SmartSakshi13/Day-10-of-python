# part 4 - methonds inside function

class robot:
	def __init__(self,name):
		self.name = name
	def speak(self):
		print(f"I am {self.name}")

r = robot("TurtleBot")
r.speak()
