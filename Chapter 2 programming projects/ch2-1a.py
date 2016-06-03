def main():
	print("This program converts a celsius temperature to fahrenheit.")
	for i in range(4):
	    c = eval(input("Enter a celsius temp to be converted:"))
	    f = 9/5 * c + 32
	    print("The temp is ", f, " degrees fahrenheit.")
main()
