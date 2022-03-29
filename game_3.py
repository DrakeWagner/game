#!/usr/bin/env python

import pygame
from pygame.locals import *
import sys
import os

os.chdir('C:\\Users\\dwagn\\git\\game')

pygame.init() # begins game

height = 480
width = 720
ground_height = 325

'''
images
'''
image = pygame.image.load('player.png')
leftimage = pygame.transform.flip(image, True, False)

fps_clock = pygame.time.Clock()

displaysurface = pygame.display.set_mode((width, height))
pygame.display.set_caption('Title')

class Background(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.bgimage = pygame.image.load('bg.png')
        self.bgY = 0
        self.bgX = 0

    def render(self):
        displaysurface.blit(self.bgimage, (self.bgX, self.bgY))

class Ground(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('ground.png')
        self.rect = self.image.get_rect(center = (360, 650))

    def render(self):
        displaysurface.blit(self.image, (self.rect.x, self.rect.y))

class Player(pygame.sprite.Sprite):
    global isJump

    def __init__(self, x, y):
        self.x = x  
        self.y = y
        self.pos = (x, y)
        self.movex = 0
        self.movey = 0
        self.image = image

        self.isJump = False
        self.jumpCount = 10

        self.rect = self.image.get_rect()

    def gravity(self):
        self.movey += 3.2
        
        # stop if hitting ground
        if self.pos[1] >= ground_height:
            self.movey -= 3.2


    # def jump(self): 
    #         print('attempting jump')
    #         self.movey += 3.2
    #         v = 5
    #         m = 1   

    #         F = (1 / 2) * m * (v**2)   
    #         self.movey -= F
    #         v = v-1
    #         if v<0:
    #             m = -1
    #         if v == -6:
    #             print('jump reset')
    #             isJump = False
    #             v=5
    #             m=1    

    def jump(self):
        if self.isJump:
            if self.jumpCount >= -10:
                neg = 1
                if self.jumpCount < 0:
                    neg = -1
                self.movey -= self.jumpCount**2 * 0.1 * neg
                self.jumpCount -= 1
            else:
                self.isJump = False
                self.jumpCount = 10

            self.pos = ((self.x + self.movex), (self.y + self.movey))

    def asd(self):
        # jump testing
        self.movey -= 50

    def move(self):

        keys = pygame.key.get_pressed() 

        # left
        if keys[K_a]:
            self.image = leftimage
            self.movex -= 5

        # right
        if keys[K_d]:
            self.image = image
            self.movex += 5

        if keys[K_SPACE]:
            print('attempting jump')
            isJump = True
        
        # if self.pos[1] == 325.6:
        #     isJump = False

    
        self.pos = ((self.x + self.movex), (self.y + self.movey))


    def render(self):
        displaysurface.blit(self.image, self.pos)   

'''
Setup class variables
'''

background = Background()
ground = Ground()
player = Player(20, 300)
player.rect.x = 0
player.rect.y = 0


running = True

while running:

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.asd()
                # Start to jump by setting isJump to True.
                player.isJump = True
            if event.key == ord('q'):
                pygame.quit()
                sys.exit()
            if event.key == ord('a'):
                print('left')
            if event.key == ord('d'):
                print('right')
            if event.key == ord('w'):
                print('up')
            if event.key == ord('s'):
                print('end down')


        if event.type == pygame.KEYUP:
            if event.key == ord('a'):
                print('end left')
            if event.key == ord('d'):
                print('end right')
            if event.key == ord('w'):
                print('end up')
            if event.key == ord('s'):
                print('end down')

    background.render()
    ground.render()
    
    player.gravity()
    player.move()
    player.jump
    player.update()
    player.render()
    fps_clock.tick(20)

    print(player.isJump)

    pygame.display.update()