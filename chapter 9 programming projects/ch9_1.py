# Harrison Frahn
# Peroid 2
# Chapter 9.1
# expected input: how many times to run the simulation
from random import random
import time as t
from graphics import *
def inCircle(pX,pY):
    if pX**2 + pY**2 <= 1:
        return True
    else:
        return False
def main():
    print("This program calculates the value of pi using a Monte Carlo simulation")
    times = eval(input("How many darts should be randomly thrown?: "))
    a = t.time()
    h=0
    vis = input("Run the visual simulation as well? This will look cool, but make the program a \nLOT slower:(y/n) ")
    if vis[0].upper() == "Y":
        win = GraphWin("Visual Simulation",545,545)
        win.setCoords(-1,-1,1,1)
        Image(Point(0,0),'dartboard.gif').draw(win)
    for i in range(times):
        pX = 2*random()-1; pY = 2*random()-1
        if vis[0].upper() =="Y":
            Point(pX,pY).draw(win)
        if inCircle(pX,pY):
            h+=1
    b = t.time()
    time = b-a
    if vis[0].upper() =="Y":
    	print("Click on the window to quit.")
    print("Approximated Value of Pi = 4 *",h,"/",times," = ",4*h/times)
    print("Time = {0:0.2f} seconds.".format(time))
    if vis[0].upper() =="Y":
        win.getMouse()
main()
