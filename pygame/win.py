import pygame
import sys
import time
import json
from pygame.locals import *
from write_text import write_text


mainClock = pygame.time.Clock()

pygame.init()
pygame.display.set_caption('Squabble')
screen = pygame.display.set_mode((800, 600),0,32)
font = pygame.font.SysFont(None, 42)

def win(winner):
    while True:
        screen.fill((0,0,0))
        s=winner+" won!!"
        write_text(s, font, (255, 255, 255), screen,400,200)
        btn=pygame.Rect(260, 250, 270, 50)
        pygame.draw.rect(screen, (255, 255, 255),btn)
        write_text('Continue', font, (0, 0, 0), screen, 400, 275)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            mouse_pos = pygame.mouse.get_pos()
            if btn.collidepoint(mouse_pos):                  
                if event.type == MOUSEBUTTONDOWN:
                    print("click")
                    

        pygame.display.update()
        mainClock.tick(60)

