# create a vehicle abstract class with start(),stop(),accelerate()  Then create car and bike classes

from abc import ABC,abstractmethod
import time

class vehicle(ABC):
	@abstractmethod
	def start(self):
		pass

	@abstractmethod
	def stop (self):
		pass

	@abstractmethod
	def accelerate(self,speed):
		self.speed = speed

class car(vehicle):
	def start(self):
		print("Car Started")

	def stop(self):
		print("Car Stoped")

	def accelerate(self,speed):
		print(f"Car accelerated at speed {speed}m/s")

class bike(vehicle):
	def start(self):
		print("Bike Started")
	
	def stop(self):
		print("Bike Stop")
	
	def accelerate(self,speed):
		print(f"Bike accelerated at speed {speed}m/s")

c = car()
b = bike()

print("Car Details")
c.start()
c.accelerate(25)
c.stop()

time.sleep(1)

print("Bike Details")
b.start()
b.accelerate(30)
b.stop()


