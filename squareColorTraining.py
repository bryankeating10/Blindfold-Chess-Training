# This is my first draft of an app that will allow me to practice identifying the
# square colors on a chess board. For reference, the bottom right corner of a 
# chess board is always light and the bottom left is always dark

from random import randint
from time import time, sleep

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
		sleep(1)
		print("Use 'l' to indicate light squares and 'd' to indicate dark squares")
		sleep(1)
		print("Begin")
		sleep(1)
		break
	except:
		print('That is not a valid amount of squares')


# Tests the user on the amount of squares they requested
start = time()
correct = 0

# Debugging
light_count = 0
dark_count = 0

for i in range(run):
	square = board[randint(0,63)]		# Generates a random square
	if square in light:
		color = 'l'
		light_count += 1
	else:
		color = 'd'
		dark_count += 1
	answer = input(square + ': ')		# Tests the user
	if answer == color:					# Checks for accuracy
		print('Correct!')
		correct += 1
	else:
		print('Incorrect')

# End of training session
stop = time()
duration = stop-start
accuracy = correct/run
per_question = round(duration/run,3)
sleep(1)
print('Training complete.')
sleep(1)
print(f'Your score was {correct} out of {run} or {accuracy*100}%')
sleep(1)
print(f'Your average speed was {per_question} seconds per square')

# Debugging
sleep(1)
print(f'Light count: {light_count}, Dark count: {dark_count}')
