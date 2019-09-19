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
		result = input('Player 1, would you like to be X or O?').upper()
		if result == 'X':
			print('\nPlayer 1 is X\nPlayer 2 is O\n')
			return {'player_one': 'X', 'player_two': 'O'}
		elif result == 'O':
			print('\nPlayer 1 is O\nPlayer 2 is X\n')
			return {'player_one': 'O', 'player_two': 'X'}
		else:
			print('\nThat is not a valid answer!\n')


def randomize():
	from random import randint

	result = randint(1, 2)
	print(f'Player {result} goes first!\n')

	return randint(1, 2)


def display_board(board):

	index = 1

	while index < len(board):
		print(' {} | {} | {}'.format(board[index], board[index + 1], board[index + 2]))
		index += 3
		if index < len(board):
			print('-----------')

	print('\n')

    #  Sample Board

    #    1 | 2 | 3
    #   -----------
    #    4 | 5 | 6
    #   -----------
    #    7 | 8 | 9




def play():

	# define board
	board = ['#', '1', '2', '3', '4', '5', '6', '7', '8', '9']

	# ask if player 1 wants to be X or O and store it as a dict
	players = player_input()

	# display the sample board
	print('-'*20 + '\n')
	print('Here is a sample board:\n')
	display_board(board)
	print("Each player will take turns choosing a space\nthat corresponds to the numbers above.\n\nLet's begin!\n")
	print('-'*20 + '\n')

	# randomly determine who will go first
	current_player = randomize()



play()




