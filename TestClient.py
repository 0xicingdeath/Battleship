from Gamefield import Gamefield
from Square import Square
from Fleet import Fleet
from Constants import Constants
#import unittest 
from DuplicateIDException import DuplicateIDException
from PastBound import PastBound
from OverlapException import OverlapException
from Coordinate import Coordinate

#class TestClient(unittest.TestCase): 
class TestClient(): 

	p1 = Gamefield(Constants.width, Constants.height) 
	p2 = Gamefield(Constants.width, Constants.height) 		
	player1 = Fleet() 
	player2 = Fleet()


 
 	try: 
		player1.addToFleet(0, 5, Coordinate(-1, 0,), "v")
	except PastBound: 
		print("caught past bound exception")

	player1.addToFleet(0, 4, Coordinate(1,1), "v")	

	#self.assertRaises(DuplicateIDException, player1.addToFleet, (0, 4, 2, 2, "h"))
	try: 
		player1.addToFleet(0, 4, Coordinate(2, 2), "h")
	except DuplicateIDException: 
		print("caught Duplicate id Exception")

	#player1.addToFleet(0, 5, 1, 1, "v")	
	try: 
		player1.addToFleet(1, 2, Coordinate(1, 1), "v")
	except OverlapException: 
		print("caught vertical overlap")

	try: 
		player1.addToFleet(2, 3, Coordinate(1, 1), "h")
	except OverlapException: 
		print("caught horiz overlap")

	player1.addToFleet(1, 2, Coordinate(5, 5), "h")
	player1.addToFleet(2, 3, Coordinate(4, 4), "v")
	player1.addToFleet(3, 3, Coordinate(2, 1), "h")
	player1.addToFleet(4, 5, Coordinate(6, 0), "v")

	p1.addFleet(player1)
	p2.addFleet(player2)

	print (str(p1.printFleet()))

	print str(p1.hitOrMiss(Coordinate(5,5)))

