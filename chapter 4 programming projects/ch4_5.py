#harrison Frahn
# period 2
# chapter 4.5
#expected input: 2 clicks
from graphics import *
def main():
    win = GraphWin()
    title = Text(Point(100,20),"Click on 2 points:")
    title.draw(win)
    p1 = win.getMouse(); p1.draw(win)
    p2 = win.getMouse(); p1.undraw()
    line = Line(p1,p2); 
    line.draw(win)
    midPoint = line.getCenter()
    slope = -1/((p1.getY()-p2.getY())/(p1.getX()-p2.getX()))
    p3 = Point(p1.getX(), slope*(p1.getX()-midPoint.getX())+midPoint.getY())
    p4 = Point(p2.getX(), slope*(p2.getX()-midPoint.getX())+midPoint.getY())
    bisector = Line(p3,p4); bisector.setFill('peachpuff')
    bisector.draw(win)
    title.setText("Click to quit:")
    win.getMouse()
main()
