from inits import  *

class Max:

	def __init__(self,name="",location=0,isHuman=False):
		self.isHuman=isHuman
		self.cardsInHand=[]
		self.currentPlay=None
		self.has2Clubs=False
		self.hasQueenSpades=False
		self.isPlayHeart=False
		self.isQueenSpadesPlayed=False
		self.result=0
		self.allDeckResult=0
		self.name=name
		self.locationInPlayedCard=location
		self.result=0
		self.tmpResult=0
		self.notMyCards = []
		self.round = 13

	def addHand(self,card):
		self.cardsInHand.append(card)
		card.index=len(self.cardsInHand)-1
		if card.name==cardNumber.num2 and card.type==cardType.Clubs:
			self.has2Clubs=True
		if card.name==cardNumber.queen and card.type==cardType.Spades:
			self.hasQueenSpades=True

	def play(self,cardInGround,playedCard,Players):
		self.round -= 1
		lookAhead = self.lookAheadLookup()
		maxHand = []
		opponentHand = []
		for card in self.cardsInHand:
			if card.isPlayed != True:
				maxHand.append(card)
		for card in self.notMyCards:
			if card.isPlayed != True:
				opponentHand.append(card)
		for card in cardInGround:
			if card[0].type == cardType.Hearts:
				self.isPlayHeart = True
		node = None
		
		node = self.MaxTree(maxHand, opponentHand, [] if len(cardInGround) == 0 else [cardInGround[0][0]], MaxNode(None, (0,0,0,0), (26,26,26,26), 0), lookAhead, [20000], self.isPlayHeart)
		retcard = None
		for child in node.childNodes:
			if child.valueTaken == node.valueTaken:
				retcard = child.cardPlayed
				break

		if retcard.type == cardType.Hearts:
			self.isPlayHeart == True

		return self.setAsPlay(retcard)

	def lookAheadLookup(self):
		if self.round > 7:
			return 4
		else:
			return 5

	def setAsPlay(self,card):
		card.isPlayed=True
		if card.name==cardNumber.queen and cardType.Spades==card.type:
			self.hasQueenSpades=False
		return card

	def playAgain(self):
		self.cardsInHand=[]
			
	def getCard(self,index):        
		return self.cardsInHand[index]

	def moveCard(self,index,x,y):
		self.cardsInHand[index].moveCard(x,y)
				
	def showCard(self,index,screen):
		background=self.getCardImg(index)
		screen.blit(background, (self.cardsInHand[index].rect))
		
	def moveAndShowCard(self,index,x,y,screen):
		self.moveCard(index, x, y)
		self.showCard(index, screen)

		
	def refreshHand(self,screen):
		for i in range(0,13):
			if self.cardsInHand[i].isPlayed==False:
				self.showCard(i, screen)
			elif self.currentPlay!=None :
				if self.currentPlay.index==i:
					self.showCard(i, screen)

	def getCardImg(self,index):                
		cardimg,cardrct=self.cardsInHand[index].getfrontImage()
		return cardimg

	def hastThisType(self,type):   
		for i in range(0,13):
			if self.cardsInHand[i].isPlayed==False:
				if self.cardsInHand[i].type==type:
					return True
		return False

	def checkIsPlayHeart(self,playedCard):
		if self.isQueenSpadesPlayed==True and self.isPlayHeart==True :
			return 
		for i in range(0,len(playedCard)):
			for j in range(0,4):
				if playedCard[i][j].type==cardType.Hearts:
					self.isPlayHeart=True
				if playedCard[i][j].type==cardType.Spades and  playedCard[i][j].name == cardNumber.queen :
					self.isQueenSpadesPlayed=True
				if self.isQueenSpadesPlayed==True and self.isPlayHeart==True :
					return 

	def checkOnlyHaveHearts(self, cards):
		for card in cards:
			if not card.type == cardType.Hearts and card.isPlayed == False:
				return False
		self.isPlayHeart = True
		return True

	def hasTrump(self, trumpCard, hand):
		for card in hand:
			if card.type == trumpCard.type:
				return True
		return False

	def MaxTree(self, maxHand, opponentHand, playedCards, node, depth, nodeDepth, heartsPlayed):	#positionInRound index 0, 0 is this player
		if depth == 0 or nodeDepth <= 0 or (len(maxHand) == 0 and len(opponentHand) == 0):
			node.v = node.score
			return node
		playableCards = opponentHand
		if node.player == 0:
			playableCards = self.playablePlayerCards(maxHand, len(playedCards) == 0, None if len(playedCards) == 0 else playedCards[0], heartsPlayed)

		for card in playableCards:
			newPlayed = list(playedCards)
			newPlayed.append(card)
			newNode = None
			if len(newPlayed) == 4:
				node.setRoundScore(newPlayed)
				newNode = MaxNode(card, node.score, node.valueTaken, node.roundWinner)
				newPlayed = []
			else:
				newNode = MaxNode(card, node.score, node.valueTaken, self.nextPlayer(node.player))

			nodeDepth[0] -= 1
			node.childNodes.append(newNode)
			if node.player == 0:
				newHand = list(maxHand)
				newHand.remove(card)
				self.MaxTree(newHand, opponentHand, newPlayed, newNode, depth - 1, nodeDepth, heartsPlayed or card.type == cardType.Hearts)
			else:
				newHand = list(opponentHand)
				newHand.remove(card)
				self.MaxTree(maxHand, newHand, newPlayed, newNode, depth - 1, nodeDepth, heartsPlayed or card.type == cardType.Hearts)

			if node.childNodes[len(node.childNodes) - 1].valueTaken[node.player] < node.valueTaken[node.player]:
				node.valueTaken = node.childNodes[len(node.childNodes) - 1].valueTaken
			elif node.childNodes[len(node.childNodes) - 1].valueTaken[node.player] == node.valueTaken[node.player]:	#tie breaker
				biggest = 0
				for i in range(0,4):
					if i == node.player:
						continue
					if node.valueTaken[i] > biggest:
						biggest = node.valueTaken[i]
				for i in range(0,4):
					if i == node.childNodes[len(node.childNodes) - 1].player:
						continue
					if node.childNodes[len(node.childNodes) - 1].valueTaken[i] > biggest:
						node.valueTaken = node.childNodes[len(node.childNodes) - 1].valueTaken
						break
		return node


	def nextPlayer(self, currentPlayer):
		if currentPlayer == 3:
			return 0
		return currentPlayer + 1

	def playablePlayerCards(self, playerCards, isFirst, firstCard, heartsPlayed):
		playable=[]
		if isFirst and heartsPlayed:
			return playerCards
		if len(playerCards) == 13 and self.has2Clubs:
			for card in playerCards:
				if card.type == cardType.Clubs and card.name == cardNumber.num2:
					playable.append(card)
			return playable
		if isFirst and not heartsPlayed:
			if self.checkOnlyHaveHearts(playerCards):
				return playerCards
			else:
				for card in playerCards:
					if card.type != cardType.Hearts:
						playable.append(card)
				return playable
		
		gotTrump = self.hasTrump(firstCard, playerCards)
		if len(playerCards) == 13 and gotTrump == False :
			for card in playerCards:
				if card.type != cardType.Hearts and (card.name != cardNumber.queen or card.type != cardType.Spades):
					playable.append(card)
			if len(playable) == 0:
				playable == playerCards
			return playable
		if gotTrump == True:
			for card in playerCards:
				if card.type == firstCard.type:
					playable.append(card)
			return playable
		
		return playerCards


class MaxNode(object):
	def __init__(self, cardPlayed, InitScore, valueTaken, player):
		self.cardPlayed = cardPlayed
		self.score = InitScore
		self.valueTaken = valueTaken
		self.player = player
		self.childNodes = []
		self.roundWinner = -1

	def setRoundScore(self, playedCards):
		roundWinnerIndex = 0
		#Find winning card
		for i in range(1, 4):
			if playedCards[i].type == playedCards[roundWinnerIndex].type and playedCards[i].name > playedCards[roundWinnerIndex].name:
				roundWinnerIndex = i
		
		#count points
		score = 0;
		for i in range(0, 4):
			if playedCards[i].type == cardType.Hearts:
				score += 1
			elif playedCards[i].type == cardType.Spades and playedCards[i].name == cardNumber.queen:
				score += 13

		#get roundWinner
		playOrder = []
		if self.player == 0:
			playOrder = [1,2,3,0]
		elif self.player == 1:
			playOrder = [2,3,0,1]
		elif self.player == 2:
			playOrder = [3,0,1,2]
		else:
			playOrder = [0,1,2,3]
		self.roundWinner = playOrder[roundWinnerIndex]
		
		if self.roundWinner == 0:
			self.score = (self.score[0] + score, self.score[1], self.score[2], self.score[3])
		elif self.roundWinner == 1:
			self.score = (self.score[0], self.score[1] + score, self.score[2], self.score[3])
		elif self.roundWinner == 2:
			self.score = (self.score[0], self.score[1], self.score[2] + score, self.score[3])
		else:
			self.score = (self.score[0], self.score[1], self.score[2], self.score[3] + score)


