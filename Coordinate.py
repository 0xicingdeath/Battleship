class Coordinate: 

	def __init__(self, xc, yc): 
		self.__x = xc 
		self.__y = yc

	def getX(self): 
		return self.__x

	def getY(self): 
		return self.__y

	def __eq__(self, coord2): 
		return self.__x == coord2.getX() and self.__y == coord2.getY()

	def __str__(self): 
		return "x : " + str(self.__x) + " y: " + str(self.__y)
