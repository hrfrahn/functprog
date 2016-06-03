#harrison frahn
#period 2
#ch5.1
# expected input:an integer
def main():
    score = eval(input("enter the score out of 13:"))
    grades = ['F','D-','D','D+','C-','C','C+','B-','B','B+','A-','A','A+']
    grade = grades[score-1]
    print("Grade:",grade)
main()
