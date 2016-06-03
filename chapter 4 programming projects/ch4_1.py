#Harrison Frahn
#period 2
#chapter 4.1
#no input expected 
from graphics import *
def main():
	win = GraphWin("A checkerboard")
	border = Rectangle(Point(0,0),Point(200,200))
	border.setFill(color_rgb(205,133,63))
	border.draw(win)
	redSquares = Rectangle(Point(8,8),Point(192,192))
	redSquares.setFill('red')
	redSquares.draw(win)
	topLeft = Point(8,8)
	bottomRight = Point(31,31)
	for i in range(8):
		blackSqaures = []
		if(i%2!=0):
			topLeft.move(23,0); bottomRight.move(23,0)
		elif(i!=0):
			topLeft.move(-23,0); bottomRight.move(-23,0)
		for x in range(4):
			blackSqaures.append(Rectangle(topLeft,bottomRight))
			blackSqaures[x].setFill('black')
			blackSqaures[x].draw(win)
			topLeft.move(46,0); bottomRight.move(46,0)
		topLeft.move(-184,23); bottomRight.move(-184,23)
	win.getMouse()
	win.close()
main()