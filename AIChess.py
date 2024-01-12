# A chess playing program that makes random moves.  
#  upgrade will use AI to generate moves

class ChessBoard():
	'Creates list of the 64 squares. Stored in list Board '
	def __init__(self):
		Files = ('a','b','c','d','e','f','g','h')
		Ranks = ('1','2','3','4','5','6','7','8')
		BlackSquare = True
		Board = []
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
		for squares in Board:
			if 'white' is in Board[squares]:
				WhiteSquares.append(Board[squares])
			else:
				BlackSquares.append(Board[squares])


class ChessMen(self):
	'Prototype class for all pieces and pawns'
	def __init__(self):
		pass 

	def move(CurrentLocation):
		'prototype class for chessmen moves - override for each pawn/piece'
		default = CurrentLocation + 1

		def MayBeBlocked(self):
			pass 

		def MayCapture(self):
			pass 

		def DoesCastle(self):
			pass 

		def DoesEnPassant(self):
			pass 

		def MayPromote(self):
			pass 

		def MayCheck(self):
			pass

	def Status(self):
		IsFirstMove = True 
		IsOnRank7 = False
		CanDoEnPassant = False
		IsInCheck = False
		CanCastleKingSide = False
		CanCastleQueenSide = False




	def ChessMenStatus(self):
		'Prototype for tracking status by piece/pawn i.e. hasmoved() isonRank7() etc.'
		def __init__(self):
			pass 

		def hasmoved(self):
			HasMoved = True 
			return HasMoved

		def MayCastle(self):
			MayCastle = True
			return MayCastle

		def HasCastled(self):
			HasCastled = True 
			return HasCastled

		def OnRank7(self):
			OnRank7 = True 
			return OnRank7

	def GameStatus(self):
		' track drawcounts, checks, stalemate, checkmate, insufficient material'
		def __init__(self):
			pass 

		def IsCheck(self):
			IsCheck = True 
			return IsCheck

		def IsStaleMate(self):
			Stalemate = True 
			return Stalemate

		def DrawByThreeFoldRule(self):
			3FoldCount = 3FoldCount+1
			if 3FoldCount == 3:
				DrawByThreeFold = True
				return DrawByThreeFold
			else:
				DrawByThreeFold = False

		def DrawByFiftyMoveRule(self):
			DrawByFiftyMovesCount = DrawByFiftyMovesCount + 1
			if DrawByFiftyMovesCount == 50:
				DrawByFiftyMoves = True
				return DrawByFiftyMoves
			else:
				DrawByFiftyMovesCount = DrawByFiftyMovesCount + 1
				DrawByFiftyMoves =  False
				return DrawByFiftyMoves


		def IsCheckMate(self):
			if IsCheck() && not Move(King):
				IsCheckMate = True
				return IsCheckMate
			else:
				IsCheckMate = False
				return IsCheckMate




		

	def BoardDict(self): # use nested for loops to generate boardmatrix?

class AllPiecesByName(self):
	def __init__(self):
		WhitePieces = {'a1':'WLRook','h1':'WRRook','b1':'WLKnight','g1':'WRKnight', 'c1':'WBBishop','f1':'WWBishop',
			'd1':'WQueen','e1':'WKing'}
		WhitePawns = {'a2':'WP1','b2':'WP2','c2':'WP3','d2':'WP4','e2':'WP5','f2':'WP6', 'g2':'WP7','h2':'WP8'}
		BlackPieces = {'h8':'BLRook','a8':'BRRook','g8':'BLKnight','b8':'RBKnight', 'f8':'BBBishop','c8':'BWBishop',
			'd8':'BQueen','e8':'BKing'}
		BlackPawns = ('a7':'BP1','b7':'BP2','c7':'BP3','d7':'BP4','e7':'BP5','f7':'BP6', 'g7':'BP7','h7':'BP8')

		class AllPiecesByHomePosition(self):   # probably a bad idea as will not readily integrate with algebraic notation 
			pass 



		class WhiteChessMen(self):
			def __init__(self):
				# create all white pieces and pawns, and their capability

		class BlackChessMen(self):
			def __init__(self):
				# create all black pices and pawns



class GameStatus(self):
	def __init__(self):
		pass 

	def WhiteInCheck(self):
		pass

	def BlackInCheck(self):
		pass 

# to describe piece/pawn movements, convert algebraic notation to polar coordinates
def CurrentPositiontoCoordinates(CurrentPosition):
	x = int(CurrentPosition[1:2])
	y = ord(CurrentPosition[0:1]) - 96 # reduce ASCII to range 1-8
	return x, y

def CoordinatestoPosition(x,y):
	ConvertedY = chr(int(y)) + 96
	CurrentPosition = ConvertedY + str(x)
	return CurrentPosition 

class Pawn(ChessMen):
	def __init__(self):
		pass 

	def MoveTaxonomy(CurrentPosition):
		'''MoveTaxonomy is used to assist the move generator in iterating through all possible moves at 
		    any given position '''
		x, y = CurrentPositiontoCoordinates(CurrentPosition)
		default = [x+1, y]
		en_passant = [x+1, y+1]
		promotion = [x+1,y,die]
		capture[x+1,y+1]
		firstmove[x+2,0]

	def Status(self, EnPassantFlag, OnRank7Flag, FirstMoveFlag):
		def __init__(self):
			FirstMove = True
			OnRank7 = False
			CanPromote = False
			CanDoEnPassant = False
			CanCapture = False


		def MoveUpdate(self):
			CanDoEnPassant = EnPassantFlag
			OnRank7 = OnRank7Flag
			if OnRank7 and CanCapture or Rank8SameFile is Empty:
				CanPromote = True 
			else:
				CanPromote = False
			FirstMove = FirstMoveFlag




		OnRank7 = False
		CanDoEnPassant = EnPassantFlag

class Rook(ChessMen):
	def __init__(self):
		Move(CurrentPosition):
		x,y =CurrentPositiontoCoordinates(CurrentPosition)
		default = [x+BOARD_WIDTH-1, 0] or [0, y+BOARD_WIDTH-1]
		castleKingSide = [0,y-2]
		castleQueenSide = [0,y+3]

class Knight(ChessMen):



	def Status(self):





# setup a Class for game tokens, and sub class pawn and pieces
#  enumerate all legal moves and conditionals:
#  Pawn - forward one square, one or two squares on first move
#   capture opposing piece on either diagonal, may/must be queened
#   on last rank, en passant.  Track t/f for first move of each pawn. 
#   and t/f for move to last rank.  
def EvaluateMove(CurrentPosition, Token, Token_Status, Game_Status):
	# we know our current position, the piece/pawn we are working with
	#  its status (first move, check/no check) and game status (check/no check, move counter(s) in play, ) 
def legalmove(CurrentPosition):
	for tokens in CurrentPosition:
		# recursively evaluate each token's legal moves
		EvaluateMove(CurrentPosition, token) 
	# 
	return

def Pawn(Token):

if firstmove == True:
	pass
else:
	!en_passant
	!two_squares_forward



def King(Token):


def Status(check=False, )
def MyMove(Status):
	if Status == check: # evaluate only moves that remove check
		 
	else:  # enumerate all possible moves
		for token in tokens:
			movelist.append(legalmove)
			movelist.add()
		return movelist.random()

class initializeGameBoard(self): # GameBoard is a dict containing current position of all chessmen
	def __init__(self):
		GameBoard = ('')

class initializeGameStatus(self):
	def __init__(self):
		CheckMate = False
		StaleMate = False
		ThreeFoldDrawCount = 0 
		FiftyFoldDrawCount = 0 

class initializeChessMenStatus(self): #set moves to 0, all starting positions, all global illegal moves


class GetWhiteMove(currentBoardPosition, currentGameStatus, currentChessMenStatus):
	def __init__(self): # need methods for enumerating legal moves, enumerating status changes
		                # of game and chessmen, choosing a move, updating game and chessmen status  

	def legalmoves(currentBoardPosition):
		# significant code to iterate thru board position and generate List of all legal moves
		# include choosemove function to recieve a list of all moves and choose the 'best'
		# Conditions to test for on all moves:
		# is possible capture legal? 
		# will the move result in check from the opponent? i.e. illegal move
		# does the move cause draw by: stalemate, 3foldrule, 50moverule, insufficient material rule?
		# does the king move adjacent to opponents king? 
		# evaluate each non-routine move:  castlequeenside, castlekingside, enpassant, pawn promotion,
		#  pawnfirstmove, exposure to check by moving into or through check or exposing king to check
		# are we in check, if so evaluate the three possible ways to remedy: by capture (identify piece
		#  in question and evaluate if it can be captured, move the king to a safe square, shield the king
		#  with a pawn or another piece) 
		# are we in stalemate,  are we already in an (as yet undeclared) draw => this would apply to 
		# human players, as the computer will automatically detect and declare these conditions immediately
		# pawn promotion - move pawn to 8th rank and replace with knight, bishop (note color), rook, or queen
		#  identity piece as 3rd+ k,b,r or 2nd+ queen.  allow for up to 9 queens and 10 of k,b,r!
		# 


def main():
	currentBoardPosition = {}
	currentBoardPosition = initializeGameBoard()
	currentGameStatus = initializeGameStatus()
	currentChessMenStatus = initializeChessMenStatus()
	WhitesMove = True
	while not currentGameStatus.checkmate():
		if WhitesMove:
			WhiteMove = GetWhiteMove(currentBoardPosition, currentGameStatus, currentChessMenStatus)
			currentBoardPosition = currentBoardPosition(WhiteMove)
			currentGameStatus = 
































