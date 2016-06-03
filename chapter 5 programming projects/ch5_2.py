# harrison frahn
# period 2
# chapter 5.2
# expected input: a number from 0-100
def getGrade(score):
	if score <= 100 and score >= 88:
		return 'A'
	if score <= 88 and score >= 77:
		return 'B'
	if score <= 77 and score >= 66:
		return 'C'
	if score <= 66 and score >= 55:
		return 'D'
	if score <= 55 and score >= 0:
		return 'F'
def main():
	score = eval(input("Please enter the score out of 100:"))
	if score > 100 or score < 0:
		score = eval(input("Please enter the score out of 100:"))
	grade = getGrade(score)
	print('Grade:',grade)
main()