class LoggerMixin:
	def log(self,msg):
		print (f"[LOG] : {msg}")


class robot(LoggerMixin):
	def __init__(self,name):
		self.name = name

	def move(self):
		self.log(f"{self.name} is moving Forward")

r = robot("Spider")
r.move()

