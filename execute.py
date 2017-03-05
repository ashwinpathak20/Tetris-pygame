import sys
import random
import pygame
import time
from Gameplay import Gameplay
from Board import Board
from Block import Block
#initialising pygame
pygame.init()
pygame.key.set_repeat(250, 25)
display = pygame.display.set_mode((800, 640))
pygame.display.set_caption('Tetris')
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 25)
FPS = 3
#function to display a message
def message(msg, x, y):
    reply = font.render(msg, True, (0, 0, 0))
    rect = reply.get_rect()
    rect.midtop = (x, y)
    display.blit(reply, rect)

exit = True
b = Gameplay()
pause = 0
speed = 0
ret = 0
#loop to end the game
while exit:
    gameover = 0
    power = 0
    p = True
    b.selectPiece()
    if b.special == 1:
        power = 1
    display.fill((255, 255, 255))
    b.draw(700, 500, display)
    #loop to generate the random shapes
    while p:
        for event in pygame.event.get():
            #provision of pausing and quitting the game at any point of time
            # q quits the game , p pauses it
            if event.type == pygame.QUIT:
                exit = False
                p = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    if pause == 1:
                        pause = 0
                    else:
                        pause = 1
                elif event.key == pygame.K_q:
                    ret = 1

            if pause == 0 and ret == 0:
                #controls
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        if b.checkLeft():
                            b.moveLeft()
                    elif event.key == pygame.K_d:
                        if b.checkRight():
                            b.moveRight()
                    elif event.key == pygame.K_s:
                        b.rotate()
                    elif event.key == pygame.K_SPACE:
                        while b.checkDown():
                            b.moveDown()
        if pause == 0 and ret == 0:
            #drawing the whole game board and checking for each and every conditions
            message("TETRIS:", 700, 200)
            b.fillPiecePos(display)
            b.draw(b.x, b.y, display)
            if not b.checkRowEmpty():
                gameover = 1
                break
            if not b.checkDown():
                p = False
            else:
                b.moveDown()
            b.checkRowFull()
            msg = str(b.getScore())
            msg1 = str(b.getLevel())
            message("Score : " + msg, 700, 300)
            message("Level : " + msg1, 700, 400)
            pygame.display.update()
            clock.tick(FPS)

        if pause == 1:
            #after the game has been paused
            display.fill((255, 255, 255))
            message("TETRIS:", 700, 200)
            message("Score : " + msg, 700, 300)
            message("Level : " + msg1, 700, 400)
            message("Paused", 300, 200)
            pygame.display.update()

        if ret == 1:
            #after the game has been quit
            display.fill((255, 255, 255))
            message("Are You Sure That You Want To Quit?", 400, 200)
            message("Press Y to Quit , Press N to Continue", 400, 300)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit = False
                    p = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y:
                        exit = False
                        p = False
                    elif event.key == pygame.K_n:
                        ret = 0
            pygame.display.update()

    if gameover == 0:
        #special block functionality and updating the scores,levels and difficulty
        if power == 1:
            del(b.board[b.y/b.height])
            del(b.shade[b.y/b.height])
            b.board.insert(0, [0 for i in range(b.dis_width)])
            b.shade.insert(0, [(255, 255, 255) for i in range(b.dis_width)])

        b.updateScore(10)
        speed += 10
        if speed == 100:
            b.updateLevel()
            speed = 0
            FPS += 1
            del(b.board[0])
            del(b.shade[0])
            random1 = random.randint(b.y/b.height, b.dis_height-1)
            random2 = random.randint(0, b.dis_width-1)
            b.board[random1][random2] = 2
            b.board.insert(b.dis_height-1, [2 for i in range(b.dis_width)])
            b.shade.insert(b.dis_height-1, [(255, 255, 255) for i in range(b.dis_width)])

    if gameover == 1:
        #after the game is over
        display.fill((255, 255, 255))
        message("GAMEOVER!!", 300, 200)
        message("TETRIS:", 700, 200)
        message("Score : " + msg, 700, 300)
        message("Press C to continue or Q to Quit the game", 300, 400)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = False
                p = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    exit = False
                    p = False
                elif event.key == pygame.K_c:
                    b = Gameplay()
        pygame.display.update()
pygame.quit()
quit()
