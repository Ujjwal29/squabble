import pygame
import sys
import time
import json
from pygame.locals import *
from game import Game
from write_text import write_text

mainClock = pygame.time.Clock()

pygame.init()
pygame.display.set_caption('Squabble')
screen = pygame.display.set_mode((800, 600),0,32)
font = pygame.font.SysFont(None, 42)

with open('characters.json') as info:
    data = json.load(info)
 

def main_menu():
    while True:
        screen.fill((0,0,0))
        write_text('Select a character to start playing!', font, (255, 255, 255), screen,400,50)
        button=[]
        for i in range(len(data)):
            btn=pygame.Rect(100, 100+(i*70), 600, 50)
            button.append(btn)
            pygame.draw.rect(screen, (255, 255, 255),btn)
        for i in range(len(data)):
            write_text(data[i]['name'], font, (0, 0, 0), screen, 400,125+(i*70))

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
                        game_obj=Game(character,character_id,"Ironman",2)
                        game_obj.play()

        pygame.display.update()
        mainClock.tick(60)
 