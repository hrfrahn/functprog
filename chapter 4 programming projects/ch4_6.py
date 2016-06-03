# harrison frahn
# period 2
# chapter 4.6
# expected input: 3 clicks
from graphics import *
from math import sqrt
def main():
	win = GraphWin()
	title = Text(Point(100,20),"Click 3 points:")
	title.draw(win)
	p1 = win.getMouse(); p1.draw(win)
	p2 = win.getMouse(); p2.draw(win)
	p3 = win.getMouse(); p1.undraw(); p2.undraw()
	triangle = Polygon(p1,p2,p3)
	triangle.draw(win)
	a = sqrt((p1.getX()-p2.getX())**2+(p1.getY()-p2.getY())**2)
	b = sqrt((p2.getX()-p3.getX())**2+(p2.getY()-p3.getY())**2)
	c = sqrt((p3.getX()-p1.getX())**2+(p3.getY()-p1.getY())**2)
	print(a,b,c)
	s = (a+b+c)/2
	area = sqrt(s*(s-a)*(s-b)*(s-c))
	areaText = Text(Point(100,170),"The area is "+str(area))
	areaText.draw(win)
	title.setText("Click to quit:")
	win.getMouse()
	win.close()
main()