import random

def main():
	board = [[".", ".", "."], [".", ".", "."], [".", ".", "."]]
	names, token = getPlayerNames()

def getPlayerNames():
	names = []
	names.append(input("What is your name p1? "))
	names.append(input("What is your name p2? "))
	return random.choice(names), names, "X"

def getMove(currentPlayer)