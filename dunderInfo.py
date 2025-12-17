'''
							Dunder Methods
Dunder methods are magic methods starting with __

Important onces :
	1.__str__                     Print Object
	2.__repr__		      Debug Output
	3.__len__		      length
	4.__add__		      Overloading +
	5.__eq__		      Compare Objects
	6.__iter__		      Make Iterable

'''
# RobotArm class using magic methods

class RobotArm:
	def __init__(self,name,joints,max_speed):
		self.name = name
		self.joints = joints
		self.max_speed = max_speed

	# __str__ -> human readable (operator display)
	def __str__(self):
		return f"RobotArm {self.name} with {self.joints} joints"

	# __repr__ -> debug / logging
	def __repr__(self):
		return f"RobotArm(name={self.name},joints={self.joints},max_speed={self.max_speed})"

	# __len__ -> number of joints
	def __len__(self):
		return self.joints

	# __add__ -> combine two robot arms
	def __add__(self,other):
		return RobotArm(
			name = f"{self.name}-{other.name}",joints=self.joints+other.joints,
			max_speed = min(self.max_speed,other.max_speed))

	# __eq__ -> compare two robot arms
	def __eq__(self,other):
		return (self.joints == other.joints and self.max_speed == other.max_speed)

	# __iter__ -> iterate over joint speeds
	def __iter__(self):
		for i in range(self.joints):
			return f"joint {i+1} runnning at {self.max_speed} rpm"

arm1 = RobotArm("A1", joints = 6, max_speed=120)
arm2 = RobotArm("A2",joints=4,max_speed=100)

print("Arm1 : ",arm1)
print(len(arm1))
