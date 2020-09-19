import pygame
import sys
import time
import json
from pygame.locals import *
from game_map import game_map
from write_text import write_text
from wip import wip

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
background=pygame.image.load("images/map-bg.png")
house1=pygame.image.load("images/house1.png")
house1 = pygame.transform.scale(house1, (180, 100))
house2=pygame.image.load("images/house2.png")
house2 = pygame.transform.scale(house2, (100, 164))
house3=pygame.image.load("images/house3.png")
house3 = pygame.transform.scale(house3, (150, 100))
char=pygame.image.load('images/volleyball.png')


class Wall(pygame.sprite.Sprite):
    """This class represents the bar at the bottom that the player controls """
 
    def __init__(self, x, y, width, height, color):
        """ Constructor function """
 
        # Call the parent's constructor
        super().__init__()
 
        # Make a BLUE wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
 
 
class Player(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the
    player controls """
 
    # Set speed vector
    change_x = 0
    change_y = 0
 
    def __init__(self, x, y):
        """ Constructor function """
 
        # Call the parent's constructor
        super().__init__()
 
        # Set height, width
        self.image = pygame.Surface([25, 25])

 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.image.blit(char,(x,y))
    def changespeed(self, x, y):
        """ Change the speed of the player. Called with a keypress. """
        self.change_x += x
        self.change_y += y
 
    def move(self, walls):
        """ Find a new position for the player """
 
        # Move left/right
        self.rect.x += self.change_x
 
        # Did this update cause us to hit a wall?
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:
            # If we are moving right, set our right side to the left side of
            # the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right
 
        # Move up/down
        self.rect.y += self.change_y
 
        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:
            # Reset our position based on the top/bottom of the object.
           
            if self.change_y < 0:
                self.rect.top = block.rect.bottom
        
            else:
                self.rect.bottom = block.rect.top         
                

class Map(object):
    """ Base class for all rooms. """
 
    # Each room has a list of walls, and of enemy sprites.
    wall_list = None
 
    def __init__(self):
        """ Constructor, create our lists. """
        self.wall_list = pygame.sprite.Group()
 
 
class Map1(Map):
    """This creates all the walls in room 1"""
    def __init__(self):
        super().__init__()
        # Make the walls. (x_pos, y_pos, width, height)
 
        # This is a list of walls. Each is in the form [x, y, width, height]
        walls = [[0, 0, 20, 530, WHITE],
                 [800, 140, 1, 450, WHITE],
                 [20, 0, 770, 20, WHITE],
                 [20, 600, 760, 1, WHITE],
                 [20, 20, 205, 60, GREEN],
                 [20, 400, 90, 130, BLUE],
                 [640, 20, 158, 80, BLUE],
                 [20, 130, 35, 300, RED],
                 [40, 145, 90, 280, RED],
                 [120, 160, 90, 180, RED],
                 [110, 350, 20, 180, RED],
                 [100, 490, 250, 70, RED],
                 [180, 20, 400, 70, RED],
                 [240, 20, 380, 70, RED],
                 [275, 100, 150, 225, RED],
                 [200, 385, 490, 40, RED],
                 [475, 220, 265, 120, RED],
                 [410, 480, 370, 130, RED],
                 [260, 20, 300, 150, RED],
                 [650, 140, 145, 40, RED]
                ]
 
        # Loop through the list. Create the wall, add it to the list
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)
           

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
    
            if player.rect.x > 700:
                done=False
                print("Bye")
            
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

    def start(self):
        while True:
            button=[]
            btn=pygame.Rect(220, 200, 360, 50)
            button.append(btn)
            pygame.draw.rect(self.screen, (255, 255, 255),btn)
            write_text('Play against computer', self.font, (0, 0, 0), self.screen, 400, 225)
            btn=pygame.Rect(220, 290, 360, 50)
            button.append(btn)
            pygame.draw.rect(self.screen, (255, 255, 255),btn)
            write_text('Play online (Multiplayer)', self.font, (0, 0, 0), self.screen, 400, 315)

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
                                return 1
            pygame.display.update()
            self.mainClock.tick(60)

    def game_loop(self):
        running=True
        x=0
        while(running):
            if(self.start()):
                self.game_map()



obj=Game_client()
obj.game_loop()