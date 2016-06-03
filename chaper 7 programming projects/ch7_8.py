# harrison frahn
# period 2
# chapter 7.8
# expected input: the four coordinates of the trapezoid
# height/area formula from http://www.murderousmaths.co.uk/books/trap.htm
from graphics import *
from math import sqrt
def getSlope(p1,p2):
	try:
		return (p1.getY() - p2.getY())/(p1.getX()-p2.getX())
	except ZeroDivisionError:
		return 0
def validateParallel(p1,p2,p3,p4,bases):
	if getSlope(p1,p2) == getSlope(p4,p3) and getSlope(p1,p4) != getSlope(p2,p3) and getSlope(p1,p3) != getSlope(p2,p4):
		bases[0] = p1; bases[1] = p2; bases[2] = p3; bases[3] = p4;
		return True
	if getSlope(p1,p4) == getSlope(p2,p3) and getSlope(p1,p2) != getSlope(p4,p3) and getSlope(p1,p3) != getSlope(p2,p4):
		bases[0] = p1; bases[1] = p4; bases[2] = p2; bases[3] = p3;
		return True
	if getSlope(p1,p3) == getSlope(p2,p4) and getSlope(p1,p2) != getSlope(p4,p3) and getSlope(p1,p4) != getSlope(p2,p3):
		bases[0] = p1; bases[1] = p3; bases[2] = p2; bases[3] = p4;
		return True
	else: 
		return False
def main():
	try: 
		win = GraphWin("Coordinate Entry",400,225)
		title =  Text(Point(200,50),"Please enter the Coordinates of the four points of the trapezoid\n in the corresponding boxes and click \"Calculate\" when done.")
		title.setStyle('italic'); title.setSize(14); title.draw(win)
		x1entry = Entry(Point(100,100),7); x1entry.draw(win)
		x2entry = Entry(Point(100,125),7); x2entry.draw(win)
		x3entry = Entry(Point(100,150),7); x3entry.draw(win)
		x4entry = Entry(Point(100,175),7); x4entry.draw(win)
		y1entry = Entry(Point(200,100),7); y1entry.draw(win)
		y2entry = Entry(Point(200,125),7); y2entry.draw(win)
		y3entry = Entry(Point(200,150),7); y3entry.draw(win)
		y4entry = Entry(Point(200,175),7); y4entry.draw(win)
		x = 1
		for i in range(100,200,25):
			x1 = Text(Point(50,i),"x"+str(x)); x1.setSize(16); x1.draw(win)
			x+=1
		x = 1
		for i in range(100,200,25):
			x1 = Text(Point(150,i),"y"+str(x)); x1.setSize(16); x1.draw(win)
			x+=1
		button = Rectangle(Point(90,190),Point(210,220)); button.setFill('green4'); button.draw(win)
		quit = Text(Point(150,205),"Calculate"); quit.draw(win)
		a = Text(Point(300,100),"Area:"); a.setSize(18); a.draw(win)
		p = win.getMouse()
		while p.getX() < 90 or p.getX() > 220 or p.getY() < 190 or p.getY() > 220:
			p = win.getMouse()
		p1 = Point(eval(x1entry.getText()), eval(y1entry.getText()))
		p2 = Point(eval(x2entry.getText()), eval(y2entry.getText()))
		p3 = Point(eval(x3entry.getText()), eval(y3entry.getText()))
		p4 = Point(eval(x4entry.getText()), eval(y4entry.getText()))
		areaText = Text(Point(320,150),"You entered an invalid Trapezoid!\nPlease enter the values again."); areaText.setSize(12)
		bases = [p1,p2,p3,p4]
		while validateParallel(p1,p2,p3,p4,bases) == False:
			if x < 6:	
				areaText.draw(win)
			p = win.getMouse()
			while p.getX() < 90 or p.getX() > 220 or p.getY() < 190 or p.getY() > 220:
				p = win.getMouse()
			p1 = Point(eval(x1entry.getText()), eval(y1entry.getText()))
			p2 = Point(eval(x2entry.getText()), eval(y2entry.getText()))
			p3 = Point(eval(x3entry.getText()), eval(y3entry.getText()))
			p4 = Point(eval(x4entry.getText()), eval(y4entry.getText()))
			x+=1
		a = round(sqrt((bases[1].getX()-bases[0].getX())**2+(bases[1].getY()-bases[0].getY())**2), 2)
		c = round(sqrt((bases[3].getX()-bases[2].getX())**2+(bases[3].getY()-bases[2].getY())**2), 2)
		b = round(sqrt((bases[3].getX()-bases[1].getX())**2+(bases[3].getY()-bases[1].getY())**2), 2)
		d = round(sqrt((bases[2].getX()-bases[0].getX())**2+(bases[2].getY()-bases[0].getY())**2), 2)
		base = (a+c)/2
		triBase = max(a,c)-min(a,c)
		s = 1/2*(triBase+b+d)
		triArea = round((s*(s-triBase)*(s-d)*(s-b))**0.5,2)
		triHeight = 2*triArea/triBase
		rectArea = min(a,c)*triHeight
		area = triArea+rectArea
		areaText = Text(Point(300,150),str(area)); areaText.setSize(18); areaText.draw(win)
		quit.setText("Quit")
		p = win.getMouse()
		while p.getX() < 90 or p.getX() > 220 or p.getY() < 190 or p.getY() > 220:
				p = win.getMouse()
	except:
		win.close()
		win = GraphWin("ERROR!!", 200, 200)
		Text(Point(100,100),"Something went wrong!\nTry running the program again.").draw(win)
		button = Rectangle(Point(80,120),Point(120,140)); button.setFill('green4'); button.draw(win)
		quit = Text(Point(100,130),"Quit"); quit.draw(win)
		p = win.getMouse()
		while p.getX() < 80 or p.getX() > 120 or p.getY() < 120 or p.getY() > 140:
				p = win.getMouse()
main()