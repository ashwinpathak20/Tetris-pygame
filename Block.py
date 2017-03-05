import sys
import random
import pygame
import time

class Block:
    #drawing the block
    def __init(self):
        return 0 

    def draw(self,x,y,display):
        for i in range(len(self.select)):
            for j in range(len(self.select[i])):
                if self.select[i][j]>0:
                    pygame.draw.rect(display,self.color,[x+self.width*i,y+self.height*j,self.width-1,self.height-1])
    #moving down of block
    def moveDown(self):
        self.y+=self.height
    #moving left of block
    def moveLeft(self):
        self.x-=self.width
    #moving right of block
    def moveRight(self):
        self.x+=self.width
    #rotating the block
    def rotate(self):
        self.select=list(reversed(zip(*self.select)))
        #if rotation is not possible
        if not  self.checkDown1():
            self.select=list(reversed(zip(*self.select)))
            self.select=list(reversed(zip(*self.select)))
            self.select=list(reversed(zip(*self.select)))

    #checking left area
    def checkLeft(self):
        flag=0
        for i in range(len(self.select)):
            for j in range(len(self.select[i])):
                if self.select[i][j]>0:
                    if self.checkPiecePos(self.x+self.width*i-self.width,self.y+self.height*j) or self.x+self.width*i==0:
                        flag=1
        if flag==0:
            return True
        else:
            return False
    #checking right area
    def checkRight(self):
        flag=0
        for i in range(len(self.select)):
            for j in range(len(self.select[i])):
                if self.select[i][j]>0:
                    if self.checkPiecePos(self.x+self.width*i+self.width,self.y+self.height*j) or self.x+self.width*(i+1)==self.dis_width*self.width:
                        flag=1
        if flag==0:
            return True
        else:
            return False
