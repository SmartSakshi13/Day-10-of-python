# program of single inheritance

# single inheritance means child class inheritis properties of one parent class

class robot:
	def say_hello(self):
		print("Hello")
	
class humanoid(robot):
	pass

h = humanoid()
h.say_hello()
