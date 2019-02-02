import random

#Create a Board
board = []

for x in range(10):
	board.append(['O'] * 10)

#Format Board
def printBoard(board):
	for row in board:
		print(" ".join(row))

#Display Board
printBoard(board)

#Define Random Selection
def rand_col(board):
	return random.randint(0, len(board) - 1)

def rand_row(board):
	return random.randint(0, len(board) - 1)

#Define Ship Position
shipRow = rand_row(board)
shipCol = rand_col(board)

print("Dev Row: ", shipRow)
print("Dev Col: ", shipCol)

for turn in range(20):
	print("Turn: ", turn + 1)