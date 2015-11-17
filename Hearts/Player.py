#Game developed by Milad Rastian (miladmovie atsign gmail dot com) 
#http://www.fritux.com/
#I wrote this Game for course Artificial Intelligent in Yazd Jahad University
#Thanks my teacher Mr Asghar Dehghani
#I in this project I know how much I Love Python !
#Copyright (C) 2006  Milad Rastiann
#
#This program is free software; you can redistribute it and/or
#modify it under the terms of the GNU General Public License
#as published by the Free Software Foundation; either version 2
#of the License, or (at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program; if not, write to the Free Software
#Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.


from inits import  *
from random import randint

class Player:
	
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
		self.tryDontPlayHearts=False
		self.tryDontPlaySpades=False
		self.tryDontPlayDaimond=False
		self.tryDontPlayClubs=False
		self.tryGetHearts=False
		self.result=0
		self.tmpResult=0
		self.notMyCards = []

		
	def addHand(self,card):
		self.cardsInHand.append(card)
		card.index=len(self.cardsInHand)-1
		if card.name==cardNumber.num2 and card.type==cardType.Clubs:
			self.has2Clubs=True
		if card.name==cardNumber.queen and card.type==cardType.Spades:
			self.hasQueenSpades=True

	def analayzPlayer(self,playedCard):
		for cards in playedCard:
			pass
			
	def play(self,cardInGround,playedCard,Players):
		cardsLeft = []
		for card in self.cardsInHand:
			if card.isPlayed != True:
				cardsLeft.append(card)
		for card in cardInGround:
			if card[0].type == cardType.Hearts:
				self.isPlayHeart = True

		if len(cardInGround) == 0:
			playable = self.playablePlayerCards(cardsLeft, True, None, self.isPlayHeart)
		else:
			playable = self.playablePlayerCards(cardsLeft, False, cardInGround[0][0], self.isPlayHeart)

		retcard=playable[randint(0, len(playable) - 1)]
		if retcard.type == cardType.Hearts:
			self.isPlayHeart == True

		return self.setAsPlay(retcard)
				

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

	def hasTrump(self, trumpCard, hand):
		for card in hand:
			if card.type == trumpCard.type:
				return True
		return False

	def setAsPlay(self,card):
		card.isPlayed=True
		if card.name==cardNumber.queen and cardType.Spades==card.type:
			self.hasQueenSpades=False
		return card

	def sortHande(self):

		for i in range(0,13):
			for j in range(0,13):
				if(self.cardsInHand[i].type>self.cardsInHand[j].type):
					tmp=self.cardsInHand[i]
					#self.cardsInHand[i]=None
					self.cardsInHand[i]=self.cardsInHand[j]
					#self.cardsInHand[j]=None
					self.cardsInHand[j]=tmp
				elif(self.cardsInHand[i].type==self.cardsInHand[j].type):
					if(self.cardsInHand[i].name<self.cardsInHand[j].name):
						tmp=self.cardsInHand[i]
						self.cardsInHand[i]=self.cardsInHand[j]
						self.cardsInHand[j]=tmp
						pass
	
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


		self.errorMsg=None
		return True

	def checkOnlyHaveHearts(self, cards):
		for card in cards:
			if not card.type == cardType.Hearts and card.isPlayed == False:
				return False
		self.isPlayHeart = True
		return True
	
		