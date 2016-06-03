# Harrison Frahn
# Peroid 2
# Chapter 9.2
# expected input: how many times to run the simulation
from random import random
from time import time
def main():
	print("This program calculates a random walk.")
	steps = 0
	times = eval(input("How many times should the simulation be run?: "))
	avg = 0
	flips = eval(input("How many times should the coin be flipped each time?: "))
	y,b,c = 0,0,0
	for x in range(times):
		for i in range(flips):
			a = random()
			if a < 0.5:
				steps -= 1
				b+=1
			else:
				steps += 1
				c+=1
			y += 1
		avg += steps
	avg /= times
	print("Steps taken   :",y)
	y/= times
	print("Forward steps :",c)
	print("Backward steps:",b)
	print("Average steps per simulation:",y)
	print("Average position from start: {0:0.2f}".format(avg))
main()
	