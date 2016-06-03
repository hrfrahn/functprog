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
	try:
		a,b,c = eval(input("Enter the 3 side lengths, separated by commas: "))
		if isTriangle(a,b,c) == True:
			print("It is a triangle.")
		else: 
			print("It is not a triangle.")
	except NameError:
		print("You entered letters, not numbers!")
	except SyntaxError:
		print("Either you didn't enter any numbers, or you entered the numbers wrong! Remember to separate them with commas.") 
	except ValueError:
		print("You didn't enter 3 numbers!")
	except TypeError:
		print("You only entered 1 number!")
	except KeyboardInterrupt:
		print("\n")
	except:
		print("Something went wrong!!")
if __name__ == '__main__':
	main()