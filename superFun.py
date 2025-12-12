# used to call parent constructor

class robot:
	def __init__(self,name):
		self.name = name
		
class drone(robot):
	def __init__(self,name,altitude):
		super().__init__(name)
		self.altitude = altitude
		print(f"Name : {self.name} , Altitude : {self.altitude}")

d = drone("TurtleBot","150deg")
