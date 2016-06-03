# harrison frahn
# period 2 
# chapter 11.1
# expected input: the size of the sqaure matrix, and then the elements
import statistics
def getMed(matrix,size):
    a = []
    for x in range(size):
        for y in range(size):
            a.append(matrix[x][y])
    return statistics.median(a)
def findMode(matrix,size):
    a = []
    for x in range(size):
        for y in range(size):
            a.append(matrix[x][y])
    try:
        return statistics.mode(a)
    except statistics.StatisticsError:
        return "Multiple Modes Present"
def main():
	print("This program demonstrates a square matrix.")
	matrix = []
	size = eval(input("How big should the square matrix be? Enter the side length: "))
	for i in range(size):
		matrix.append([])
	print("The matrix looks like this:")
	for i in range(size):
		print(matrix[i])
	for y in range(size):
		print("Enter row",y+1,"of the matrix.")
		for x in range(size):
			element = eval(input(""))
			matrix[y].append(element)
	edit = True
	while edit:
		a = input("Do you wish to edit the matrix?(y/n): ")
		if a.lower() == 'y':
			e = input("Which element do you wish to change?")
			if int(e[0])>size or int(e[1])> size:
				print("You entered an element that wasn't in the list!")
			else:
				matrix[int(e[0])-1][int(e[1])-1] = eval(input("Enter the new number: "))
			print("The matrix looks like this:")
			for i in range(size):
				print(matrix[i])
		elif a .lower() == 'n':
			break
		else:
			raise RuntimeError("You didn't enter y or n!")
	maxi = max(matrix[0])
	for i in range(size):
		maxi1 = max(matrix[i])
		if maxi1 > maxi:
			maxi = maxi1
	mini = min(matrix[0])
	for i in range(size):
		mini1 = min(matrix[i])
		if mini1 < mini:
			mini = mini1
	total = 0 
	for i in range(size):
		for x in range(size):
			total += matrix[i][x]
	total /= size**2
	print("The matrix looks like this:")
	for i in range(size):
		print(matrix[i])
	m = matrix
	print("Maximum      Minimum      Average      Median      Mode")
	print("-------------------------------------------------------")
	print("{0:7}      {1:7}      {2:7.2f}      {3:6}      {4:4}".format(maxi,mini,total,getMed(matrix,size),findMode(matrix,size)))
	if size == 2:
	    det = m[0][0]*m[1][1]-m[0][1]*m[1][0]
	    print("Determinant:",det)
	elif size == 3:
	    d1 = m[0][0]*(m[1][1]*m[2][2]-m[1][2]*m[2][1])
	    d2 = m[0][1]*(m[1][0]*m[2][2]-m[1][2]*m[2][0])
	    d3 = m[0][2]*(m[1][0]*m[2][1]-m[1][1]*m[2][0])
	    det = d1-d2+d3
	    print("Determinant:",det)
if __name__ == '__main__':
	main()