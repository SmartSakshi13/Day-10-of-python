# OOP factory pattern

# It creates object dynamically which is used in robot plugin system

'''

Factory pattern mhanje object tyar karnyachi jababdari veglya class la dene

Mhanje :
	Main code la object kasa banavto te mahiti nako
	Fakta sangaych konta type hava aahe
'''

class Camera:
	def capture(self):
		print("Capturing image")

class Lidar:
	def scan(self):
		print("Scanning environment")

class sensorFactory:
	'''
		hee ek factory class aahe
		hich kam = yogya sensor object tayyar karun dene
	'''
	def create(self,type):
		# type tells which sensor you want
		if type == "camera":
			return Camera()
		if type == "lidar":
			return Lidar()

factory = sensorFactory()

s1 = factory.create("camera")
s2 = factory.create("lidar")

s1.capture()
s2.scan()
