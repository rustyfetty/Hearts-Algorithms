from inits import  *
import time

class Paranoid:

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
		self.calculateTime = 0

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
		paranoidHand = []
		opponentHand = []
		for card in self.cardsInHand:
			if card.isPlayed != True:
				paranoidHand.append(card)
		for card in self.notMyCards:
			if card.isPlayed != True:
				opponentHand.append(card)
		for card in cardInGround:
			if card[0].type == cardType.Hearts:
				self.isPlayHeart = True
		self.calculateTime = time.time()
		node = None
		if len(cardInGround) == 0:
			node = self.ParanoidTree(paranoidHand, opponentHand, [], ParanoidNode(True, None, 0, 26, 0, 26), lookAhead, [40000], self.isPlayHeart)
		else:
			node = self.ParanoidTree(paranoidHand, opponentHand, [cardInGround[0][0]], ParanoidNode(True, None, 0, 26, 0, 26), lookAhead, [40000], self.isPlayHeart)
		retcard = None
		for child in node.childNodes:
			if child.v == node.v:
				retcard = child.cardPlayed
				break

		if retcard.type == cardType.Hearts:
			self.isPlayHeart == True
		self.calculateTime = time.time() - self.calculateTime
		return self.setAsPlay(retcard)

	def lookAheadLookup(self):
		if self.round > 7:
			return 4
		else:
			return 6

	def setAsPlay(self,card):
		card.isPlayed=True
		if card.name==cardNumber.queen and cardType.Spades==card.type:
			self.hasQueenSpades=False
		return card

	def playAgain(self):
		self.cardsInHand=[]
			
	def getCard(self,index):        
		return self.cardsInHand[index]

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

	def ParanoidTree(self, paranoidHand, opponentHand, playedCards, node, depth, nodeDepth, heartsPlayed):	#positionInRound index 0, 0 is this player
		if depth == 0 or nodeDepth <= 0 or (len(paranoidHand) == 0 and len(opponentHand) == 0):
			node.v = node.score
			return node
		#making the tree
		if node.isMin:
			playable = []
			playable = self.playablePlayerCards(paranoidHand, len(playedCards) == 0, None if len(playedCards) == 0 else playedCards[0], heartsPlayed)
			for card in playable:
				newNode = ParanoidNode(False, card, node.score, 0, node.alpha, node.beta)
				played = list(playedCards)
				played.append(card)
				if len(played) == 4:
					newNode.setRoundScore(played, [1,2,3,0])
					played = []
				node.childNodes.append(newNode)
				hand = list(paranoidHand)
				hand.remove(card)
				if len(played) == 0 and newNode.roundWinner == 0:
					playable = self.playablePlayerCards(hand, True, None, heartsPlayed or card.type == cardType.Hearts)
					for card in playable:
						nodeDepth[0] -= 1
						newHand = list(hand)
						newHand.remove(card)
						played.append(card)
						self.ParanoidTree(newHand, opponentHand, played, newNode, depth - 1, nodeDepth, heartsPlayed or card.type == cardType.Hearts)
						if node.childNodes[len(node.childNodes) - 1].v < node.v:	#alphabeta pruning
							node.v = node.childNodes[len(node.childNodes) - 1].v
							node.beta = node.v
						if node.v < node.alpha:	# if this is less than the best so far for the max return. the min node will only get take smaller, and max node alreay has a bigger num
							return node
				else:
					nodeDepth[0] -= 1
					self.ParanoidTree(hand, opponentHand, played, newNode, depth - 1, nodeDepth, heartsPlayed or card.type == cardType.Hearts)
					if node.childNodes[len(node.childNodes) - 1].v < node.v:	#alphabeta pruning
						node.v = node.childNodes[len(node.childNodes) - 1].v
						node.beta = node.v
					if node.v < node.alpha:	# if this is less than the best so far for the max return. the min node will only get take smaller, and max node alreay has a bigger num
						return node
			return node

		else:
			comb = self.getOpponentCombinations(opponentHand, 4 - len(playedCards))
			playable = comb[0]
			order = comb[1]

			for cards in playable:
				if nodeDepth[0] < 1:
					break
				newNode = ParanoidNode(True, None, node.score, 26, node.alpha, node.beta)
				played = list(playedCards)
				hand = list(opponentHand)
				for card in cards:
					played.append(card)
					hand.remove(card)
				if len(played) == 4:
					newNode.setRoundScore(played, order)
				node.childNodes.append(newNode)
				if len(played) < 4:
					nodeDepth[0] -= 1
					self.ParanoidTree(paranoidHand, hand, played, newNode, depth - 1, nodeDepth, heartsPlayed or card.type == cardType.Hearts)
					if node.childNodes[len(node.childNodes) - 1].v > node.v:	#alphabeta pruning
						node.v = node.childNodes[len(node.childNodes) - 1].v
						node.alpha = node.v
					if node.v > node.beta:	#if bigger than best min value then return. the max node can only get bigger, and the min node will never take it, because it already has something smaller
						return node
				elif newNode.roundWinner == 0:
					nodeDepth[0] -= 1
					self.ParanoidTree(paranoidHand, hand, [], newNode, depth - 1, nodeDepth, heartsPlayed or card.type == cardType.Hearts)
					if node.childNodes[len(node.childNodes) - 1].v > node.v:	#alphabeta pruning
						node.v = node.childNodes[len(node.childNodes) - 1].v
						node.alpha = node.v
					if node.v > node.beta:	#if bigger than best min value then return. the max node can only get bigger, and the min node will never take it, because it already has something smaller
						return node
				else:
					howManyCardsShouldOppPlay = [3,2,1]
					beginRound = self.getOpponentCombinations(hand, howManyCardsShouldOppPlay[newNode.roundWinner - 1])[0]
					for played in beginRound:
						newHand = list(hand)
						for card in played:
							newHand.remove(card)
						nodeDepth[0] -= 1
						self.ParanoidTree(paranoidHand, newHand, played, newNode, depth -1, nodeDepth, heartsPlayed or card.type == cardType.Hearts)
						if node.childNodes[len(node.childNodes) - 1].v > node.v:	#alphabeta pruning
							node.v = node.childNodes[len(node.childNodes) - 1].v
							node.alpha = node.v
						if node.v > node.beta:	#if bigger than best min value then return. the max node can only get bigger, and the min node will never take it, because it already has something smaller
							return node
			return node



	def getOpponentCombinations(self, opponentHand, numberInCombination):
		retValue = []
		order = []
		if numberInCombination == 1:
			order = [2,3,0,1]
			for card in opponentHand:
				retValue.append([card])
		elif numberInCombination == 2:
			order = [3,0,1,2]
			for i in range(0, len(opponentHand)):
				for j in range(i + 1, len(opponentHand)):
					retValue.append([opponentHand[i], opponentHand[j]])
		else:
			order = [0,1,2,3]
			for i in range(0, len(opponentHand)):
				for j in range(i + 1, len(opponentHand)):
					for k in range(j + 1, len(opponentHand)):
						retValue.append([opponentHand[i], opponentHand[j], opponentHand[k]])
		return (retValue, order)


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


class ParanoidNode(object):
	def __init__(self, isMin, cardPlayed, InitScore, v, alpha, beta):
		self.isMin = isMin
		self.cardPlayed = cardPlayed
		self.score = InitScore  #score of paranoid player
		self.v = v
		self.alpha = alpha	#best explored for max
		self.beta = beta	#best explored for min
		self.childNodes = []
		self.roundWinner = -1

	def setRoundScore(self, playedCards, playerOrder):
		roundWinnerIndex = 0
		#Find winning card
		for i in range(1, 4):
			if playedCards[i].type == playedCards[roundWinnerIndex].type and playedCards[i].name > playedCards[roundWinnerIndex].name:
				roundWinnerIndex = i
		score = 0;
		#count points
		for i in range(0, 4):
			if playedCards[i].type == cardType.Hearts:
				score += 1
			elif playedCards[i].type == cardType.Spades and playedCards[i].name == cardNumber.queen:
				score += 13

		#get roundWinner
		self.roundWinner = playerOrder[roundWinnerIndex]
		
		if(self.roundWinner == 0):
			self.score += score


