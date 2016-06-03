#harrison frahn
#period 2
#project 3.2
#expected input: estimated number of tacos sold, toppings, distance the truck traveled
def main():
	print("This program calculates the cost of having Rocko's Ice Cream Tacos at a party.")
	tacos, toppings, distance = eval(input("Enter the estimated number of tacos that will be sold, the estimated number of extra toppings, and then the distance(in miles) your house is from Rocko's, separated by a comma: "))
	tacocost = tacos * 3.75 + 0.5 * toppings
	travelcost = 20+distance*0.5
	total = tacocost + travelcost
	print("The total cost is $",total,".")
main()