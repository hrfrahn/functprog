#avg2.py
def main():
	print("Enter 5 exam scores to be averaged:")
	score1 = eval(input("1:"))
	score2 = eval(input("2:"))
	score3 = eval(input("3:"))
	score4 = eval(input("4:"))
	score5 = eval(input("5:"))
	total = score5 + score4 + score3 + score2 + score1
	print("The average is ", total/5, ".")
main()