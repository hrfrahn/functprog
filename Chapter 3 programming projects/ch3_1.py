# harrison frahn
# period 2
# project 3.1
# expected input: 2 numbers separated by a comma
import math
def main():
	print("This program computes the surface area and range of a cylinder.")
	rad, h = eval(input("Please enter the radius and height separated by a comma: "))
	vol = math.pi*rad**2*h
	SA = 2*math.pi*rad*(h+rad)
	print("volume: ", vol, "\nSurface area: ", SA)
main()