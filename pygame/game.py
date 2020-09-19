import pygame
import sys
import time
import json
from pygame.locals import *
from write_text import write_text
from win import win

class Game:

    def __init__(self,player1,player1_id,player2,player2_id):
        self.mainClock = pygame.time.Clock()
        pygame.init()
        pygame.display.set_caption('Squabble')
        self.screen = pygame.display.set_mode((800, 600),0,32)
        self.font = pygame.font.SysFont(None, 42)
        self.font_sm=pygame.font.SysFont(None,30)
        self.font_xs=pygame.font.SysFont(None,16)
        self.font_info=pygame.font.SysFont(None,24)
        self.img = pygame.image.load('images/character/elsa.png')
        self.bg= pygame.image.load('images/fight-bg.png')
        self.msg=pygame.image.load('images/msgs.png')
        self.att_button=pygame.image.load('images/button.png')
        self.att_bg=pygame.image.load('images/button-bg.png')
        self.lose=''
        self.win=''

        self.player1=player1
        self.player1_id=player1_id
        self.player2=player2
        self.player2_id=player2_id
        self.life1=240
        self.life2=240
        self.button=[]
        
        self.attack=' '
        self.attack_damage=0
        self.attack_desc=''
        self.attack_message=''

        #get json self.data
        with open('characters.json') as info:
            self.data = json.load(info)

        #set player1 images
    def set_img(self,a):
        rect = self.img.get_rect()
        if(a==1):
            x=200
        else:
            x=600
        rect.center = x, 250
        self.screen.blit(self.img, rect)

    #set bar at bottom for attack desc
    def info_bar(self,a):
        bar=pygame.Rect(0, 420, 800, 40)
        pygame.draw.rect(self.screen, (200,200,200),bar)
        if(a==1):
            temp=self.attack_desc
        else:
            temp=self.attack_message
        write_text(temp, self.font_info, (0, 0, 0), self.screen, 400,435 )
        print(self.attack_message)
        # bar=pygame.Rect(0, 420, 800, 40)
        # pygame.draw.rect(self.screen, (200,200,200),bar)

    #set health bar, width =240
    def health_bar(self,a):
        if(a==1):
            center_x=60
            rect_margin=75
        else:
            center_x=460
            rect_margin=475
        write_text("hp", self.font_xs, (255,255,255), self.screen,center_x,40)
        bar=pygame.Rect(rect_margin, 38, 250, 7)
        pygame.draw.rect(self.screen, (200, 200, 200),bar)

    def health_bar_update(self,a):
        self.health_bar(a)
        if(a==1):
            rect_margin=78
            self.life2-=((int(self.attack_damage))*240)/100
            if(self.life2<0):
                self.life2=0
            width=self.life2
        else:
            rect_margin=478
            self.life1-=((int(self.attack_damage))*240)/100
            if(self.life1<0):
                self.life1=0
            width=self.life1
        
        if(self.life2==0):
            print('player 1 wins!')
            self.win=self.player2
        if(self.life1==0):
            print('player 2 wins')
            self.win=self.player1
        bar=pygame.Rect(rect_margin, 39.5,width, 4.5)
        pygame.draw.rect(self.screen, (0, 255, 0),bar)

    #shows attack options
    def attack_bar(self):
        bar=pygame.Rect(0, 450, 800, 150)
        pygame.draw.rect(self.screen, (255, 255, 255),bar)

        for i in range(4):
            if(i<2):
                margin_left=80+(i*340)
                margin_top=465
            else:
                margin_left=80+(i-2)*340
                margin_top=525
            btn=pygame.Rect(margin_left,margin_top, 310, 50)
            self.button.append(btn)
            pygame.draw.rect(self.screen, (0, 0, 0),btn)
            

        for i in range(4):
            if(i<2):
                margin_top=490
                margin_left=220+(i*360)
            else:
                margin_top=550
                margin_left=220+(i-2)*360
            write_text(self.data[int(self.player1_id)]['attacks'][i]['attack_name']
            , self.font_sm, (255,255,255), self.screen, margin_left,margin_top)

    #basic setup of player 1- name,healthbar and img
    def player1_char_set(self):
        write_text(self.player1, self.font_sm, (255, 255, 255), self.screen, 200,20 )
        self.health_bar(1)
        self.health_bar_update(1)
        self.set_img(1)

    def player2_char_set(self):
        write_text(self.player2, self.font_sm, (255, 255, 255), self.screen, 600,20 )
        self.health_bar(2)
        self.health_bar_update(2)
        self.set_img(2)

    #game play of player1. choose attacks and shit
    def player1_play(self):
        self.attack_bar()


    def update_player1(self):
        self.info_bar(1)
        self.health_bar_update(2)

    def update_player2(self):
        self.info_bar(2)
        self.health_bar_update(1)

    #gameloop
    def play(self):
        running = True
        self.screen.blit(self.bg,(0,0))
        line=pygame.Rect(405,0, 1, 600)
        pygame.draw.rect(self.screen, (255, 255, 255),line)
        bar=pygame.Rect(0, 440, 800, 160)
        pygame.draw.rect(self.screen, (255, 255, 255),bar)
        self.player1_char_set()
        self.player2_char_set()
        flag=0
        msg=False
        while running:
            self.player1_play()
            # self.player2(2)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                temp=0
                mouse_pos = pygame.mouse.get_pos()
                for i, rect in enumerate(self.button):  
                    if rect.collidepoint(mouse_pos):                
                        if event.type == MOUSEBUTTONDOWN:
                            flag=1
                            self.attack=self.data[int(self.player1_id)]['attacks'][self.button.index(rect)]['attack_name']
                            self.attack_damage=self.data[int(self.player1_id)]['attacks'][self.button.index(rect)]['attack_damage']
                            self.attack_desc=self.data[int(self.player1_id)]['attacks'][self.button.index(rect)]['attack_desc']
                            self.attack_message=self.data[int(self.player1_id)]['attacks'][self.button.index(rect)]['attack_message']

                if(flag==1):
                    self.update_player1()                   
                    flag=2
                    pygame.display.update()
                    pygame.time.wait(2000)

                if(flag==2):
                    self.attack=self.data[int(self.player2_id)]['attacks'][0]['attack_name']
                    self.attack_damage=self.data[int(self.player2_id)]['attacks'][0]['attack_damage']
                    self.attack_desc=self.data[int(self.player2_id)]['attacks'][0]['attack_desc']
                    self.attack_message=self.data[int(self.player2_id)]['attacks'][0]['attack_message']
                    self.update_player2()
                    flag=0

                if(self.win):
                    running=False
                    win(self.win)
                    print(self.won,'is the winner')
                    break


            pygame.display.update()
            self.mainClock.tick(10)
