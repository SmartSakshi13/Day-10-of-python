# create a temperature class with property setter - restrict temperature < 120

class temperature:
	def __init__(self,temper):
		self.temper = temper

	@property
	def temper(self):
		return f"Temperature : {self._temper}"

	@temper.setter
	def temper(self,value):
		if value < 120:
			raise ValueError("Temperature must be above 120 degree celcius")
		self._temper = value

t = temperature(130)
print(t.temper)

t.temper = 100
print(t.temper)

