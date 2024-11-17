# This is my first draft of an app that will allow me to practice identifying the
# square colors on a chess board. For reference, the bottom right corner of a 
# chess board is always light and the bottom left is always dark

from random import randint

# Instantiates the table
light = ('b1','d1','f1','h1','a2','c2','e2','g2','b3','d3','f3','h3','a4','c4','e4','g4',
		 'b5','d5','f5','h5','a6','c6','e6','g6','b7','d7','f7','h7','a8','c8','e8','g8')
dark = ('a1','c1','e1','g1','b2','d2','f2','h2','a3','c3','e3','g3','b4','d4','f4','h4',
		 'a5','c5','e5','g5','b6','d6','f6','h6','a7','c7','e7','g7','b8','d8','f8','h8')
board = dark + light

# Asks the user how many squares they want to practice
while True:
	run = input('How many squares do you want to train? ')
	try:
		run = int(run)
		break
	except:
		print('That is not a valid amount of squares')


# Tests the user on the amount of squares they requested
correct = 0
for i in range(run):
	square = board[randint(0,63)]		# Generates a random square
	if square in light:
		color = 'light'
	else:
		color = 'dark'
	answer = input(square + ': ')		# Tests the user
	if answer == color:					# Checks for accuracy
		print('Correct!')
		correct += 1
	else:
		print('Incorrect')

# End of training session
accuracy = correct/run
print(f'Training complete. Your score was {correct} out of {run} or {accuracy*100}%')