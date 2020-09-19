import pygame
import sys
import time
import json
from pygame.locals import *
from menu import main_menu
from write_text import write_text

mainClock = pygame.time.Clock()

pygame.init()
pygame.display.set_caption('Squabble')
screen = pygame.display.set_mode((800, 600),0,32)
font = pygame.font.SysFont(None, 42)

def start():
    while True:
        screen.fill((0,0,0))
        
        btn=pygame.Rect(260, 250, 270, 50)
        pygame.draw.rect(screen, (255, 255, 255),btn)
        write_text('START', font, (0, 0, 0), screen, 400, 275)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            mouse_pos = pygame.mouse.get_pos()
            if btn.collidepoint(mouse_pos):                  
                if event.type == MOUSEBUTTONDOWN:
                    print("click")
                    running=False
                    main_menu()

        pygame.display.update()
        mainClock.tick(60)

