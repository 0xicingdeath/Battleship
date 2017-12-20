class Ships: 
	def __init__(self, uID, loc): 
		from Coordinate import Coordinate
		self.__uID = uID
		self.__sunk = False
		self.__loc = loc
		self.__sunk = self.__initSunk()

	def getID(self): 
		return self.__uID

	def getSunk(self): 
		return self.__sunk

	def getLoc(self): 
		return self.__loc

	def doesOccupy(self, location): 
		from Coordinate import Coordinate
		return self.__helper(location) >= 0

	def setSunk(self, coord): 
		index = self.__helper(coord) 
		self.__sunk[index] = True

	def __helper(self, location): 
		from Coordinate import Coordinate
		count = 0; 		
		for coord in self.__loc: 
			print "coord: " + str(coord)  + " location : " + str(location)
			count+=1
			if location == coord: 
				return count
		return -1				


	def hitCoord(self, index, xc, xy): 
		self.__coord[index] = True
		if __isSunk(): 
			self.__sunk = True; 

	def __initSunk(self): 
		self.__sunk = [[False] for i in xrange (len(self.__loc))]

	def __isSunk(self): 
		return False not in self.__coord

	def __str__(self): 
		return "id: " + str(self.__uID) + " sunk : " + str(self.__sunk) + " loc :" + str(self.__loc)



