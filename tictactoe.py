import random

def main():
	board = [[".", ".", "."], [".", ".", "."], [".", ".", "."]]
	beadsPlayed = 0
	currentPlayer, names, token = getPlayerNames()
	while winner == False:
		move = getMove()
		winner = anylizeMove(move, currentPlayer, token)
		currentPlayer, token = nextPlayer(currentPlayer, token, names)

def getPlayerNames():
	names = []
	names.append(input("What is your name p1? "))
	names.append(input("What is your name p2? "))
	return random.choice(names), names, "X"

def getMove(currentPlayer):
	return input("What is your move " + currentPlayer + "? (1 1), (2 1)").split()

def anylizeMove(move, currentPlayer, token):
	full = True
	
def nextPlayer(currentPlayer, token, names):
	if currentPlayer == names[0]:
		r

