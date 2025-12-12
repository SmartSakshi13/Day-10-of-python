class player:
	def __init__(self,name):
		self.name = name

class Team:
	def __init__(self,players):
		self.players = players # agreegation

	def show(self):
		print("Team players:")
		for p in self.players:
			print("-",p.name)

p1 = player("Ronaldo")
p2 = player("Messi")

team = Team([p1,p2])
team.show()

print("\n Player still exist even if team is deleted:")
del team
print(p1.name," and ",p2.name)
