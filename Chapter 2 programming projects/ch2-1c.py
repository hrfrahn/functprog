def main():
	print("This program converts a celsius temperature to fahrenheit.")
	print("Celsius:     Fahrenheit:")
	spaces = '           '
	for c in range(-10, 55, 5):
		if c == -10:
			spaces = '          '
		elif c == 0:
			spaces += ' '
		elif c ==5:
			spaces += ' '
		print(c, end = '')
		print(spaces, end = '')
		f = 9/5 * c + 32
		print(f)
		spaces = '           '
main()
