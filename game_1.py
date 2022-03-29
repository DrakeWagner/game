#!/usr/bin/env python

from asyncio.constants import ACCEPT_RETRY_DELAY
import pygame
from pygame.locals import *
import sys
import os
import random
from tkinter import *
from tkinter import filedialog

os.chdir('C:\\Users\\dwagn\\git\\game')
'''
Variables/settings
'''
pygame.init() # begins game

vec = pygame.math.Vector2
height = 480
width = 720
acc = .3
fric = -.1
fps = 50
fps_clock = pygame.time.Clock()
count = 0

displaysurface = pygame.display.set_mode((width, height))
pygame.display.set_caption('Title')



'''
Objects
'''
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
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('player.png')
        self.rect = self.image.get_rect()

        self.pos = vec((10, 385))
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.fric = fric

        self.ACC = .4
        self.FRIC = 0


    def move(self):

        if abs(self.vel.x) > .3:
            self.running = True
        else:
            self.running = False

        # key presses
        keys = pygame.key.get_pressed()

        if keys[K_a]:
            self.acc.x = -self.ACC
        if keys[K_d]:
            self.acc.x = self.ACC

        self.acc.x += self.vel.x * self.fric
        self.vel += self.acc
        self.pos += self.vel + .5 * self.acc

        self.rect.topleft = self.pos

    def render(self):
        displaysurface.blit(self.image, self.pos)

    

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()



'''
Setup
'''
background = Background()
ground = Ground()
player = Player()

'''
Loop
'''

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    Background().render()
    Ground().render()

    player.move()
    player.render()

    pygame.display.update()
    fps_clock.tick(fps)

