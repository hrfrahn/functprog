# harrison frahn
# period 2
# chapter 6.3
# expected input: the name of an animal
def print_verse(animal,bingo):
	print("There was a farmer, had a "+animal+"\nand Bingo was his name-o.")
	for i in range(3):
		for i in range(5):
			print(bingo[i],end="")
		print("")
	print("And Bingo was his name-o.")
def main():
	animal = input("Enter what kind of animal Bingo is: ")
	bingo = ['B','I','N','G','O',' ']
	for i in range(6):
		print_verse(animal,bingo)
		bingo[i]='(clap)'
main()