# harrison frahn
# period 2
# project 3.3
# expected input: x1,y1,z1 (<enter>) x2,y2,z2
import math
def main():
	print("This program calculates the distance between 2 3-dimensional points.")
	x1,y1,z1 = eval(input("Please enter the coordinates of the first point: "))
	x2,y2,z2 = eval(input("Please enter the coordinates of the second point: "))
	distance = math.sqrt((x2-x1)**2+(y2-y1)**2+(z2-z1)**2)
	print("The distance between the 2 points is", distance,".")
main()
	