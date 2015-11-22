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
import os, math

class cardType:
	Hearts=1
	Spades=2
	Daimond=3
	Clubs=4

class cardNumber:
	Ace=13
	num2=1
	num3=2
	num4=3
	num5=4
	num6=5
	num7=6
	num8=7
	num9=8
	num10=9
	jack=10
	queen=11
	king=12

class card:
	def __init__(self,name,type,priority,x=0,y=0):
		self.name=name
		self.type=type
		self.priority=priority
		self.use=False
		self.isPlayed=False
		self.side = 0
		self.index=0


	def getfrontImage(self):
		return self.fimg,self.rect
	def getImage(self):
		return self.img,self.rect
	def goUp(self,screen):
		background=self.fimg
		screen.blit(background, (self.rect))
	def getBackImage(self):
		return self.bimg,self.rect
	def getTypeName(self):
		if self.type == cardType.Hearts:
			return "hearts"
		elif self.type == cardType.Clubs:
			return "clubs"
		elif self.type == cardType.Daimond:
			return "diamond"
		else:
			return "spades"
	def getNameString(self):
		if self.name == cardNumber.Ace:
			return "ace"
		elif self.name == cardNumber.jack:
			return "jack"
		elif self.name == cardNumber.king:
			return "king"
		elif self.name == cardNumber.queen:
			return "queen"
		else:
			return self.name + 1

screenPlayer1=[]

for i in range (60,265,15):
    screenPlayer1.append([10,i])

screenPlayer1.append([132,150])

screenPlayer2=[]
for i in range (120,326,15):
    screenPlayer2.append([i,5])
screenPlayer2.append([210,103])    

screenPlayer3=[]
for i in range (60,265,15):
    screenPlayer3.append([420,i])
screenPlayer3.append([290,150]) 
  
screenPlayer4=[]
for i in range (120,326,15):
    screenPlayer4.append([i,300])
screenPlayer4.append([210,200])
#for loc in screenPlayer1:
#    print loc[1]
