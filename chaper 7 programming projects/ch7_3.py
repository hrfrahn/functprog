# harrison frahn
# period 2
# chapter 7.2
# expected input: how many minutes the call is
def main():
	mins = eval(input("How long is the call to Lexington, Virginia?(minutes): "))
	print("Cost: $"+str(1.15+(mins-2)/2))
if __name__ == '__main__':
	main()