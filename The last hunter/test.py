import pygame
from pygame import mixer

#window setting
pygame.init()
screen = pygame.display.set_mode((1400,900))
pygame.display.set_caption('The Last Hunter')
image = pygame.image.load('ICON.jpg')
pygame.display.set_icon(image)
name_game = pygame.image.load('name.png')
name_game = pygame.transform.scale(name_game,(700,200))
mixer.music.load('sound bg.mp3')
mixer.music.play()
heart = pygame.image.load('1hp.png')
heart = pygame.transform.scale(heart,(30,30))
red = (255, 0, 0)
green = (0, 255, 0)

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

class char():
    def __init__(self, x, y, name, hp, atk, block, scale):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.atk = atk
        self.block = block
        self.alive = True
        self.animation_list = []
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        for i in range(2):
            img = pygame.image.load(f'{self.name}/{i}.png')
            img = pygame.transform.scale(img, (img.get_width()*scale, img.get_height()*scale))
            self.animation_list.append(img)
        self.image = self.animation_list[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        #loop for motion
        animation_cooldown = 400
        self.image = self.animation_list[self.frame_index]
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        if self.frame_index >= len(self.animation_list):
            self.frame_index = 0
        
    def draw(self):
        screen.blit(self.image, self.rect)

class heartbar():
    def __init__(self, x, y, hp, max_hp):
        self.x = x
        self.y = y
        self.hp = hp
        self.max_hp = max_hp
        
    def draw(self, hp):
        self.hp = hp
        ratio = self.hp/self.max_hp
        pygame.draw.rect(screen, red, (self.x, self.y, 150, 20))
        pygame.draw.rect(screen, green, (self.x, self.y, 150*ratio, 20))
        
#create character
monster1 = char(1000, 490, 'Monster1', 6, 1, 1, 0.75)
monster3 = char(1000, 520, 'Monster3', 12, 4, 2, 4)
monster4 = char(1000, 520, 'Monster4', 20, 5, 1, 1)
monster6 = char(900, 600, 'Monster6', 18, 5, 5, 1)
monster7 = char(1000, 520, 'Monster7', 15, 6, 1, 1)
archer = char(300, 520, 'Archer', 8, 4, 1, 0.5)
assasin = char(300, 520, 'Assasin', 7, 3, 1, 0.5)
witch = char(300, 520, 'Witch', 7, 5, 1, 0.5)
swordman = char(300, 520, 'Swordman', 10, 2, 4, 0.5)

#create button
start_btn = pygame.image.load('START.png')
quit_btn = pygame.image.load('QUIT.png')
start = button(620, 500, start_btn, 0.75)
quit = button(620, 600, quit_btn, 0.75)

#create hpbar
archer_hpbar = heartbar(100, 200, archer.hp, archer.max_hp)

bg_intro = pygame.image.load('bg_intro.jpeg')
bg_intro = pygame.transform.scale(bg_intro,(1400,900))
def intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        screen.blit(bg_intro,(0,0))
        screen.blit(name_game,(350,100))
        if start.draw():
            choose_class()
        if quit.draw():
            quit()
        pygame.display.update()

choose = pygame.image.load('choose your class.png')
choose = pygame.transform.scale(choose,(1400,900))
class_pic = pygame.image.load('class.png')
pic1 = pygame.image.load('swordman1.png')
choice1 = button(150, 250 , pic1, 0.75)
pic2 = pygame.image.load('archer1.png')
choice2 = button(450, 250 , pic2, 0.75)
pic3 = pygame.image.load('assasin1.png')
choice3 = button(750, 250 , pic3, 0.75)
pic4 = pygame.image.load('witch1.png')
choice4 = button(1050, 250 , pic4, 0.75)

def choose_class():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        screen.blit(choose,(0,0))
        screen.blit(class_pic,(550,50))
        if choice1.draw():
            Background_1(True, False, False)
        if choice2.draw():
            Background_1(False, True, False)
        if choice3.draw():
            Background_1(False, False, True)
        if choice4.draw():
            Background_1(False, False, False)
        pygame.display.update()

bg_1 = pygame.image.load('bg_1.jpg')
bg_1 = pygame.transform.scale(bg_1,(1400,900))
def Background_1(char1, char2, char3):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    Background_2()

        screen.blit(bg_1,(0,0))
        monster1.update()
        monster1.draw()
        if char1:
            swordman.update()
            swordman.draw()
        elif char2:
            archer.update()
            archer.draw()
        elif char3:
            assasin.update()
            assasin.draw()
        else:
            witch.update()
            witch.draw()
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
        monster3.update()
        monster3.draw()
        screen.blit(heart,(60,195))
        archer_hpbar.draw(archer.hp)
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
        monster4.update()
        monster4.draw()
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
        monster6.update()
        monster6.draw()
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
        monster7.update()
        monster7.draw()
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
