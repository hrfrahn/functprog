def main():
	print("This program calculates the future value of an investment.")
	years = eval(input("Enter the number of years for the investment:"))
	principle = eval(input("Enter the priciple of the investment:"))
	apr = eval(input("Enter the annual interest rate:"))
	for i in range(years):
		principle = principle * (1+apr)
	print("The value in", years, "years is", principle, ".")
main()