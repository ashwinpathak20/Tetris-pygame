import sys
import random
import pygame
import time
from Block import Block
from Board import Board

class Gameplay(Block,Board):
    #initialising the variables
    def __init__(self):
        self.height=20
        self.width=20
        self.dis_height=32
        self.dis_width=30
        self.board=[[0 for i in range(31)] for j in range(33)]
        self.shade=[[(255,255,255) for i in range(31)] for j in range(33)]
        self.__score=0
        self.__level=1
    #selecting a piece at random
    def selectPiece(self):
        self.x=300
        self.y=0
        self.special=0
        shapes=[[[1]],[[1,1,1,1]],[[2,2,2],[0,2,0]],[[3,3,0],[0,3,3]],[[0,4,4],[4,4,0]],[[5,5,5],[0,0,5]],[[6,6,6],[6,0,0]],[[7,7],[7,7]]]
        e=random.randint(0,7)
        if e==0:
            self.special=1
        self.select=shapes[e]
        colour=[(255,0,0),(0,150,0),(0,0,150),(255,255,0),(160,32,240),(255,140,0)]
        e=random.randint(0,5)
        self.color=colour[e]
    #checking whether the row is full
    def checkRowFull(self):
        for j in range(self.dis_height):
            flag=0
            for i in range(self.dis_width):
                if self.board[j][i]!=1:
                    flag=1
            if flag==0:
                self.updateScore(100)
                del(self.board[j])
                del(self.shade[j])
                self.board.insert(0,[0 for k in range(self.dis_width)])
                self.shade.insert(0,[(255,255,255) for k in range(self.dis_width)])
    #checking whether the row is empty (for gameover functionality)
    def checkRowEmpty(self):
        flag=0
        for j in range(self.dis_width):
            if self.board[0][j]==1:
                flag=1
        if flag==0:
            return True
        else:
            return False
    #getters and setters for score and level
    def updateScore(self,x):
        self.__score+=x

    def updateLevel(self):
        self.__level+=1

    def getScore(self):
        return self.__score

    def getLevel(self):
        return self.__level
