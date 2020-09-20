import pygame
import sys
import time
import json
from pygame.locals import *
from write_text import write_text
# from game_map import main

mainClock = pygame.time.Clock()
multi= pygame.image.load("images/multipl.png")
multi = pygame.transform.scale(multi, (800, 600))
def wip():
    
    while True:
        pygame.init()
        pygame.display.set_caption('Squabble')
        screen = pygame.display.set_mode((800, 600),0,32)
        screen.blit(multi,(0,0))
        font = pygame.font.SysFont(None, 34)
        s="We are still working on this."
        q="Try playing the game locally!!"
        write_text(s, font, (255, 255, 255), screen,400,240)
        write_text(q, font, (255, 255, 255), screen,400,270)
        btn=pygame.Rect(260, 375, 270, 50)
        pygame.draw.rect(screen, (255, 255, 255),btn)
        write_text('Continue', font, (0, 0, 0), screen, 400, 395)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            mouse_pos = pygame.mouse.get_pos()
            if btn.collidepoint(mouse_pos):                  
                if event.type == MOUSEBUTTONDOWN:
                    print("click")
                    pygame.quit()
                    from game_map import main
                    main()
                    

        pygame.display.update()
        mainClock.tick(60)

