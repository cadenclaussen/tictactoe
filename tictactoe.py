import random

def main():
	board = [[".", ".", "."], [".", ".", "."], [".", ".", "."]]
	beadsPlayed = 0
	currentPlayer, names, token = getPlayerNames()
	while winner == False:
		move = getMove()
		winner = anylizeMove(move, currentPlayer, token, board)
		for row in range(3):
			print(board[row])
		currentPlayer, token = nextPlayer(currentPlayer, token, names)

def getPlayerNames():
	names = []
	names.append(input("What is your name p1? "))
	names.append(input("What is your name p2? "))
	return random.choice(names), names, "X"

def getMove(currentPlayer):
	return input("What is your move " + currentPlayer + "? (1 1), (2 1)").split()

def anylizeMove(move, token, board):
	board[move[0]][move[1]] = token
	for row in range(3):
		for col in range(3):
			if board[row][col] == ".":
				return False
	if board[0][0] == token and board[0][1] == token and board[0][2] == token:
		return True
	if board[1][0] == token and board[1][1] == token and board[1][2] == token:
		return True
	if board[2][0] == token and board[2][1] == token and board[2][2] == token:
		return True
	if board[0][0] == token and board[1][1] == token and board[2][2] == token:
		return True
	if board[0][2] == token and board[1][1] == token and board[2][0] == token:
		return True
	if board[0][0] == token and board[1][0] == token and board[2][0] == token:
		return True
	if board[0][1] == token and board[1][1] == token and board[2][1] == token:
		return True
	if board[0][2] == token and board[1][2] == token and board[2][2] == token:
		return True

	for row in range(3):
		for col in range(3):
			if board[row][col] == ".":
				return False
	
def nextPlayer(currentPlayer, token, names):
	if currentPlayer == names[0]:
		currentPlayer = names[1]
		if token == "X":
			return currentPlayer, "O"
		else:
			return currentPlayer, "X"

	if currentPlayer == names[1]:
		currentPlayer = names[0]
		if token == "X":
			return currentPlayer, "O"
		else:
			return currentPlayer, "X"

