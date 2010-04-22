# -*- coding: utf-8 -*-

import random

print "Guess The Number!"
print "----"

print "I can guess a number between 1 and any number you give me."

while True:
	try:
		number = raw_input( "What's the highest number I should pick? " )
		number = int( number )
		break
	except ValueError, e:
		print "\"%s\" isn't a number!" % number

print "Ok, I will guess a number between 1 and", number

computer_number =  random.randint( 0, number )

winner = False

while winner == False:
	while True:
		try:
			guess = raw_input( "Ok, guess the number! " )
			guess = int( guess )
			break
		except ValueError, e:
			print "\"%s\" isn't a number!" % guess
	if guess == computer_number:
		print "You got it!"
		winner = True
	else:
		if guess < computer_number:
			print "Too low. Try again!"
		else:
			print "Too high. Try again!"

