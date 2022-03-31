#!/usr/bin/env python

import sys
import pygame
import os
os.chdir('C:\\Users\\dwagn\\git\\game')

pygame.init()

height = 480
width = 720
size = width, height
ground_height = 325
speed = [1,1]

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Movement test')

    # def render(self):
    #     displaysurface.blit(self.image, self.pos)


ball = pygame.image.load('ball.png')
ballrect = ball.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]
    screen.blit(ball, ballrect)
    pygame.display.flip()