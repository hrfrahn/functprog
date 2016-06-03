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
	try:
		a,b,c=eval(input("Enter the 3 side lengths, separated by commas: "))
		if isRight(a,b,c) == True:
			print("The triangle is right.")
		else:
			print("The triangle is not right.")
	except NameError:
		print("You entered letters, not numbers!")
	except SyntaxError:
		print("Either you didn't enter any numbers, or you entered the numbers wrong! Remember to separate them with commas.") 
	except ValueError:
		print("You didn't enter 3 numbers!")
	except TypeError:
		print("You only entered 1 number!")
	except KeyboardInterrupt:
		print('\n')
	except: 
		print("Something went wrong!")
if __name__ == '__main__':
	main()