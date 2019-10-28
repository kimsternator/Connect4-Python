class connect4:
	def __init__(self):
		print("Let's play Connect4")

	def createBoard(self):
		board = [[0]*7 for i in range(6)]
		return board

	def printBoard(self, board):
		for i in range(6):
			print("-----------------------------")
			for j in range(7):
				print("| {0} ".format(board[i][j]), end="")
			print("|")

		print("--1---2---3---4---5---6---7--")
	def goFirst(self):
		first = input("Do you want to go first? (Y/N)\n")
		if first == "Y" or first == 'y':
			first = 0
		else:
			first = 1
		return first

	def twoPlayer(self):
		player = input("Do you want to play against the computer? (Y/N)\n")
		if player == "y" or player == "Y":
			return False
		else:
			return True

	def checkWinner(self, board, row, column):
		if row >= 3 and column <= 3:
			if board[row][column] == board[row - 1][column + 1] == board[row - 2][column + 2] == board[row - 3][column + 3]:
				return True
		if 2 <= row <= 4 and 1 <= column <= 4:
			if board[row][column] == board[row - 1][column + 1] == board[row - 2][column + 2] == board[row + 1][column - 1]:
				return True
		if 1 <= row <= 3 and 2 <= column <= 5:
			if board[row][column] == board[row - 1][column + 1] == board[row + 1][column - 1] == board[row + 2][column - 2]:
				return True
		if row <= 2 and 3 <= column:
			if board[row][column] == board[row + 1][column - 1] == board[row + 2][column - 2] == board[row + 3][column - 3]:
				return True
		if row >= 3 and column >= 3:
			if board[row][column] == board[row - 1][column - 1] == board[row - 2][column - 2] == board[row - 3][column - 3]:
				return True
		if 2 <= row <= 4 and 2 <= column <= 5:
			if board[row][column] == board[row - 1][column - 1] == board[row - 2][column - 2] == board[row + 1][column + 1]:
				return True
		if 1 <= row <= 3 and 1 <= column <= 4:
			if board[row][column] == board[row - 1][column - 1] == board[row + 1][column + 1] == board[row + 2][column + 2]:
				return True
		if row <= 2 and column <= 3:
			if board[row][column] == board[row + 1][column + 1] == board[row + 2][column + 2] == board[row + 3][column + 3]:
				return True
		if column <= 3:
			if board[row][column] == board[row][column + 1] == board[row][column + 2] == board[row][column + 3]:
				return True
		if 1 <= column <= 2:
			if board[row][column] == board[row][column + 1] == board[row][column + 2] == board[row][column - 1]:
				return True
		if 2 <= column <= 1:
			if board[row][column] == board[row][column + 1] == board[row][column - 1] == board[row][column - 2]:
				return True
		if 3 <= column:
			if board[row][column] == board[row][column - 1] == board[row][column - 2] == board[row][column - 3]:
				return True
		if row <= 2:
			if board[row][column] == board[row + 1][column] == board[row + 2][column] == board[row + 3][column]:
				return True
		return False

	def playerMove(self, board, player):
		a = 0
		spot = 5
		done = False
		while not done:
			a = int(input("Enter your move:\n"))
			for i in range(6):
				if board[i][a - 1] != 0:
					spot -= 1
			if spot < 6:
				done = True
			else:
				print("Cannot move there.\nTry Again")
		self.drop(board, spot, a - 1, player)
		return self.checkWinner(board, spot, a - 1)

	#def compMove(self, board):

	def drop(self, board, row, column, player):
		board[row][column] = player

	def play(self):
		board = self.createBoard()
		self.printBoard(board)
		twoPlay = self.twoPlayer()
		first = self.goFirst() #0 if player goes first, 1 if comp goes first
		finish = False
		winner = 0
		move = 1
		while not finish:
			if move % 2 != first:
				print("Player X")
				finish = self.playerMove(board, "X")
				move += 1
			else:
				if twoPlay:
					print("Player O")
					finish = self.playerMove(board, "O")
					move += 1
				else:
					finish = True
					#self.compMove(board)
					move += 1
			self.printBoard(board)
		print("Game Over!\nThanks for playing! <3")
