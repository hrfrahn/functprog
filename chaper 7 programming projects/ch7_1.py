# harrison frahn
# period 2
# chapter 7.1
# expected input: 3 numbers separated by commas
def isRight(a,b,c):
	if a**2+b**2==c**2 or a**2+c**2==b**2 or c**2+b**2==a**2:
		return True
	else:
		return False
def main():
	a,b,c=eval(input("Enter the 3 side lengths, separated by commas: "))
	if isRight(a,b,c) == True:
		print("The triangle is right.")
	else:
		print("The triangle is not right.")
if __name__ == '__main__':
	main()