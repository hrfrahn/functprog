# harrison frahn
# period 2 
# chapter 4.3
# no input expected
from graphics import *
def main():
	win = GraphWin()
	title = Text(Point(100,150),"Drawing dice...")
	title.draw(win)
	#drawing the dice
	Rectangle(Point(10,88),Point(35,113)).draw(win)
	Rectangle(Point(40,88),Point(65,113)).draw(win)
	Rectangle(Point(70,88),Point(95,113)).draw(win)
	Rectangle(Point(100,88),Point(125,113)).draw(win)
	Rectangle(Point(130,88),Point(155,113)).draw(win)
	Rectangle(Point(160,88),Point(185,113)).draw(win)
	# drawing points on die 1
	Point(22,100).draw(win)
	# die 2
	Point(46,94).draw(win)
	Point(59,107).draw(win)
	# die 3
	Point(76,94).draw(win)
	Point(82,100).draw(win)
	Point(89,107).draw(win)
	# die 4
	Point(106,94).draw(win)
	Point(119,94).draw(win)
	Point(106,107).draw(win)
	Point(119,107).draw(win)
	# die 5
	Point(136,94).draw(win)
	Point(149,94).draw(win)
	Point(142,100).draw(win)
	Point(136,107).draw(win)
	Point(149,107).draw(win)
	# die 6
	Point(166,94).draw(win)
	Point(179,94).draw(win)
	Point(166,100).draw(win)
	Point(179,100).draw(win)
	Point(166,107).draw(win)
	Point(179,107).draw(win)
	title.setText("Click to quit:")
	win.getMouse()
main()