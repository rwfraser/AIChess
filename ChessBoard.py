Files = ('a','b','c','d','e','f','g','h')
Ranks = ('1','2','3','4','5','6','7','8')
BlackSquare = True
Board = []
RankCount = 1
for rank  in Ranks:
	for file in Files:
		if BlackSquare:
			Square = 'Black' + file + rank
			Board.append(Square)
		else:
			Square = 'White' + file + rank
			Board.append(Square)
		BlackSquare = not BlackSquare
	BlackSquare = not BlackSquare
SquareQTY = len(Board)
print(f'Board has {SquareQTY} squares.  They are {Board}')