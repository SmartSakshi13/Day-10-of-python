class Engine:
	def start(self):
		print("Engine Start")
	
class car:
	def __init__(self):
		self.engine = Engine() #composition

c = car()
c.engine.start()

