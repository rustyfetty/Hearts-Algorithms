#!/usr/bin/env python
#Game developed by Milad Rastian (miladmovie atsign gmail dot com) 
#https://gna.org/projects/pyhearts/
#I wrote this Game for course Artificial Intelligent in Yazd Jahad University
#Thanks my teacher Mr Asghar Dehghani
#I in this project I know how much I Love Python !
#Copyright (C) 2006  Milad Rastian
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

from time import gmtime, strftime
import os,math
from Player import *
from Paranoid import *
from Max import *
from inits import  *
from  Card import *

class background:
	def __init__(self):
		self.blink=0 #it will contorl blink text until 
		self.ShowScoreBoardDialog =False
		self.playedCards=[]
		self.tmpPlayedCard=[]
		self.scoreBoard=[]
		self.errorMsg=""
		self.isPlayHeart=False
		
		self.numOfGames = int(raw_input("Please input number of games: "))
		self.gameNumber = 0
		self.player1=None
		self.player2=None
		self.player3=None
		self.player4=None
		self.playerName=[]
		self.playerName.append("paranoid1")
		self.playerName.append("max1")
		self.playerName.append("max2")
		self.playerName.append("max3")
		self.directory = strftime("%a, %d %b %Y %H;%M;%S", gmtime())
		os.makedirs(self.directory)
		self.scoreFile = open(self.directory + "\score.csv", 'w')
		self.timeFile = open(self.directory + "\\time.csv", 'w')
	
		#reset hands
		self.playAgain()
		self.emptyGround=False
		
		self.numOfDeckPlay=0
		self.players=[]
		self.players.append(self.player1)
		self.players.append(self.player2)
		self.players.append(self.player3)
		self.players.append(self.player4)

		self.scoreFile.write(self.playerName[0] + "," + self.playerName[1] + "," + self.playerName[2] + "," + self.playerName[3] + "\n")
		self.timeFile.write(self.playerName[0] + "," + self.playerName[1] + "," + self.playerName[2] + "," + self.playerName[3] + "\n")
		indD=0
		while 1:  
			#change status of self.blink
			if self.blink==11 : self.blink=0
			else : self.blink+=1
			#check if Option Dialog is open dont let players to play
			if self.ShowScoreBoardDialog==True:
				self.scoreBoardDialog()
				
				continue
			if self.numOfDeckPlay==13:
				if self.player1.tmpResult==26:
					self.player1.result-=26
					self.player2.result+=26
					self.player3.result+=26
					self.player4.result+=26
				elif self.player2.tmpResult==26:
					self.player2.result-=26
					self.player1.result+=26
					self.player3.result+=26
					self.player4.result+=26
				elif self.player3.tmpResult==26:
					self.player3.result-=26
					self.player1.result+=26
					self.player2.result+=26
					self.player4.result+=26
				elif self.player4.tmpResult==26:
					self.player4.result-=26
					self.player1.result+=26
					self.player2.result+=26
					self.player3.result+=26
					
				print ""
				print ""
				print ""
				print self.player1.name," got ",self.player1.result," point"
				print self.player2.name," got ",self.player2.result," point"
				print self.player3.name," got ",self.player3.result," point"
				print self.player4.name," got ",self.player4.result," point"
				print ""
				print ""
				print ""
				self.scoreFile.write(str(self.player1.result) + "," + str(self.player2.result) + "," + str(self.player3.result) + "," + str(self.player4.result) + "\n")
				self.scoreBoard.append([self.player1.result,self.player2.result,self.player3.result,self.player4.result])
				self.ShowScoreBoardDialog=True
				self.scoreBoardDialog()
				if self.player1.result>=100 or self.player2.result>=100 or self.player3.result>=100 or self.player4.result>=100 :
						self.gameNumber += 1
						self.playedCards=[]
						self.tmpPlayedCard=[]
						self.numOfDeckPlay=0 
						self.players=[]
						self.players.append(self.player1)
						self.players.append(self.player2)
						self.players.append(self.player3)
						self.players.append(self.player4)
						self.emptyGround=False          
						self.errorMsg=""
						self.isPlayHeart=False
						self.scoreFile.write("\n")
				else:
					self.playAgain()
				if self.gameNumber < self.numOfGames:
					self.backToGame()
				if self.gameNumber == self.numOfGames:
					self.scoreFile.close()
					self.timeFile.close()
				continue
			indD+=1
			if self.turnPlay==1 and self.player1.currentPlay==None:
				self.selectedCard=self.player1.play(self.tmpPlayedCard,self.playedCards,self.players)
				self.player1.currentPlay=self.selectedCard
				self.tmpPlayedCard.append([self.selectedCard,1])
				#print "Player 1 play ",self.selectedCard.name
				self.selectedCard=None
				print self.player1.name, " played ", self.player1.currentPlay.getNameString(), " of ", self.player1.currentPlay.getTypeName()
				

				
			elif self.turnPlay==2 and self.player2.currentPlay==None:
				self.selectedCard=self.player2.play(self.tmpPlayedCard,self.playedCards,self.players)
				self.player2.currentPlay=self.selectedCard
				self.tmpPlayedCard.append([self.selectedCard,2])
				#print "Player 2 play ",self.selectedCard.name
				self.selectedCard=None
				print self.player2.name, " played ", self.player2.currentPlay.getNameString(), " of ", self.player2.currentPlay.getTypeName()

			elif self.turnPlay==3 and self.player3.currentPlay==None:
				self.selectedCard=self.player3.play(self.tmpPlayedCard,self.playedCards,self.players)
				self.player3.currentPlay=self.selectedCard
				self.tmpPlayedCard.append([self.selectedCard,3])
				#print "Player 3 play ",self.selectedCard.name
				self.selectedCard=None
				print self.player3.name, " played ", self.player3.currentPlay.getNameString(), " of ", self.player3.currentPlay.getTypeName()

			elif self.turnPlay==4 and self.player4.currentPlay==None:
				self.selectedCard=self.player4.play(self.tmpPlayedCard,self.playedCards,self.players)
				self.player4.currentPlay=self.selectedCard
				self.tmpPlayedCard.append([self.selectedCard,4])
				#print "Player 3 play ",self.selectedCard.name
				self.selectedCard=None
				print self.player4.name, " played ", self.player4.currentPlay.getNameString(), " of ", self.player4.currentPlay.getTypeName()
											   
			
			if self.player1.currentPlay!=None and self.player2.currentPlay!=None and self.player3.currentPlay!=None   and self.player4.currentPlay!=None  :
				#played on deck so we put ground in  PlayedCards
				self.player1.currentPlay.isPlayed=True
				self.player2.currentPlay.isPlayed=True
				self.player3.currentPlay.isPlayed=True
				self.player4.currentPlay.isPlayed=True
				self.addPlayedCards(self.player1.currentPlay, self.player2.currentPlay, self.player3.currentPlay, self.player4.currentPlay)
				self.turnPlay=self.whoseTurnNow(self.player1.currentPlay, self.player2.currentPlay, self.player3.currentPlay, self.player4.currentPlay)
				
				#check result on this deck
				typeToPlayed=self.tmpPlayedCard[0][0].type
				numOfMaxPlayed=self.tmpPlayedCard[0][0].name
				cardBelongToPlayer=None
				for i in range(0,4):
					if self.tmpPlayedCard[i][0].type==typeToPlayed and  self.tmpPlayedCard[i][0].name>=numOfMaxPlayed:
						numOfMaxPlayed=self.tmpPlayedCard[i][0].name
						if self.tmpPlayedCard[i][1] ==1:
							cardBelongToPlayer=self.player1
						elif self.tmpPlayedCard[i][1]==2:
							cardBelongToPlayer=self.player2
						elif self.tmpPlayedCard[i][1]==3:    
							cardBelongToPlayer=self.player3
						elif self.tmpPlayedCard[i][1]==4:
							cardBelongToPlayer=self.player4
				if cardBelongToPlayer:
					result=0
					for card in self.tmpPlayedCard:
						if card[0].type==cardType.Hearts:
							result+=1
						if card[0].type==cardType.Spades and card[0].name==cardNumber.queen:
							result+=13
					cardBelongToPlayer.result+=result
					cardBelongToPlayer.tmpResult+=result
					print cardBelongToPlayer.name," got ",result," point(s)"
					print ""
					cardBelongToPlayer=None
					self.timeFile.write(str(self.player1.calculateTime) + "," + str(self.player2.calculateTime) + "," + str(self.player3.calculateTime) + "," + str(self.player4.calculateTime) + "\n")
					
				else:
					print "Error ! report me now ! thanks"
				
				#now set None to play next deck
				self.player1.currentPlay=None
				self.player2.currentPlay=None
				self.player3.currentPlay=None
				self.player4.currentPlay=None
				
				self.numOfDeckPlay+=1
				self.tmpPlayedCard=[]
				
				
				
			else:
				if self.turnPlay==1 and self.player1.currentPlay!=None:
					self.turnPlay=2
				if self.turnPlay==2 and self.player2.currentPlay!=None:
					self.turnPlay=3
				if self.turnPlay==3 and self.player3.currentPlay!=None:
					self.turnPlay=4
				if self.turnPlay==4 and self.player4.currentPlay!=None:
					self.turnPlay=1
			
	#check how is turn now
	def whoseTurnNow(self,card1,card2,card3,card4):
		getMaxCardOfDeckPlay=self.tmpPlayedCard[0][0]
		turn=1
		if (card1.type==getMaxCardOfDeckPlay.type):
			if(card1.name>=getMaxCardOfDeckPlay.name):
				turn=1
				getMaxCardOfDeckPlay=card1
		if (card2.type==getMaxCardOfDeckPlay.type):
			if(card2.name>=getMaxCardOfDeckPlay.name):
				turn=2
				getMaxCardOfDeckPlay=card2
		if (card3.type==getMaxCardOfDeckPlay.type):
			if(card3.name>=getMaxCardOfDeckPlay.name):
				turn=3
				getMaxCardOfDeckPlay=card3
		if (card4.type==getMaxCardOfDeckPlay.type):
			if(card4.name>=getMaxCardOfDeckPlay.name):
				turn=4
				getMaxCardOfDeckPlay=card4
		return turn

	def addPlayedCards(self,cardP1,cardP2,cardP3,cardP4):
		self.playedCards.append([cardP1,cardP2,cardP3,cardP4])
		
	def playAgain(self):
		self.playedCards=[]
		self.tmpPlayedCard=[]
		cc=cards()
		self.numOfDeckPlay=0
		
		#save players result
		resultPlayer1=0
		resultPlayer2=0
		resultPlayer3=0
		resultPlayer4=0

		#check if this is first Play scape
		if self.player1!=None:
			resultPlayer1=self.player1.result
			resultPlayer2=self.player2.result
			resultPlayer3=self.player3.result
			resultPlayer4=self.player4.result
		
		self.player1=Paranoid(self.playerName[0],0);
		self.player2=Max(self.playerName[1],1);
		self.player3=Max(self.playerName[2],2);
		self.player4=Max(self.playerName[3],3)
		
		#set Last players Result
		self.player1.result=resultPlayer1
		self.player2.result=resultPlayer2
		self.player3.result=resultPlayer3
		self.player4.result=resultPlayer4
		
		cc.deck(self.player1, self.player2, self.player3, self.player4)
		
		#check how has card 2 Clubs to first play
		if self.player1.has2Clubs==True:
			self.turnPlay=1
		if self.player2.has2Clubs==True:
			self.turnPlay=2
		if self.player3.has2Clubs==True:
			self.turnPlay=3
		if self.player4.has2Clubs==True:
			self.turnPlay=4
	
	def scoreBoardDialog(self):    
		"""show Board Dialog"""
		xLocation=75
		
		#show players score 
		for scores in self.scoreBoard:
			fontColorPlayer1=(0, 0, 0)
			fontColorPlayer2=(0, 0, 0)
			fontColorPlayer3=(0, 0, 0)
			fontColorPlayer4=(0, 0, 0)
			minScore=scores[0]
			
			if scores[0]<=scores[1] and scores[0]<=scores[2] and scores[0]<=scores[3]:
				fontColorPlayer1=(234, 20, 35)
			
			if scores[1]<=scores[0] and scores[1]<=scores[2] and scores[1]<=scores[3]:
				fontColorPlayer2=(234, 20, 35)

			if scores[2]<=scores[0] and scores[2]<=scores[1] and scores[2]<=scores[3]:
				fontColorPlayer3=(234, 20, 35)

			if scores[3]<=scores[0] and scores[3]<=scores[1] and scores[3]<=scores[2]:
				fontColorPlayer4=(234, 20, 35)
				

			xLocation+=20
			


	def backToGame(self):
		"""back to game"""
		self.ShowScoreBoardDialog=False
		if self.player1.result>=100 or self.player2.result>=100 or self.player3.result>=100 or self.player4.result>=100 :
			self.scoreBoard=[]
			self.player1.result=0
			self.player2.result=0
			self.player3.result=0
			self.player4.result=0
			self.playAgain()
					
def main():
	g = background()

 
	  
