# harrison frahn
# period 2
# project 3.5
# expected input: the number of numbers to be entered, <enter>, then the numbers with an <enter> after each one
def main():
	print("This program calculates the sum of a set of numbers.")
	numOfNums = eval(input("Enter the number of numbers you will be entering."))
	print("Start entering numbers: ")
	total = 0
	for i in range(numOfNums, 0, -1):
		x = eval(input(""))
		total+=x
	print("The sum is", total, ".")
main()