# Tic-tac-toe


# Ask player 1 if they would like to be X or O -> store this info

# Randomly determine who will go first

# Display board

# Check if board is full -> Tie

# Ask player what space they want to pick

# Check if that space is available

# Mark the board

# Check for win -> declare winner

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
		if board[n] != 'X' and board[n] != 'O':
			return False
	return True



def move_is_valid(board, move):

	if board[move] == 'X' or board[move] == 'O':
		print('That space is already occupied\n')
	else:
		return True

	return False


def player_move(board, player):

	move = input(f'\nPlayer {player}, please choose a space (1 - 9)\n')

	try:
		move = int(move)
		if move >= 1 and move <= 9:
			return move
		else:
			print('Please choose a valid space\n')
			return 0
	except:
		print('Please choose a valid space\n')
		return 0

	return 0


def mark_board(board, move, mark):
	board[move] = mark
	print('\n')
	display_board(board)


def win_check(board, mark):
	row_check = [1, 2, 3]
	column_check = [1, 4, 7]

	# row check
	for index in row_check:
		if board[index] == mark and board[index + 3] == mark and board[index + 6] == mark:
			return True

	# column check
	for index in column_check:
		if board[index] == mark and board[index + 1] == mark and board[index + 2] == mark:
			return True

	# diagonal check
	if board[1] == mark and board[5] == mark and board[9] == mark:
		return True
	elif board[3] == mark and board[5] == mark and board[7] == mark:
		return True
	
	# no winner
	return False

def prompt_replay():

	while True:
		answer = input('Would you like to play again? (y/n)').upper()
		if answer == 'Y':
			return True
		elif answer == 'N':
			return False








def play(replay):

	# define board
	sample_board = ['#', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
	replay_game = replay
	game_over = False

	# ask if player 1 wants to be X or O and store it as a dict
	players = player_input()

	if replay_game != True:
		# display the rules
		display_rules(sample_board)

	# randomly determine who will go first
	current_player = randomize()

	# loop until the game is over
	while game_over == False:

		# record the move
		valid_move = False

		while valid_move == False:
			move = player_move(board, current_player)
			if move != 0:
				if move_is_valid(board, move) == True:
					valid_move = True

		# mark the board and check for winner
		if current_player == 1:
			mark_board(board, move, players['player_one'])
			if win_check(board, players['player_one']):
				print(f'\nPlayer {current_player} is the winner!\n')
				game_over = True
			else:
				current_player = 2
		else:
			mark_board(board, move, players['player_two'])
			if win_check(board, players['player_two']):
				print(f'\nPlayer {current_player} is the winner!\n')
				game_over = True
			else:
				current_player = 1

		# check to see if the board is full
		if board_is_full(board):
			print('\nTie game!\n')
			game_over = True
			break

	if prompt_replay() == True:
		play(True)



play(False)




