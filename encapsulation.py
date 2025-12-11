
# Encapsulation program
# Encapsulation means hinding internal details showing only esential data
# use _var or __var for make the variable private or protected

class battery:
	def __init__(self):
		self.__level = 100 # privat

	def get_level(self):
		return self.__level


b = battery()
print(b.get_level())
