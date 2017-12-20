class Gamefield: 
	def __init__(self, width, height): 
		from Square import Square

		self.__board = [[Square() for y in xrange(width)] for x in xrange(height)]

		from Ships import Ships 
		from Fleet import Fleet

		self.__fleet = []

	def hitOrMiss(self, coord): 
		from Coordinate import Coordinate 
		if self.__board[coord.getX()][coord.getY()].hasShip(): 
			self.__board[coord.getX()][coord.getY()].setGuessed(True) 
			self.__board[coord.getX()][coord.getY()].shipHit() 
			hitShip = self.__board[coord.getX()][coord.getY()].getID()
			self.__changeHit(coord)

	def printFleet(self): 
		print (str(self.__fleet))		


	def __changeHit(self, coord): 
		from Coordinate import Coordinate 
		tempCount = 0; 
		for ships in self.__fleet: 
			print " occupy : " + str(ships.doesOccupy(coord)) 
			if ships.doesOccupy(coord): 
				self.__fleet[tempCount].setSunk(coord)
			tempCount+=1


	#def isSunk(Location): 

	def addFleet(self, fleet): 
		from Ships import Ships
		for ships in fleet.getFleet(): 
			self.__addShip(ships.getID(), ships.getLoc())

	def __addShip(self, uid, loc):
		from Ships import Ships
		from Coordinate import Coordinate
		print "type of loc : " + str(type(loc))
		for coord in loc:  
			xc = coord.getX()
			yc = coord.getY()
			self.__board[xc][yc].addShip(uid)
		self.__fleet += [Ships(uid, loc)]


	def __withinRange(self, length, x, y, direction): 
		for i in self.__ships: 
			if (direction == "v"): 
				self.__vertical(i, length, x, y) 
			else: 
				self.__horizontal(length, x, y)
