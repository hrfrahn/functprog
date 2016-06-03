#this program converts meter to feet, or the reverse
def main():
	print('This program converts meters to feet, or the opposite.')
	x = input('Enter m for to convert meters to feet or f for the opposite: ')
	while x != 'f' and x != 'm':
		x = input('You didn\'t enter f or m! Please enter again: ')
	if x == 'm':
		y = eval(input('Enter a value in meters to be converted:')) 
		z = float(y) * 3.28084
		print(y, 'meters is ', z, 'feet')
	elif x == 'f':
		y = eval(input('Enter a value in feet to be converted:')) 
		z = float(y) / 3.28084
		print(y, ' feet is', z, 'meters.')
main()
