# -*- coding: utf-8 -*-

from random import randint

ROCK = 0
PAPER = 1
SCISSORS = 2

StringValues = ( 'Rock', 'Paper', 'Scissors' )

def compare ( a, b ):
	if a == b:
		return 0
	elif a == ROCK and b == PAPER:
		return -1
	elif a == PAPER and b == SCISSORS:
		return -1
	elif a == SCISSORS and b == ROCK:
		return -1
	return 1

def main ():

	print "Rock, Paper, Scissors"
	print

	while True:

		choice = None
		while choice == None:
			option = raw_input( "1,2,3 Shoot! [Rock, Paper, Scissors] " )
			if "rock" == option.lower():
				choice = ROCK
			elif "paper" == option.lower():
				choice = PAPER
			elif "scissors" == option.lower():
				choice = SCISSORS
			else:
				print "You can't pick %s!" % option
				print
				continue
			break

		computer_choice = randint( 0, 2 )

		print
		print "     You Chose : %s" % StringValues[choice]
		print "Computer Chose : %s" % StringValues[computer_choice]
		print

		winner = compare( choice, computer_choice )

		if 1 == winner:
			print "You Win!"
		elif -1 == winner:
			print "You Lose!"
		else:
			print "Tie!"

		print
		option = raw_input( "Pay Again? [Y/n] " )
		if 'n' == option.lower():
			break
		print

if __name__ == "__main__":
	main()