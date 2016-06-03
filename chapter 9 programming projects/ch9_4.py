# Harrison Frahn
# period 2
# chapter 9.4
# expected input: your throw, and then whether to play again.
from random import randrange
def getThrow():
	a = randrange(0,5)
	throws = ['rock','paper','scissors','lizard','spock']
	return throws[a]
def main():
	again = True
	pScore, cScore = 0,0
	print("This program simulates a game of rock-paper-scissors-lizard-spock.")
	while again:
		won = 'N'
		throw = input("What is your throw?(Rock,Paper,Scissors,Lizard, or Spock): ")
		compThrow = getThrow()
		if compThrow == throw.lower():
			print("You tied! You both threw",compThrow)
		else:
			if throw.lower() == 'rock':
				if compThrow == 'lizard' or compThrow == 'scissors':
					won = 'p'
				elif compThrow == 'spock' or compThrow == 'paper':
					won = 'c'
			elif throw.lower() == 'scissors':
				if compThrow == 'lizard' or compThrow == 'paper':
					won = 'p'
				elif compThrow == 'spock' or compThrow == 'rock':
					won = 'c'
			elif throw.lower() == 'paper':
				if compThrow == 'spock' or compThrow == 'rock':
					won = 'p'
				elif compThrow == 'scissors' or compThrow == 'lizard':
					won = 'c'
			elif throw.lower() == 'lizard':
				if compThrow == 'spock' or compThrow == 'paper':
					won = 'p'
				elif compThrow == 'scissors' or compThrow == 'rock':
					won = 'c'
			elif throw.lower() == 'spock':
				if compThrow == 'scissors' or compThrow == 'rock':
					won = 'p'
				elif compThrow == 'lizard' or compThrow == 'paper':
					won = 'c'
			else:
				raise RuntimeError("You Didn't enter rock,paper,scissors,lizard,or spock!")
			if won =='c':
				print("You Lost!",compThrow.capitalize(),"beats",throw.capitalize(),".")
				cScore += 1
			elif won =='p':
				print("You Won!",throw.capitalize(),"beats",compThrow.capitalize(),".")
				pScore += 1
		print("Score:\nComputer:",cScore,"\nPlayer: ",pScore)
		a = input("Do you want to play again? Enter y or n: ")
		if a.lower() == 'y':
			pass
		elif a.lower() == 'n':
			break
		else:
			raise RuntimeError("You didn't enter y or n!")
	print("Final Score:\nComputer:",cScore,"Player:",pScore)
if __name__=='__main__':
	main()
