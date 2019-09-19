# Tic-tac-toe


# Ask player 1 if they would like to be X or O -> store this info

# Randomly determine who will go first

# Display board

# Check if board is full -> Tie

# Ask player what space they want to pick

# Check if that space is available

# Mark the board

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


def display_rules(board):

	print('-'*20 + '\n')
	print('Here is a sample board:\n')
	display_board(board)
	print("Each player will take turns choosing a space\nthat corresponds to the numbers above.\n\nLet's begin!\n")
	print('-'*20 + '\n')


def board_is_full(board):

	index = range(1, 10)

	for n in index:
		if board[n] != 'X' or board[n] != 'O':
			return False
	return True



def move_is_valid(board, move):

	if board[move] == 'X' or board[move] == 'O':
		print('\nThat space is already occupied\n')
	else:
		return True


def player_move(board, player):

	move = input(f'\nPlayer {player}, please choose a space (1 - 9)\n')

	try:
		move = int(move)
		if move >= 1 and move <= 9:
			if move_is_valid(board, move) == True:
				return move
			else: 
				player_move(board, player)
		else:
			print('Please choose a valid space\n')
			player_move(player)
	except:
		print('Please choose a valid space\n')
		player_move(board, player)




def play():

	# define board
	board = ['#', 'X', '2', '3', '4', '5', '6', '7', '8', '9']
	game_over = False

	# ask if player 1 wants to be X or O and store it as a dict
	players = player_input()

	# display the rules
	display_rules(board)

	# randomly determine who will go first
	current_player = randomize()

	# loop until the game is over
	while game_over == False:

		#check to see if the board is full
		if board_is_full(board):
			print('\nGame over\n')
			break

		# record the move
		move = player_move(board, current_player)

		# testing - to be removed
		game_over = True











play()




