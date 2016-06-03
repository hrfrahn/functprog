# harrison frahn
# period 2
# chapter 6.5
# expected input: perceived length & width and actual length & width
from graphics import *
def calcArea(length,width):
	return length * width
def percentError(actual,perceived):
	return (abs(actual-perceived)/actual)*100
def main():
        win = GraphWin("Percent Error Calculator",400,200)
        Text(Point(200,20),"This program calculates the percent error of the area of a rectangle.").draw(win)
        plEntry,pwEntry,alEntry,awEntry = Entry(Point(200,50),20),Entry(Point(200,80),20),Entry(Point(200,110),20),Entry(Point(200,140),20)
        plEntry.draw(win);pwEntry.draw(win);alEntry.draw(win);awEntry.draw(win)
        plEntry.setText("Perceived Length");pwEntry.setText("Perceived width");alEntry.setText("Actual Length");awEntry.setText("Actual Length")
        Text(Point(200,170),"Click to calculate").draw(win); win.getMouse()
        pLength, pWidth = eval(plEntry.getText()), eval(pwEntry.getText())
        aLength, aWidth = eval(alEntry.getText()), eval(awEntry.getText())
        pArea = calcArea(pLength,pWidth); aArea = calcArea(aLength,aWidth) 
        error = percentError(aArea,pArea)
        win.close()
        win1 = GraphWin("Results")
        Text(Point(100,50),"Perceived area: "+str(pArea)).draw(win1)
        Text(Point(100,100),"Actual area: "+str(aArea)).draw(win1)
        Text(Point(100,150),"Error: "+str(round(error,2))+"%").draw(win1)
        win1.getMouse()
main()
