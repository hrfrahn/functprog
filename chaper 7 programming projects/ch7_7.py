# harrison frahn
# period 2
# chapter 7.7
# expected input: the length, width, and height of a rectangular prism
# from graphics import *
# ADD THE GRAPHICS STUFF
def calcVol(l,w,h):
	if l <=0 or w <=0 or h <= 0:
		raise RuntimeError()
	return l*w*h
def getDiff(num):
	diff = 0.5
	diffStr = "0.05"
	num = str(float(num))
	numlist = num.split(".")
	decimals = str(numlist[1])
	if decimals != '0':
		for i in range(len(decimals)):
			diff += float(diffStr)
			diffStr = str(float(diffStr)*10)
			diff -= float(diffStr)
			diffStr = str(float(diffStr)/100)
	return round(diff,len(diffStr))
def main():
	print("This program calculates the percent error of the volume of a rectangular prism.")
	try:
		l,w,h = eval(input("Please enter the length, width, and height, separated by commas: "))
		orginalVol = calcVol(l,w,h)
		smallVol = calcVol(l-getDiff(l),w-getDiff(w),h-getDiff(h))
		bigVol = calcVol(l+getDiff(l),w+getDiff(w),h+getDiff(h))
		error0 = abs((smallVol-orginalVol)/orginalVol)*100
		error1 = abs((bigVol-orginalVol)/orginalVol)*100
		print(error0,error1)
		if error0<error1:
			error = error1
		else:
			error = error0
		print("Actual Volume:",orginalVol)
		print("Smallest Possible Volume:",smallVol)
		print("Largest Possible Volume:",bigVol)
		print("Error: {0:0.2f}%.".format(error))
	except SyntaxError:
		print("Either you didn't enter any numbers, or you entered the numbers wrong!")
	except NameError:
		print("You entered letters, not numbers!")
	except ValueError:
		print("You didn't enter 3 numbers!")
	except TypeError:
		print("You only entered 1 number!")
	except RuntimeError:
		print("You can't have a side length of 0 or less!")
	except KeyboardInterrupt and EOFError:
		print("")
	except:
		print("Something went wrong!")
if __name__ == '__main__':
	main()