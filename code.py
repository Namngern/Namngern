import pygame
from pygame import mixer

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('The Last Hunter')
image = pygame.image.load('icon.png')
pygame.display.set_icon(image)
bg = pygame.image.load('bd.png')
bg = pygame.transform.scale(bg,(800,600))
name_game = pygame.image.load('name.png')
name_game = pygame.transform.scale(name_game,(400,200))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    screen.blit(bg,(0,0))
    screen.blit(name_game,(200,50))
    pygame.display.update()
