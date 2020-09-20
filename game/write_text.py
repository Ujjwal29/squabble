import pygame

pygame.init()
pygame.display.set_caption('Squabble')
screen = pygame.display.set_mode((800, 600),0,32)
font = pygame.font.SysFont(None, 42)

def write_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect(center=(x,y))
    surface.blit(textobj, textrect)