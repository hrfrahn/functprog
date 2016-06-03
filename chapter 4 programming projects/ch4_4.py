# Harrison Frahn
# period 2
# chapter 4.4
# expected input: Principal, rate, and term, in the repsective boxes
from graphics import *
def main():
	win = GraphWin("Interest Calculator")
	title = Text(Point(100,20),"Enter the principal, rate, and time.")
	title.draw(win)
	pEntry = Entry(Point(100,60),10)
	pEntry.draw(win); pEntry.setText("Principal")
	rEntry = Entry(Point(100,100),10)
	rEntry.draw(win); rEntry.setText("Rate")
	tEntry = Entry(Point(100,140),10)
	tEntry.draw(win); tEntry.setText("Time(years)")
	button = Rectangle(Point(65,160),Point(135,180))
	button.setFill('green'); button.draw(win)
	Text(Point(100,170),"Compute").draw(win)
	p = win.getMouse()
	while(p.getX()<65 or p.getX()>135 or p.getY()<160 or p.getY()>180):
		p = win.getMouse()
	principle = float(pEntry.getText())
	rate = float(rEntry.getText())
	time = float(tEntry.getText())
	interest = principle*rate*time
	win.close()
	endWin = GraphWin("Your Earnings")
	Text(Point(100,100),"You earned $"+str(interest)+" in interest!").draw(endWin)
	endButton = Rectangle(Point(75,125),Point(125,150))
	endButton.draw(endWin); endButton.setFill('red')
	Text(Point(100,137),"Quit").draw(endWin)
	x = endWin.getMouse()
	while(x.getX()<65 or x.getX()>135 or x.getY()<160 or x.getY()>180):
		x = win.getMouse()
	endWin.close()
main()