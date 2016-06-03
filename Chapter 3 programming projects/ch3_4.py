# harrison frahn
# period 2
# project 3.4
# expected input: a 4-digit year
def main():
	print("This program calculates the gregorian epact.")
	year = eval(input("Please enter a four-digit year to calculate the epact of: "))
	C = year//100
	epact = (8 + (C//4) - C + ((8*C + 13)//25) + 11*(year % 19))%30
	print("The epact is", epact)
main()