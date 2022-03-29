#!/usr/bin/env python

from asyncio.constants import ACCEPT_RETRY_DELAY
from turtle import window_width
import pygame
from pygame.locals import *
import sys
import os
import random
from tkinter import *
from tkinter import filedialog

os.chdir('C:\\Users\\dwagn\\git\\game')

pygame.init()

height = 480
width = 720

game_window = pygame.display.set_mode((width, height))
pygame.display.set_caption("movement")

clock = pygame.time.Clock()

x_pos = width / 2
y_pos = height / 2

x_vel = 0
y_vel = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                x_vel += 5
            if event.key == pygame.K_a:
                x_vel -= 5
            if event.key == pygame.K_w:
                y_vel -= 5
            if event.key == pygame.K_s:
                y_vel += 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                x_vel -= 5
            if event.key == pygame.K_a:
                x_vel += 5
            if event.key == pygame.K_w:
                y_vel += 5
            if event.key == pygame.K_s:
                y_vel -= 5

    game_window.fill((255, 255, 255))

    x_pos += x_vel
    y_pos += y_vel
    rect = pygame.Rect(x_pos, y_pos, 100, 100)
    pygame.draw.rect(game_window, (255, 0, 0), rect)

    pygame.display.update()

    clock.tick(40)

pygame.quit()
sys.exit()