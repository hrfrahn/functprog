# harrison frahn
# period 2 
# chapter 8.2
# expected input: 3 of the 4 variables
from math import sqrt
def solveQuad(a,b,c,d):
	dis = b**2-4*a*c
	if dis < 0:
		raise RuntimeError("The quadratic has no real solution.")
	else:
		x1 = (-b+sqrt(dis))/(2*a)
		x2 = (-b-sqrt(dis))/(2*a)
		d.append(x1);d.append(x2)
def main():
	print("This program calculates the value of the missing variable in the equation:\ns(t) = -0.5gt^2+v0t+h0, where \ns(t) is the current position\ng = acceleration due to gravity(9.8 meters/second) \nt = time object has been in the air \nv0= initial velocity of the object \nh0 = initial height of the object.")
	not_enter = input("Which variable will you not be entering?(Either s, t, v0 or h0): ")
	if not_enter == 's':
		t = eval(input("Enter the time the object has been in the air in seconds (t): "))
		v0 = eval(input("Enter the initial velocity of the object in meters/second (v0): "))
		h0 = eval(input("Enter the initial height of the object in meters(h0): "))
		sT = max(-4.9*t**2+v0*t+h0,0)
		print("Current Height:",sT,"meters.")
	elif not_enter == 't':
		d = []
		s = eval(input("Enter the current height above the ground in meters (s(t)): "))
		v0 = eval(input("Enter the initial velocity of the object in meters/second (v0): "))
		h0 = eval(input("Enter the initial height of the object in meters(h0): "))
		t = solveQuad(-4.9,v0,h0-s,d)
		if d[1] < 0:
			print("Time:",d[0],"seconds.")
		elif d[0] < 0:
			print("Time:",d[1],"seconds.")
		else:
			print("Time:",d[1],"or",d[0],"seconds.")
	elif not_enter == 'v0':
		s = eval(input("Enter the current height of the object in meters (s): "))
		t = eval(input("Enter the time the object has been in the air in seconds (t): "))
		h0 = eval(input("Enter the initial height of the object in meters(h0): "))
		if s!=h0 and t <= 0:
			raise RuntimeError("The current height and initial height must be the same if no time has passed.")
		v = 4.9*t-h0+s
		print("Initial velocity:",v,"meters/second.")
	elif not_enter == 'h0':
		s = eval(input("Enter the current height of the object in meters (s): "))
		t = eval(input("Enter the time the object has been in the air in seconds (t): "))
		v0 = eval(input("Enter the initial velocity of the object in meters(h0): "))
		h = 4.9*t**2-v0*t+s
		print("Initial height:",h,"meters")
	else:
		print("You didn't enter s, t, v0, or h0!")
if __name__ == '__main__':
	main()