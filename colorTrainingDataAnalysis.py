# The purpose of this color training version is to create a dictionary that
# stores the reaction time of the user for each square. It will then take the
# reaction time data and suggest a tailored study plan based on the files the
# user is weakest in

from random import choice
from time import time, sleep
# from datetime import datetime
# import openpyxl
import matplotlib.pyplot as plt
import numpy as np

# Initializes the board
light = ('b1','d1','f1','h1','a2','c2','e2','g2','b3','d3','f3','h3','a4','c4','e4','g4',
		 'b5','d5','f5','h5','a6','c6','e6','g6','b7','d7','f7','h7','a8','c8','e8','g8')
dark = ('a1','c1','e1','g1','b2','d2','f2','h2','a3','c3','e3','g3','b4','d4','f4','h4',
		 'a5','c5','e5','g5','b6','d6','f6','h6','a7','c7','e7','g7','b8','d8','f8','h8')
board = dark + light

# Initializes the reaction time data dictionary
correct_reaction, incorrect_reaction = {}, {}
count = 0
for light_in, dark_in in zip(light,dark):
	if count%8<4:
		correct_reaction[dark_in], incorrect_reaction[dark_in] = [], []
		correct_reaction[light_in], incorrect_reaction[light_in] = [], []
	else:
		correct_reaction[light_in], incorrect_reaction[light_in] = [], []
		correct_reaction[dark_in], incorrect_reaction[dark_in] = [], []
	count+=1
	
# Asks the user how many squares they want to practice
while True:
	run = input('How many squares do you want to train? ')
	try:
		run = int(run)
		break
	except:
		print('That is not a valid amount of squares')
sleep(1)
print("Use 'l' to indicate light squares and 'd' to indicate dark squares")
sleep(1)
print("Begin")
sleep(1)

# Begings testing user
correct = 0
beginning = time()
for i in range(run):
	square = choice(board)								# Generates random square
	color = 'l' if square in light else 'd'				# Evaluates the correct color
	start = time()
	answer = input(square + ': ')						# Prompts user for answer
	if answer == color:
		stop = time()
		elapsed = stop - start							# Reaction time for square
		print('Correct')
		correct_reaction[square].append(elapsed)		# Updates correct scores
		correct+=1
	else:
		stop = time()
		elapsed = stop - start
		print('Incorrect')
		incorrect_reaction[square].append(elapsed)		# Updates incorrect scores
ending = time()

# End of training session
duration = ending-beginning
accuracy = round(correct/run,3)
per_question = round(duration/run,3)
sleep(0.5)
print('Training complete.')
sleep(1)
print(f'Your score was {correct} out of {run} or {round(accuracy*100,1)}%')
sleep(1)
print(f'Your average speed was {per_question} seconds per square')

# Dictionaries for file insight
total_time_correct =  {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0}
total_time_incorrect = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0}
total_squares_correct = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0}
total_squares_incorrect = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0}
average_time_correct = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0}
average_time_incorrect = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0}

# Dictionary for square color insight
color_reaction = {'light':{'time':{'correct':0,'incorrect':0},'count':{'correct':0,'incorrect':0}},
				  'dark':{'time':{'correct':0,'incorrect':0},'count':{'correct':0,'incorrect':0}}}

# Updates dictionaries with training data
for s,t in correct_reaction.items():
	total_time_correct[s[0]] += sum(t)
	total_squares_correct[s[0]] += len(t)
	if s in light:
		color_reaction['light']['time']['correct']+=sum(t)
		color_reaction['light']['count']['correct'] += len(t)
	else:
		color_reaction['dark']['time']['correct']+=sum(t)
		color_reaction['dark']['count']['correct']+= len(t)
for s,t in incorrect_reaction.items():
	total_time_incorrect[s[0]] += sum(t)
	total_squares_incorrect[s[0]] += len(t)
	if s in light:
		color_reaction['light']['time']['incorrect']+=sum(t)
		color_reaction['light']['count']['incorrect'] += len(t)
	else:
		color_reaction['dark']['time']['incorrect']+=sum(t)
		color_reaction['dark']['count']['incorrect'] += len(t)


# # Debugging
# print(f'Total squares correct: \n {total_squares_correct}')
# print('')
# print(f'Total squares incorrect: \n {total_squares_incorrect}')
# print('')

# print(f'Total time correct: \n {total_time_correct}')
# print('')
# print(f'Total time incorrect: \n {total_time_incorrect}')
# print('')

# print(f'Color reaction: {color_reaction}')
# print('')

# Calculates the average time per answer grouped by file
for [ttk,ttv],[tlk,tlv],[atk,atv] in zip(total_time_correct.items(),total_squares_correct.items(),average_time_correct.items()):
	try:
		average_time_correct[atk] = ttv/tlv
	except ZeroDivisionError:
		average_time_correct[atk] = 0
for [ttk,ttv],[tlk,tlv],[atk,atv] in zip(total_time_incorrect.items(),total_squares_incorrect.items(),average_time_incorrect.items()):
	try:
		average_time_incorrect[atk] = ttv/tlv
	except:
		average_time_incorrect[atk] = 0

# Calculates the average time per answer grouped by square color
color_avg_time_correct = {'light':color_reaction['light']['time']['correct']/color_reaction['light']['count']['correct'],
						  'dark':color_reaction['dark']['time']['correct']/color_reaction['dark']['count']['correct']}
color_avg_time_incorrect = {'light':color_reaction['light']['time']['incorrect']/color_reaction['light']['count']['incorrect'],
						  'dark':color_reaction['dark']['time']['incorrect']/color_reaction['dark']['count']['incorrect']}

print("****************")
print(f'Color avg time correct: \n {color_avg_time_correct}')
print('')
print(f'Color avg time incorrect: \n {color_avg_time_incorrect}')

correct_list = [value for value in average_time_correct.values()]
incorrect_list = [value for value in average_time_incorrect.values()]
color_correct_list = [value for value in color_avg_time_correct.values()]
color_incorrect_list = [value for value in color_avg_time_incorrect.values()]

# Displays the data
columns = ['a','b','c','d','e','f','g','h']
colors = ['light','dark']
x_f = np.arange(len(columns))
x_c = np.arange(len(colors))
width = 0.35

# Plots results by file
plt.figure('Files')
plt.bar(x_f - width/2, correct_list, width, label='Corect')
plt.bar(x_f + width/2, incorrect_list, width, label='Incorrect')
plt.xlabel('Column')
plt.ylabel('Reaction Time')
plt.title('Average Reaction Time by File')
plt.xticks(x_f, columns)
plt.grid(True)
plt.legend()

# Plots results by color
plt.figure('Colors')
plt.bar(x_c - width/2, color_correct_list, width, label='Corect')
plt.bar(x_c + width/2, color_incorrect_list, width, label='Incorrect')
plt.xlabel('Color')
plt.ylabel('Reaction Time')
plt.title('Average Reaction Time by Color')
plt.xticks(x_c, colors)
plt.grid(True)
plt.legend()
plt.show()
