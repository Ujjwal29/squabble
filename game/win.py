import pygame
import sys
import time
import json
from pygame.locals import *
from write_text import write_text
# from game_map import main

mainClock = pygame.time.Clock()


continuehom=pygame.image.load("images/continue-bg.png")
continuehom = pygame.transform.scale(continuehom, (800, 600))
def win(winner):
    while True:
        pygame.init()
        pygame.display.set_caption('Squabble')
        screen = pygame.display.set_mode((800, 600),0,32)
        font = pygame.font.SysFont(None, 42)
        screen.blit(continuehom,(0,0))
        s=winner+" won!!"
        write_text(s, font, (255, 255, 255), screen,390,160)
        btn=pygame.Rect(263, 360, 270, 90)
        pygame.draw.rect(screen, (235,205,84),btn)
        write_text('Continue', font, (255,255, 255), screen, 400, 406)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            mouse_pos = pygame.mouse.get_pos()
            if btn.collidepoint(mouse_pos):                  
                if event.type == MOUSEBUTTONDOWN:
                    print("click")
                    pygame.quit()
                    from game_map import game_map
                    game_map()
                    

        pygame.display.update()
        mainClock.tick(60)
