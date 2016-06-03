# harrison frahn
# period 2 
# chapter 3.7
# expected input: an integer
# fibonomial algorithm : Knott, Ron (2013) The Fibonomials (version 1.0) [Article] 
# Availible at http://www.maths.surrey.ac.uk/hosted-sites/R.Knott/Fibonacci/Fibonomials.html (Accessed 8 September 2015)
# printing a list without brackets: http://stackoverflow.com/questions/13207697/how-to-remove-square-brackets-from-list-in-python
def fibFact(n):
	a,b,c = 1,1,1
	for i in range(n-1):
		a,b = b,b+a
		c *= a
	return c
def fibonomial(n, k):
	a = fibFact(n)/(fibFact(k)*fibFact(n-k))
	return int(a)
def main():
	print("This program prints the Fibonacci Coefficient Triangle.")
	rows = eval(input("Enter the number of rows to print: "))
	for n in range(rows):
		row = []
		for k in range(n+1):
			row.append(fibonomial(n,k))
		print(','.join(map(str, row)))
main()