import pygame
import sys
import time
import json
from pygame.locals import *
from game_map import Wall,Player,Map,Map1
from write_text import write_text
from wip import wip
from game import Game
from random import randint

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
startmenu=pygame.image.load("images/startmenu.jpg")
startmenu = pygame.transform.scale(startmenu, (800, 600))
background=pygame.image.load("images/map-bg.png")
house1=pygame.image.load("images/house1.png")
house1 = pygame.transform.scale(house1, (180, 100))
house2=pygame.image.load("images/house2.png")
house2 = pygame.transform.scale(house2, (100, 164))
house3=pygame.image.load("images/house3.png")
house3 = pygame.transform.scale(house3, (150, 100))
char=pygame.image.load('images/volleyball.png')
homescreen=pygame.image.load("images/mainmenu.png")
homescreen = pygame.transform.scale(homescreen, (800, 600))
continuehom=pygame.image.load("images/continue-bg.png")
continuehom = pygame.transform.scale(continuehom, (800, 600))
bg= pygame.image.load('images/fight-bg2.png')        
bg = pygame.transform.scale(bg, (800, 600))
multi= pygame.image.load("images/multipl.png")
multi = pygame.transform.scale(multi, (800, 600))

with open('characters.json') as info:
    data = json.load(info)

class Game_client:

    def __init__(self):
        self.mainClock = pygame.time.Clock()
        pygame.init()
        pygame.display.set_caption('Squabble')
        self.screen = pygame.display.set_mode((800, 600),0,32)
        self.font = pygame.font.SysFont(None, 42)
        self.font_sm=pygame.font.SysFont(None,30)
        self.font_xs=pygame.font.SysFont(None,16)
        self.font_info=pygame.font.SysFont(None,24)
        self.screen.fill((0,0,0))
        # self.game_map=game_map()
        with open('characters.json') as info:
            self.data = json.load(info)

    
    def start(self):
        while True:
            button=[]
            self.screen.blit(homescreen,(0,0))
            btn=pygame.Rect(250, 250, 270, 45)
            button.append(btn)
            pygame.draw.rect(self.screen, (255, 255, 255),btn)
            write_text('Play against computer', self.font_sm, (0, 0, 0), self.screen, 390, 275)
            btn=pygame.Rect(290, 380, 270, 45)
            button.append(btn)
            pygame.draw.rect(self.screen, (255, 255, 255),btn)
            write_text('Play online (Multiplayer)', self.font_sm, (0, 0, 0), self.screen,420, 405)

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
                                return "local"
                            else:
                                return "online"
            pygame.display.update()
            self.mainClock.tick(60)


    def game_map(self):
        player = Player(100, 100)
        movingsprites = pygame.sprite.Group()
        movingsprites.add(player)
    
        maps = []
    
        room = Map1()
        maps.append(room)
    
        current_room_no = 0
        current_room = maps[current_room_no]
    
        clock = pygame.time.Clock()
    
        done = False
    
        while not done:
    
            # --- Event Processing ---  
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        player.changespeed(-3, 0)
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        player.changespeed(3, 0)
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        player.changespeed(0, -3)
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        player.changespeed(0, 3)
    
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        player.changespeed(3, 0)
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        player.changespeed(-3, 0)
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        player.changespeed(0, 3)
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        player.changespeed(0, -3)
    
            # --- Game Logic ---          
            player.move(current_room.wall_list)
    
            if player.rect.x < 40:
                done=False
                print('hello')
                return 1             
    
            if player.rect.x > 700:
                done=False
                print("Bye")
                return 1
            
            # --- Drawing ---
            self.screen.fill(BLACK)
            current_room.wall_list.draw(self.screen)
            self.screen.blit(background,(0,0))
            self.screen.blit(house1,(0,-20))
            self.screen.blit(house2,(0,360))
            self.screen.blit(house3,(650,0))
            movingsprites.draw(self.screen)
            pygame.display.flip()
            
            clock.tick(60)

    def main_menu(self):
        while True:
            self.screen.fill((0,0,0))
            self.screen.blit(startmenu,(0,0))
            write_text('Select a character to start playing!',self.font, (255, 255, 255),self.screen,400,50)
            button=[]
            for i in range(len(data)):
                btn=pygame.Rect(100, 100+(i*70), 600, 50)
                button.append(btn)
                pygame.draw.rect(self.screen, (255, 255, 255),btn)
            for i in range(len(data)):
                write_text(data[i]['name'], self.font, (0, 0, 0), self.screen, 400,125+(i*70))

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
                            print([character,character_id])
                            return([character,character_id])
                            # player2_id=randint(0,4)
                            # player2=data[player2_id]['name']
                            # game_obj=Game(character,character_id,player2,player2_id)
                            # game_obj.play()

            pygame.display.update()
            self.mainClock.tick(60)

    def play_game(self,players):
        play=Game(players[0],players[1],players[2],players[3])
        self.screen.blit(play.bg,(0,0))
        # line=pygame.Rect(405,0, 1, 600)
        # pygame.draw.rect(self.screen, (255, 255, 255),line)
        # bar=pygame.Rect(0, 440, 800, 160)
        # pygame.draw.rect(self.screen, (255, 255, 255),bar)
        play.player1_char_set()
        play.player2_char_set()
        flag=0
        msg=False
        running=True
        while running:
            play.player1_play()
            # self.player2(2)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                temp=0
                mouse_pos = pygame.mouse.get_pos()
                for i, rect in enumerate(play.button):  
                    if rect.collidepoint(mouse_pos):                
                        if event.type == MOUSEBUTTONDOWN:
                            flag=1
                            play.attack=self.data[int(play.player1_id)]['attacks'][play.button.index(rect)]['attack_name']
                            play.attack_damage=self.data[int(play.player1_id)]['attacks'][play.button.index(rect)]['attack_damage']
                            play.attack_desc=self.data[int(play.player1_id)]['attacks'][play.button.index(rect)]['attack_desc']
                            play.attack_message=self.data[int(play.player1_id)]['attacks'][play.button.index(rect)]['attack_message']

                if(flag==1):
                    play.update_player1()                   
                    flag=2
                    pygame.display.update()
                    pygame.time.wait(2000)

                if(flag==2):
                    r=randint(0,3)
                    play.attack=self.data[int(play.player2_id)]['attacks'][r]['attack_name']
                    play.attack_damage=self.data[int(play.player2_id)]['attacks'][r]['attack_damage']
                    play.attack_desc=self.data[int(play.player2_id)]['attacks'][r]['attack_desc']
                    play.attack_message=self.data[int(play.player2_id)]['attacks'][r]['attack_message']
                    play.update_player2()
                    flag=0

                if(play.win):
                    running=False
                    return(play.win)
                    # win(self.win)
                    # print(self.won,'is the winner')
                    break


            pygame.display.update()
            self.mainClock.tick(10)

    def win(self,winner): 
        while True:
            self.screen.fill((0,0,0))
            self.screen.blit(continuehom,(0,0))
            s=winner+" won!!"
            write_text(s, self.font, (255, 255, 255), self.screen,390,165)
            btn=pygame.Rect(263, 360, 270, 90)
            pygame.draw.rect(self.screen, (235,205,84),btn)
            write_text('Play again', self.font, (0, 0, 0), self.screen, 400, 406)

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                mouse_pos = pygame.mouse.get_pos()
                if btn.collidepoint(mouse_pos):                  
                    if event.type == MOUSEBUTTONDOWN:
                        print("continue")
                        return(1)
                        
            pygame.display.update()
            self.mainClock.tick(60)


    def wip(self):
        while True:
            self.screen.blit(multi,(0,0))
            s="We are still working on this."
            q="Try playing the game locally :)"
            write_text(s, self.font_sm, (255, 255, 255), self.screen,400,240)
            write_text(q, self.font_sm, (255, 255, 255), self.screen,400,270)
            btn=pygame.Rect(260, 375, 270, 50)
            pygame.draw.rect(self.screen, (255, 255, 255),btn)
            write_text('Continue', self.font, (0, 0, 0), self.screen, 400, 400)

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                mouse_pos = pygame.mouse.get_pos()
                if btn.collidepoint(mouse_pos):                  
                    if event.type == MOUSEBUTTONDOWN:
                        print("continue locally")
                        return 1
            pygame.display.update()
            self.mainClock.tick(60)

    def game_loop(self):
        running=True
        x=''
        x=self.start()
        while(running):            
            if(x=='local'):
                self.game_map()   
            else:
                self.wip()
                self.game_map()
            temp=[]
            temp=self.main_menu()
            player2_id=randint(0,6)
            player2=data[player2_id]['name']
            temp.append(player2)
            temp.append(player2_id)
            print(temp)
            winner=''
            winner=self.play_game(temp)
            if(self.win(winner)):
                self.screen.fill((0,0,0))
            else:
                self.screen.fill((0,0,0))
                pygame.quit()
                sys.exit()




obj=Game_client()
obj.game_loop()