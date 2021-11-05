import pygame
from pygame import mixer

pygame.init()
screen = pygame.display.set_mode((1400,900))
pygame.display.set_caption('The Last Hunter')
image = pygame.image.load('ICON.jfif')
pygame.display.set_icon(image)
name_game = pygame.image.load('name.png')
name_game = pygame.transform.scale(name_game,(700,300))
mon = pygame.image.load('Monster3-1.png')
mon = pygame.transform.scale(mon,(500,500))

class button():
    def __init__(self, x, y ,image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width*scale), int(height*scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
    def draw(self):
        action = False
        #get mouse position
        pos = pygame.mouse.get_pos()
        
        #check over and click
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
        
        # draw button on screen
        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action

#create button
start_btn = pygame.image.load('START.png')
quit_btn = pygame.image.load('QUIT.png')
start = button(620, 500, start_btn, 0.25)
quit = button(620, 600, quit_btn, 0.25)

bg_intro = pygame.image.load('bd.png')
bg_intro = pygame.transform.scale(bg_intro,(1400,900))
def intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        screen.blit(bg_intro,(0,0))
        screen.blit(name_game,(350,50))
        if start.draw():
            Background_1()
        if quit.draw():
            quit()
        pygame.display.update()

bg_1 = pygame.image.load('bg_1.jpg')
bg_1 = pygame.transform.scale(bg_1,(1400,900))
def Background_1():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    Background_2()

        screen.blit(bg_1,(0,0))
        pygame.display.update()

bg_2 = pygame.image.load('bg_2.jpg')
bg_2 = pygame.transform.scale(bg_2,(1400,900))
def Background_2():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    Background_3()

        screen.blit(bg_2,(0,0))
        pygame.display.update()

bg_3 = pygame.image.load('bg_3.jpg')
bg_3 = pygame.transform.scale(bg_3,(1400,900))
def Background_3():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    Background_4()

        screen.blit(bg_3,(0,0))
        pygame.display.update()

bg_4 = pygame.image.load('bg_4.jpg')
bg_4 = pygame.transform.scale(bg_4,(1400,900))
def Background_4():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    Background_5()

        screen.blit(bg_4,(0,0))
        pygame.display.update()
        
bg_5 = pygame.image.load('bg_5.jpg')
bg_5 = pygame.transform.scale(bg_5,(1400,900))
def Background_5():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    Background_6()

        screen.blit(bg_5,(0,0))
        pygame.display.update()

bg_6 = pygame.image.load('bg_6.jpg')
bg_6 = pygame.transform.scale(bg_6,(1400,900))
def Background_6():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    Background_7()

        screen.blit(bg_6,(0,0))
        screen.blit(mon,(700,450))
        pygame.display.update()

bg_7 = pygame.image.load('bg_7.png')
bg_7 = pygame.transform.scale(bg_7,(1400,900))
def Background_7():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    Background_8()

        screen.blit(bg_7,(0,0))
        pygame.display.update()

bg_8 = pygame.image.load('bg_8.png')
bg_8 = pygame.transform.scale(bg_8,(1400,900))
def Background_8():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    quit()

        screen.blit(bg_8,(0,0))
        pygame.display.update()

intro()
