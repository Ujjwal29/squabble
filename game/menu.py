import pygame
import sys
import time
import json
from pygame.locals import *
from game import Game
from write_text import write_text
from random import randint

mainClock = pygame.time.Clock()
startmenu=pygame.image.load("images/startmenu.jpg")
startmenu = pygame.transform.scale(startmenu, (800, 600))

with open('characters.json') as info:
    data = json.load(info)
 

def main_menu():
    while True:
        pygame.init()
        pygame.display.set_caption('Squabble')
        screen = pygame.display.set_mode((800, 600),0,32)
        font = pygame.font.SysFont(None, 42)
        screen.blit(startmenu,(0,0))
        write_text('Select a character to start playing!', font, (255, 255, 255), screen,400,50)
        button=[]
        for i in range(len(data)):
            btn=pygame.Rect(100, 100+(i*70), 600, 50)
            button.append(btn)
            pygame.draw.rect(screen, (0,0,0),btn)
        for i in range(len(data)):
            write_text(data[i]['name'], font, (255,255, 255), screen, 400,125+(i*70))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            mouse_pos = pygame.mouse.get_pos()
            for i, rect in enumerate(button):
                if rect.collidepoint(mouse_pos):                  
                    if event.type == MOUSEBUTTONDOWN:
                        print(data[button.index(rect)]['name'],"selected!!")
                        character=data[button.index(rect)]['name']
                        character_id=data[button.index(rect)]['id']
                        running=False
                        player2_id=randint(0,4)
                        player2=data[player2_id]['name']
                        game_obj=Game(character,character_id,player2,player2_id)
                        game_obj.play_()

        pygame.display.update()
        mainClock.tick(60)
 