# harrison frahn
# period 2
# chapter 7.2
# expected input: 3 numbers, separated by commas
def isTriangle(a,b,c):
	if a+b>c and a+c>b and c+b>a:
		return True
	else:
		return False
def main():
	a,b,c = eval(input("Enter the 3 side lengths, separated by commas: "))
	if isTriangle(a,b,c) == True:
		print("It is a triangle.")
	else: 
		print("It is not a triangle.")
if __name__ == '__main__':
	main()