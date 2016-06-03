# harrison frahn
# period 2
# chapter 7.2
# expected input: how many minutes the call is
from math import ceil
def main():
	try:
		mins = eval(input("How long is the call to Lexington, Virginia?(minutes): "))
		cost = 1.15
		if mins < 0:
			raise ValueError
		mins = ceil(mins)
		if mins > 2: 
			for i in range(mins-2):
				cost += 0.5
		print("Cost: $"+str(cost))
	except ValueError:
		print("You can't have a call that last negative minutes!")
	except NameError:
	 	print("You entered letters, not a number!")
	except SyntaxError:
	 	print("Either you didn't enter a number, or you entered the number wrong!") 
	except TypeError:
	 	print("You entered more than 1 number!")
	except KeyboardInterrupt:
	 	print("\n")
	except:
		print("Something went wrong!!")
if __name__ == '__main__':
	main()