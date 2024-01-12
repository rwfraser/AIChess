import random

SuitsTuple = ('Spades','Hearts', 'Clubs', 'Diamonds')
RankTuple = ('Ace','2','3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King')
NCards = 8

def GetCard(DeckListIn):
	thisCard = DeckListIn.pop()
	return thisCard

def Shuffle(DeckListIn):
	DeckListOut = DeckListIn.copy()
	random.shuffle(DeckListOut)
	return DeckListOut

print('Welcome...')
print()

StartingDeckList = []
for suit in SuitsTuple:
	for thisValue, rank in enumerate(RankTuple):
		CardDict = {'rank':rank, 'suit':suit, 'value':thisValue+1}
		StartingDeckList.append(CardDict)

score = 50

while True:
	print()
	GameDeckList = Shuffle(StartingDeckList)
	CurrentCardDict = GetCard(GameDeckList)
	CurrentCardRank = CurrentCardDict['rank']
	CurrentCardValue = CurrentCardDict['value']
	CurrentCardSuit = CurrentCardDict['suit']
	print(f'First Card is: {CurrentCardRank} of {CurrentCardSuit}')
	print()

	for CardNumber in range(0,NCards):
		answer = input('Please Predict Higher or Lower (enter h or l)')
		answer = answer.casefold()
		NextCardDict = GetCard(GameDeckList)
		NextCardRank = NextCardDict['rank']
		NextCardSuit = NextCardDict['suit']
		NextCardValue = NextCardDict['value']
		print(f'Next Card Is: {NextCardRank} of  {NextCardSuit}')
		if answer == 'h':
			if NextCardValue > CurrentCardValue:
				score = score + 20
				print("Correct - it was higher")
			else:
				print("Sorry it was not higher")
				score = score - 15
		elif answer == 'l':
			if NextCardValue < CurrentCardValue:
				score = score + 20
				print("Correct - it was lower")
			else:
				score = score - 15
				print('Sorry, it was not lower')
		print('Your score is:', score)
		print()
		CurrentCardRank = NextCardRank
		CurrentCardValue = NextCardValue  
		CurrentCardSuit = NextCardSuit
	goAgain = input('To play again, press ENTER, or "q" to quit: ')
	if goAgain == 'q':
		break

print('OK bye')

