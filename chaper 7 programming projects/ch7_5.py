# harrison frahn
# period 2
# chapter 7.5
# expected input: the number of how many bags were filled (an integer)
def main():
	try:
		bags = eval(input("Enter the number of bags of litter filled: "))
		if bags%1==0 and bags > 0:
			fine = 75+bags*10
			if bags > 10:
				fine += 500
			print("Your fine is "+str(fine)+'.')
		elif bags <= 0:
			print("You can't fill negative bags!")
		elif bags%1!=0:
			print("You can't fill a fraction of a bag!")
	except NameError:
		print("You entered letters, not a number!")
	except SyntaxError:
		print("Either you didn't enter any number, or you entered the number wrong!") 
	except TypeError:
		print("You entered more than 1 number!")
	except KeyboardInterrupt:
		print("\n")
	except:
		print("Something went wrong!!")
if __name__ == '__main__':
	main()
