'''

Singleton pattern ensures that a class has only one instance and provides a global point of access to that instance

applyala eka class che object fakta ekdach banvayche aahet aani tya object la application chya kuthunahi access karta 
yeil
'''

class singleton:
	_instance = None # ha instance sathavnyasathi class variable
	def __new__(cls,*args): # this will called before init and cls referes to the class itself
		if cls._instance is None: # jar object aadhich banlela nasel
			cls._instance = super().__new__(cls) # object banav
		return cls._instance

	def __init__(self,value = None):
		if not hasattr(self,'_initialized'):	#fakta ekdach initailize kar
			self.value = value
			self._initialized = True

s1 = singleton(10)
s2 = singleton(20)

print(s1.value)
print(s2.value)
print(s1 is s2)


'''

singleton = ekach instance , global access
use-case = Database connection,logger,config
python trick = __new__ + _instance  variable

'''
'''
singleton madhe __new__(cls) ass vaparla tar error yenar because :===
	internally aas call hoota =====>> singleton.__new__(singleton,10)
'''
