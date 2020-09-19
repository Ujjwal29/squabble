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
font = pygame.font.SysFont(None, 30)
homescreen=pygame.image.load("images/mainmenu.png")
homescreen = pygame.transform.scale(homescreen, (800, 600))
def start():
    while True:
        screen.blit(homescreen,(0,0))
        button=[]
        btn=pygame.Rect(250, 250, 270, 45)
        button.append(btn)
        pygame.draw.rect(screen, (255, 255, 255,),btn)
        write_text('Play against computer', font, (0, 0, 0), screen, 390, 275)
        btn=pygame.Rect(290, 380, 270, 45)
        button.append(btn)
        pygame.draw.rect(screen, (255, 255, 255),btn)
        write_text('Play online (Multiplayer)', font, (0, 0, 0), screen, 420, 405)

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
                            main()
        pygame.display.update()
        mainClock.tick(60)

