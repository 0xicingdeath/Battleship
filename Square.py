class Square: 
	def __init__(self): 
		from Coordinate import Coordinate
		self.__guessed = False; 
		self.__hit = False; 
		self.__shipID = None; 
		self.__location = None

	def getGuessed(self): 
		return guessed 

	def setGuessed(self, x): 
		self.__guessed = x

	def hasShip(self): 
		return self.__shipID >= 0

	def addShip(self, uid): 
		self.__shipID = uid 	

	def shipHit(self): 
		self.__hit = True

	def getID(self): 
		return self.__shipID

	def __str__(self): 
		return "guessed : " + str(self.__guessed) + " ship : " + str(self.__containsShip) + " hit : " + str(self.__hit); 

