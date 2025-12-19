class point:
	
	def __init__(self,x,y):
		self.x = x
		self.y = y

	def __add__(self,other):
		return point(self.x + other.x,self.y + other.y)

	def __eq__(self,other):
		return self.x == other.x and self.y == other.y

	def __str__(self):
		return f"(x = {self.x},y = {self.y})"

p1 = point(10,20)
p2 = point(1,2)

p3 = p1 + p2
print("Addition : ",p3)
print("Equality : ",p1 == p2)
