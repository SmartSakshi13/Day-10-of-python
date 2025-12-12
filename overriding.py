# child class modifies parent's function

class robot:
	def speak(self):
		print("Robot Speaking:")
class dog(robot):
	def speak(self):
		print("Woof woof")

d = dog()
d.speak()
