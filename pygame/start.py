import pygame
import sys
import time
import json
from pygame.locals import *
from game_map import main
from write_text import write_text
from wip import wip

mainClock = pygame.time.Clock()

pygame.init()
pygame.display.set_caption('Squabble')
screen = pygame.display.set_mode((800, 600),0,32)
font = pygame.font.SysFont(None, 42)

def start():
    while True:
        screen.fill((0,0,0))
        button=[]
        btn=pygame.Rect(220, 200, 360, 50)
        button.append(btn)
        pygame.draw.rect(screen, (255, 255, 255),btn)
        write_text('Play against computer', font, (0, 0, 0), screen, 400, 225)
        btn=pygame.Rect(220, 290, 360, 50)
        button.append(btn)
        pygame.draw.rect(screen, (255, 255, 255),btn)
        write_text('Play online (Multiplayer)', font, (0, 0, 0), screen, 400, 315)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            mouse_pos = pygame.mouse.get_pos()
            for i, rect in enumerate(button):
                if rect.collidepoint(mouse_pos):                  
                    if event.type == MOUSEBUTTONDOWN:
                        print("playy!!")
                        running=False
                        if(button.index(rect)==0):
                            main()
                        else:
                            wip()

        pygame.display.update()
        mainClock.tick(60)

