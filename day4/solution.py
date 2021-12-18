with open("input.txt") as file:
	lines = file.read().splitlines()

numbers = lines.pop(0).split(",")
lines.pop(0)

boards = []
board = []

for i in range(len(lines)):
	if lines[i] == '':
		continue

	if i % 6 == 0 and len(board) > 0:
		boards.append(board.copy())
		board.clear()
	
	board.append(lines[i].split())
boards.append(board.copy())


def replace_number(number, board):
	for i in range(len(board)):
		for j in range(len(board[0])):
			if number == board[i][j]:
				board[i][j] = -1

def check_line(line):
	for nr in line:
		if nr != -1:
			return False
	return True

def check_board(board):
	for line in board:
		if check_line(line):
			return True

	board = [*zip(*board)]
	for line in board:
		if check_line(line):
			return True

def calculate_sum(board):
	sum = 0
	for line in board:
		for nr in line:
			if int(nr) > 0:
				sum += int(nr)

	return sum

sum = 0
final_nr = 0
for number in numbers:
	bingo = False
	for i in range(len(boards)):
		replace_number(number, boards[i])
		if check_board(boards[i].copy()):
			print(board)
			print(number)
			bingo = True
			sum = calculate_sum(boards[i])
			final_nr = int(number)
			break
	if bingo:
		break

print(sum * final_nr)
