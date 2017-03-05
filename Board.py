import sys
import random
import pygame
import time


class Board:
    def __init__(self):
        return 0
    #filling the whole board
    def fillPiecePos(self,display):
        for j in range(self.dis_height):
            for i in range(self.dis_width):
                if self.board[j][i]==1:
                    pygame.draw.rect(display,self.shade[j][i],[self.width*i,self.height*j,self.width-1,self.height-1])
                elif self.board[j][i]==2:
                    pygame.draw.rect(display,(0,0,0),[self.width*i,self.height*j,self.width,self.height])
                else:
                    if (i+j)%2==0:
                        pygame.draw.rect(display,(100,100,100),[self.width*i,self.height*j,self.width,self.height])
                    else:
                        pygame.draw.rect(display,(150,150,150),[self.width*i,self.height*j,self.width,self.height])
    #checking piece position whether it is already occupied
    def checkPiecePos(self,x,y):
        if self.board[y/self.height][x/self.width]!=0:
            return True
        else:
            return False
    #checking down 
    def checkDown(self):
        flag=0
        for i in range(len(self.select)):
            for j in range(len(self.select[i])):
                if self.select[i][j]>0:
                    if self.y+self.height*j+self.height==self.dis_height*self.height:
                        for i in range(len(self.select)):
                            for j in range(len(self.select[i])):
                                if self.select[i][j]>0:
                                    self.board[(self.y+self.height*j)/self.height][(self.x+self.width*i)/self.width]=1
                                    self.shade[(self.y+self.height*j)/self.height][(self.x+self.width*i)/self.width]=self.color
                        flag=1

        if flag==0:
            flag1=0
            for i in range(len(self.select)):
                for j in range(len(self.select[i])):
                    if self.select[i][j]>0:
                        if self.checkPiecePos(self.x+self.width*i,self.y+self.height*j+self.height):
                            for i in range(len(self.select)):
                                for j in range(len(self.select[i])):
                                    if self.select[i][j]>0:
                                        self.board[(self.y+self.height*(j))/self.height][(self.x+self.width*i)/self.width]=1
                                        self.shade[(self.y+self.height*(j))/self.height][(self.x+self.width*i)/self.width]=self.color
                            flag1=1
            if flag1==0:
                return True
        return False
    #condition for rotation
    def checkDown1(self):
        flag=0
        for i in range(len(self.select)):
            for j in range(len(self.select[i])):
                if self.select[i][j]>0:
                    if self.y+self.height*j+self.height==self.dis_height*self.height:
                        flag=1

        if flag==0:
            flag1=0
            for i in range(len(self.select)):
                for j in range(len(self.select[i])):
                    if self.select[i][j]>0:
                        if self.checkPiecePos(self.x+self.width*i,self.y+self.height*j+self.height):
                            flag1=1
            if flag1==0:
                return True
        return False
