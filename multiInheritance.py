class a:
	def showA(self):
		print("A")
class b:
	def showB(self):
		print("B")

class c(a,b):
	pass

c = c()
c.showA()
c.showB()

