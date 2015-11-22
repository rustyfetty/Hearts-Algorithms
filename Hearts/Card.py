#Game developed by Milad Rastian (miladmovie atsign gmail dot com) 
#http://weblog.miladmovie.com/
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
#Read more about GNU General Public License :http://www.gnu.org/licenses/gpl.txt
import random
import os,math
from inits import *
	  
class cards:
    
	def __init__(self): 

		self.cardItem = []
		#add Hearsts cards
		
		self.cardItem.append(card(cardNumber.Ace,cardType.Hearts,13))
		
		self.cardItem.append(card(cardNumber.num2,cardType.Hearts,1))
		self.cardItem.append(card(cardNumber.num3,cardType.Hearts,2))
		self.cardItem.append(card(cardNumber.num4,cardType.Hearts,3))
		self.cardItem.append(card(cardNumber.num5,cardType.Hearts,4))
		self.cardItem.append(card(cardNumber.num6,cardType.Hearts,5))
		self.cardItem.append(card(cardNumber.num7,cardType.Hearts,6))
		self.cardItem.append(card(cardNumber.num8,cardType.Hearts,7))
		self.cardItem.append(card(cardNumber.num9,cardType.Hearts,8))
		self.cardItem.append(card(cardNumber.num10,cardType.Hearts,9))
		self.cardItem.append(card(cardNumber.jack,cardType.Hearts,10))
		self.cardItem.append(card(cardNumber.queen,cardType.Hearts,11))
		self.cardItem.append(card(cardNumber.king,cardType.Hearts,12))
		
		#add Spades cards
		self.cardItem.append(card(cardNumber.Ace,cardType.Spades,13))
		self.cardItem.append(card(cardNumber.num2,cardType.Spades,1))
		self.cardItem.append(card(cardNumber.num3,cardType.Spades,2))
		self.cardItem.append(card(cardNumber.num4,cardType.Spades,3))
		self.cardItem.append(card(cardNumber.num5,cardType.Spades,4))
		self.cardItem.append(card(cardNumber.num6,cardType.Spades,5))
		self.cardItem.append(card(cardNumber.num7,cardType.Spades,6))
		self.cardItem.append(card(cardNumber.num8,cardType.Spades,7))
		self.cardItem.append(card(cardNumber.num9,cardType.Spades,8))
		self.cardItem.append(card(cardNumber.num10,cardType.Spades,9))
		self.cardItem.append(card(cardNumber.jack,cardType.Spades,10))
		self.cardItem.append(card(cardNumber.queen,cardType.Spades,11))
		self.cardItem.append(card(cardNumber.king,cardType.Spades,12))
		
		#add Daimond cards
		self.cardItem.append(card(cardNumber.Ace,cardType.Daimond,13))
		self.cardItem.append(card(cardNumber.num2,cardType.Daimond,1))
		self.cardItem.append(card(cardNumber.num3,cardType.Daimond,2))
		self.cardItem.append(card(cardNumber.num4,cardType.Daimond,3))
		self.cardItem.append(card(cardNumber.num5,cardType.Daimond,4))
		self.cardItem.append(card(cardNumber.num6,cardType.Daimond,5))
		self.cardItem.append(card(cardNumber.num7,cardType.Daimond,6))
		self.cardItem.append(card(cardNumber.num8,cardType.Daimond,7))
		self.cardItem.append(card(cardNumber.num9,cardType.Daimond,8))
		self.cardItem.append(card(cardNumber.num10,cardType.Daimond,9))
		self.cardItem.append(card(cardNumber.jack,cardType.Daimond,10))
		self.cardItem.append(card(cardNumber.queen,cardType.Daimond,11))
		self.cardItem.append(card(cardNumber.king,cardType.Daimond,12))
		
		#add Clubs cards
		self.cardItem.append(card(cardNumber.Ace,cardType.Clubs,13))
		self.cardItem.append(card(cardNumber.num2,cardType.Clubs,1))
		self.cardItem.append(card(cardNumber.num3,cardType.Clubs,2))
		self.cardItem.append(card(cardNumber.num4,cardType.Clubs,3))
		self.cardItem.append(card(cardNumber.num5,cardType.Clubs,4))
		self.cardItem.append(card(cardNumber.num6,cardType.Clubs,5))
		self.cardItem.append(card(cardNumber.num7,cardType.Clubs,6))
		self.cardItem.append(card(cardNumber.num8,cardType.Clubs,7))
		self.cardItem.append(card(cardNumber.num9,cardType.Clubs,8))
		self.cardItem.append(card(cardNumber.num10,cardType.Clubs,9))
		self.cardItem.append(card(cardNumber.jack,cardType.Clubs,10))
		self.cardItem.append(card(cardNumber.queen,cardType.Clubs,11))
		self.cardItem.append(card(cardNumber.king,cardType.Clubs,12))  
		
		
		#shuffle cards
		self.shuffle()
		
	def shuffle(self):
		for i in range(0,1000) :
			random.shuffle(self.cardItem)
			random.shuffle(self.cardItem)
			random.shuffle(self.cardItem)

	def deck(self,player1,player2,player3,player4):
		for i in range(0,13):
			player1.addHand(self.cardItem[i])
		for i in range(13,26):
			player2.addHand(self.cardItem[i])
		for i in range(26,39):
			player3.addHand(self.cardItem[i])
		for i in range(39,52):
			player4.addHand(self.cardItem[i])

		player1.notMyCards = player2.cardsInHand + player3.cardsInHand + player4.cardsInHand
		player2.notMyCards = player1.cardsInHand + player3.cardsInHand + player4.cardsInHand
		player3.notMyCards = player2.cardsInHand + player1.cardsInHand + player4.cardsInHand
		player4.notMyCards = player2.cardsInHand + player3.cardsInHand + player1.cardsInHand

s=cards()   



 