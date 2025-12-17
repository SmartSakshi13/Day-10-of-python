'''
Tiny classes that provides extra information'''

class loggerMixin:
	def log(self,msg):
		print("[LOG]",msg)

class Robot(loggerMixin):
	def move(self):
		self.log("Moving Forward")


r = Robot()
r.log("This is msg")
r.move()
'''
ROS2 code uses mixins for logging ,debugging,etc
'''

