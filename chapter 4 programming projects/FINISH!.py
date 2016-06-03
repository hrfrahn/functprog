# Harrison Frahn
# period 2
# chapter 4.2
# no expected input
from graphics import *
def drawWitch(win):
	face = Circle(Point(50,76),17)
	face.setFill('green'); face.draw(win)
	eye1 = Circle(Point(42,70),4)
	eye1.setFill('white'); eye1.draw(win)
	Point(42,70).draw(win)
	eye2 = Circle(Point(58,70),4)
	eye2.setFill('white'); eye2.draw(win)
	Point(58,70).draw(win)
	nose = Polygon(Point(50,70),Point(45,80),Point(55,80))
	nose.setFill('green4'); nose.setOutline('green4'); nose.draw(win)
	Point(47,78).draw(win)
	Point(53,78).draw(win)
	# mouth = Polygon()
	hatMiddle = Polygon(Point(50,20),Point(35,65),Point(65, 65))
	hatMiddle.setFill('black'); hatMiddle.draw(win)
	hatTop = Polygon(Point(50,20),Point(70,15),Point(40,50))
	hatTop.setFill('black'); hatTop.draw(win)
	hatLeft = Polygon(Point(35,65),Point(20,65),Point(40,55))
	hatLeft.setFill('black'); hatLeft.draw(win)
	hatRight = Polygon(Point(65,65),Point(80,65),Point(40,45))
	hatRight.setFill('black'); hatRight.draw(win)
def main():
	win = GraphWin('THIS IS HALLOWEEN')
	drawWitch(win)
	# drawPumpkin(win)
	# drawGhost(win)
	win.getMouse()
	win.close()
main()
