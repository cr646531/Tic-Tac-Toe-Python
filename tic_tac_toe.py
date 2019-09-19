# Tic-tac-toe


# Ask player 1 if they would like to be X or O -> store this info

# Randomly determine who will go first

# Display board

# Check if board is full -> Tie

# Ask player what space they want to pick

# Check if that space is available

# Check for win -> Display winning board -> declare winner

# Ask if they want to play again

def player_input():

	while True:
		result = input('Player 1, would you like to be X or O?\n').upper()
		if result == 'X':
			return {'player_one': 'X', 'player_two': 'O'}
		elif result == 'O':
			return {'player_one': 'O', 'player_two': 'X'}
		else:
			print('That is not a valid answer!\n')

def randomize():
	from random import randint

	return randint(1, 2)




def play():

	# define board
	board = ['#', '1', '2', '3', '4', '5', '6', '7', '8', '9']

	# ask if player 1 wants to be X or O and store it as a dict
	players = player_input()

	# randomly determine who will go first
	current_player = randomize()




