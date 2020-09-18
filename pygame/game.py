import pygame
import sys
import time
import json
from pygame.locals import *

mainClock = pygame.time.Clock()

pygame.init()
pygame.display.set_caption('game base')
screen = pygame.display.set_mode((800, 600),0,32)
 
font = pygame.font.SysFont(None, 42)
with open('characters.json') as info:
    data = json.load(info)
 
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
 
click = False
 
def main_menu():
    while True:
        screen.fill((0,0,0))
        draw_text('Select a character', font, (255, 255, 255), screen, 280, 50)
        button=[]
        for i in range(len(data)):
            btn=pygame.Rect(100, 100+(i*70), 600, 50)
            button.append(btn)
            pygame.draw.rect(screen, (255, 255, 255),btn)
        for i in range(len(data)):
            draw_text(data[i]['name'], font, (0, 0, 0), screen, 120,110+(i*70))

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            mouse_pos = pygame.mouse.get_pos()
            for i, rect in enumerate(button):
                if rect.collidepoint(mouse_pos):                  
                    if event.type == MOUSEBUTTONDOWN:
                        print(data[button.index(rect)]['name'],"selected!!")
                        character=data[button.index(rect)]['name']
                        game()

        pygame.display.update()
        mainClock.tick(60)
 
def game():
    running = True
    while running:
        screen.fill((0,0,0))
        
        draw_text('game', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
        mainClock.tick(60)
 
main_menu()