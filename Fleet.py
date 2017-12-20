class Fleet: 

	def __init__(self): 
		from Coordinate import Coordinate 
		from Ships import Ships

		self.__allShips = []

	def getFleet(self): 
		return self.__allShips 

	def addToFleet(self, uid, length, coord, direction): 
		from DuplicateIDException import DuplicateIDException
		from Coordinate import Coordinate
		from FullException import FullException

		if len(self.__allShips) == 5: 
			raise FullException("Cannot add entry. Maximum ships reached.")

		if self.__iden(uid): 
			raise DuplicateIDException("Cannot add entry. Exists a ship with same id. ")

		if (direction == "v"): 
			self.__vertical(uid, length, coord)
		elif (direction == "h"): 
			self.__horizontal(uid, length, coord)

	def __iden(self, uid): 
		for temp in self.__allShips: 
			if (temp.getID() == uid): 
				return True 
		return False

	def __overlap(self, tempCoord): 
		for ship in self.__allShips: 
			for coord in ship.getLoc(): 
				if coord in tempCoord: 
					return True
		return False 


	def __vertical(self, uid, length, coord): 
		from Ships import Ships
		from PastBound import PastBound
		from OverlapException import OverlapException
		from Coordinate import Coordinate

		if (not self.__withinBound(length, coord)): 
			raise PastBound("Past boundaries of the board " + str(coord.getX()) + ", " + str(coord.getY()))
			return False 

		temp = [Coordinate(coord.getX(), coord.getY()+x) for x in xrange(length)]	
		print "type of temp : "  + (str(type(temp)))
 
		if (self.__overlap(temp)): 
			raise OverlapException("Two ships overlap, unable to add") 
			return False

		self.__allShips += [Ships(uid, temp)]
		return True; 			

	def __horizontal(self, uid, length, coord): 
		from Ships import Ships
		from PastBound import PastBound
		from OverlapException import OverlapException
		from Coordinate import Coordinate
		if (not self.__withinBound(length, coord)): 
			raise PastBound("Past boundaries of the board.")
			return False 

		temp = [Coordinate(coord.getX()+x, coord.getY()) for x in xrange(length)]			
		if (self.__overlap(temp)): 
			raise OverlapException("Two ships overlap, unable to add") 
			return False

		print "type of temp : "  + (str(type(temp)))

		self.__allShips += [Ships(uid, temp)]
		return True; 	

	def __withinBoundV(self, length, coord): 
		from Constants import Constants
		from Coordinate import Coordinate
		if ((coord.getY() + length > Constants.height or self.__zeroCheck(coord)) or (coord.getX() + length > Constants.width or self.__zeroCheck(coord)): : 
			return False; 
		return True; 	

	def __zeroCheck(self, coord): 
		return coord.getX() < 0 or coord.getY() < 0