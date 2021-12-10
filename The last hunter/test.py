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
money = pygame.image.load('money.png')
money = pygame.transform.scale(money,(30,30))
coin = 300
red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)
font = pygame.font.SysFont('FC Iconic Bold', 28)

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
    def __init__(self, x, y, name, hp, atk, block, speed, potion1, scale):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.atk = atk
        self.block = block
        self.speed = speed
        self.potion = potion1
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
            
    def attack(self, target):
        damage = target.block - self.atk
        if damage <= 0:
            target.hp += damage
        else:
            target.hp += 0
        if target.hp <= 0:
            target.hp = 0
            target.alive = False
        if self.hp <= 0:
            self.hp = 0
            self.alive = False

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

def draw_text(text, font, color, x, y):
    img1 = font.render(text, True, color)
    screen.blit(img1, (x, y))

#create potion
potion_have = 2
potion_heal = 2

#create character
monster1 = char(1000, 490, 'Slime', 6, 1, 1, 1, 0, 0.75)
monster2 = char(1000, 490, 'Black bull', 10, 3, 2, 1, 0, 0.75)
monster3 = char(1000, 490, 'Necromancer', 12, 4, 2, 2, 0, 0.75)
monster4 = char(1000, 600, 'Big eye', 20, 5, 1, 2, 0, 1)
monster5 = char(1000, 490, 'Cobra', 15, 5, 1, 5, 0, 1)
monster6 = char(900, 650, 'Golem', 18, 5, 5, 1, 0, 1)
monster7 = char(1000, 520, 'Grater', 15, 6, 1, 3, 0, 1)
monster8 = char(1050, 490, 'Eros', 30, 8, 5, 5, 0, 1)
archer = char(300, 520, 'Archer', 8, 4, 1, 4, potion_have, 0.5)
assasin = char(300, 520, 'Assasin', 7, 3, 1, 5, potion_have, 0.5)
witch = char(300, 520, 'Witch', 7, 5, 1, 3, potion_have, 0.5)
swordman = char(300, 520, 'Swordman', 10, 2, 4, 2, potion_have, 0.5)

#create button
start_btn = pygame.image.load('START.png')
quit_btn = pygame.image.load('QUIT.png')
next_btn = pygame.image.load('next_button.png')
potion_img = pygame.image.load('Potion.png')
attack_img = pygame.image.load('attack.png')
start = button(620, 500, start_btn, 0.75)
quit = button(620, 600, quit_btn, 0.75)
next = button(1200, 700, next_btn, 1)
potion_hp = button(800, 650, potion_img, 0.4)
attack_btn = button(400, 650, attack_img, 0.4)

#create hpbar
archer_hpbar = heartbar(100, 200, archer.hp, archer.max_hp)
sword_hpbar = heartbar(100, 200, swordman.hp, swordman.max_hp)
ass_hpbar = heartbar(100, 200, assasin.hp, assasin.max_hp)
witch_hpbar = heartbar(100, 200, witch.hp, witch.max_hp)
mon1_hpbar = heartbar(1000, 200, monster1.hp, monster1.max_hp)
mon2_hpbar = heartbar(1000, 200, monster2.hp, monster2.max_hp)
mon3_hpbar = heartbar(1000, 200, monster3.hp, monster3.max_hp)
mon4_hpbar = heartbar(1000, 200, monster4.hp, monster4.max_hp)
mon5_hpbar = heartbar(1000, 200, monster5.hp, monster5.max_hp)
mon6_hpbar = heartbar(1000, 200, monster6.hp, monster6.max_hp)
mon7_hpbar = heartbar(1000, 200, monster7.hp, monster7.max_hp)
mon8_hpbar = heartbar(1000, 200, monster8.hp, monster8.max_hp)

bg_rip = pygame.image.load('rip.png')
bg_rip = pygame.transform.scale(bg_rip,(1400,900))
def rip():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        screen.blit(bg_rip,(0,0))
        pygame.display.update()
        

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
            story()
        if quit.draw():
            quit()
        pygame.display.update()

bg_story = pygame.image.load('story.png')
bg_story = pygame.transform.scale(bg_story,(1400,900))
def story():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    choose_class()
                    
        screen.blit(bg_story,(0,0))
        if next.draw():
            choose_class()
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
            Background_1(True, False, False, coin)
        if choice2.draw():
            Background_1(False, True, False, coin)
        if choice3.draw():
            Background_1(False, False, True, coin)
        if choice4.draw():
            Background_1(False, False, False, coin)
        pygame.display.update()

shop_bg = pygame.image.load('shop.png')
shop_bg = pygame.transform.scale(shop_bg, (1400,900))
def shop():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
   
        screen.blit(shop_bg,(0,0))

bg_1 = pygame.image.load('bg_1.jpg')
bg_1 = pygame.transform.scale(bg_1,(1400,900))
def Background_1(char1, char2, char3, coin):
    archer = char(300, 520, 'Archer', 8, 4, 1, 4, potion_have, 0.5)
    assasin = char(300, 520, 'Assasin', 7, 3, 1, 5, potion_have, 0.5)
    witch = char(300, 520, 'Witch', 7, 5, 1, 3, potion_have, 0.5)
    swordman = char(300, 460, 'Swordman', 10, 2, 4, 2, potion_have, 0.5)
    current_fighter = 1
    total_fighter = 2
    action_cooldown = 0
    action_wait = 90
    check = 1
    while True:
        attack = False
        potion = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    Background_2(char1, char2, char3, coin)
            if monster1.alive == False:
                swordman.hp = swordman.max_hp
                archer.hp = archer.max_hp
                assasin.hp = assasin.max_hp
                
                coin += 100
                Background_2(char1, char2, char3, coin)
            if swordman.alive == False:
                rip()
        screen.blit(bg_1,(0,0))
        monster1.update()
        monster1.draw()
        draw_text(f'{monster1.name} HP: {monster1.hp}', font, white, 1000, 180)
        mon1_hpbar.draw(monster1.hp)
        screen.blit(money,(1150,100))
        draw_text('%d' %coin, font, white , 1200, 100)
        if potion_hp.draw():
            potion = True
        if attack_btn.draw():
            attack = True
        if char1:
            swordman.update()
            swordman.draw()
            sword_hpbar.draw(swordman.hp)
            draw_text(f'{swordman.name} HP: {swordman.hp}', font, white, 100, 180)
            draw_text(str(swordman.potion), font, white, 930, 790)
            if swordman.speed >= monster1.speed:
                if swordman.alive == True:
                    if current_fighter == 1:
                        action_cooldown += 1
                        if action_cooldown >= action_wait:
                            if attack == True:
                                swordman.attack(monster1)
                                current_fighter += 1
                                action_cooldown = 0
                            if potion == True:
                                if swordman.potion > 0:
                                    if swordman.max_hp - swordman.hp > potion_heal:
                                        heal = potion_heal
                                    else:
                                        heal = swordman.max_hp - swordman.hp
                                    swordman.hp += heal
                                    swordman.potion -= 1
                                    current_fighter += 1
                                    action_cooldown = 0
                if current_fighter == 2:
                    if monster1.alive == True:
                        action_cooldown += 1
                        if action_cooldown >= action_wait:
                            monster1.attack(swordman)
                            current_fighter += 1
                            action_cooldown = 0
            if swordman.speed < monster1.speed:
                if current_fighter == 1:
                    if monster1.alive == True:
                        action_cooldown += 1
                        if action_cooldown >= action_wait:
                                if attack == True or potion == True:
                                    monster1.attack(swordman)
                                    current_fighter += 1
                                    action_cooldown = 0
                                if potion == True:
                                    check += 1
                if swordman.alive == True:
                    if current_fighter == 2:
                        action_cooldown += 1
                        if action_cooldown >= action_wait:
                            if check == 1:
                                swordman.attack(monster1)
                                current_fighter += 1
                                action_cooldown = 0
                            else:
                                if swordman.potion > 0:
                                    if swordman.max_hp - swordman.hp > potion_heal:
                                        heal = potion_heal
                                    else:
                                        heal = swordman.max_hp - swordman.hp
                                    swordman.hp += heal
                                    swordman.potion -= 1
                                    current_fighter += 1
                                    action_cooldown = 0
                                    check = 1
                                else:
                                    check = 1
            if current_fighter > total_fighter:
                current_fighter = 1
        elif char2:
            archer.update()
            archer.draw()
            archer_hpbar.draw(archer.hp)
            draw_text(f'{archer.name} HP: {archer.hp}', font, white, 100, 180)
            draw_text(str(archer.potion), font, white, 930, 790)
            if archer.speed >= monster1.speed:
                if archer.alive == True:
                    if current_fighter == 1:
                        action_cooldown += 1
                        if action_cooldown >= action_wait:
                            if attack == True:
                                archer.attack(monster1)
                                current_fighter += 1
                                action_cooldown = 0
                            if potion == True:
                                if archer.potion > 0:
                                    if archer.max_hp - archer.hp > potion_heal:
                                        heal = potion_heal
                                    else:
                                        heal = archer.max_hp - archer.hp
                                    archer.hp += heal
                                    archer.potion -= 1
                                    current_fighter += 1
                                    action_cooldown = 0
                if current_fighter == 2:
                    if monster1.alive == True:
                        action_cooldown += 1
                        if action_cooldown >= action_wait:
                            monster1.attack(archer)
                            current_fighter += 1
                            action_cooldown = 0
            if archer.speed < monster1.speed:
                if current_fighter == 1:
                    if monster1.alive == True:
                        action_cooldown += 1
                        if action_cooldown >= action_wait:
                                if attack == True or potion == True:
                                    monster1.attack(archer)
                                    current_fighter += 1
                                    action_cooldown = 0
                                if potion == True:
                                    check += 1
                if archer.alive == True:
                    if current_fighter == 2:
                        action_cooldown += 1
                        if action_cooldown >= action_wait:
                            if check == 1:
                                archer.attack(monster1)
                                current_fighter += 1
                                action_cooldown = 0
                            else:
                                if archer.potion > 0:
                                    if archer.max_hp - archer.hp > potion_heal:
                                        heal = potion_heal
                                    else:
                                        heal = archer.max_hp - archer.hp
                                    archer.hp += heal
                                    archer.potion -= 1
                                    current_fighter += 1
                                    action_cooldown = 0
                                    check = 1
                                else:
                                    check = 1
            if current_fighter > total_fighter:
                current_fighter = 1
        elif char3:
            assasin.update()
            assasin.draw()
            ass_hpbar.draw(assasin.hp)
            draw_text(f'{assasin.name} HP: {assasin.hp}', font, white, 100, 180)
            draw_text(str(assasin.potion), font, white, 930, 790)
            if assasin.speed >= monster1.speed:
                if assasin.alive == True:
                    if current_fighter == 1:
                        action_cooldown += 1
                        if action_cooldown >= action_wait:
                            if attack == True:
                                assasin.attack(monster1)
                                current_fighter += 1
                                action_cooldown = 0
                if current_fighter == 2:
                    if monster1.alive == True:
                        action_cooldown += 1
                        if action_cooldown >= action_wait:
                            monster1.attack(assasin)
                            current_fighter += 1
                            action_cooldown = 0
            if assasin.speed < monster1.speed:
                if current_fighter == 1:
                    if monster1.alive == True:
                        action_cooldown += 1
                        if action_cooldown >= action_wait:
                            if attack == True:
                                monster1.attack(assasin)
                                current_fighter += 1
                                action_cooldown = 0
                if assasin.alive == True:
                    if current_fighter == 2:
                        action_cooldown += 1
                        if action_cooldown >= action_wait:
                            assasin.attack(monster1)
                            current_fighter += 1
                            action_cooldown = 0
            if current_fighter > total_fighter:
                current_fighter = 1
        else:
            witch.update()
            witch.draw()
            witch_hpbar.draw(witch.hp)
            draw_text(f'{witch.name} HP: {witch.hp}', font, white, 100, 180)
            draw_text(str(witch.potion), font, white, 930, 790)
            if witch.speed >= monster1.speed:
                if witch.alive == True:
                    if current_fighter == 1:
                        action_cooldown += 1
                        if action_cooldown >= action_wait:
                            if attack == True:
                                witch.attack(monster1)
                                current_fighter += 1
                                action_cooldown = 0
                if current_fighter == 2:
                    if monster1.alive == True:
                        action_cooldown += 1
                        if action_cooldown >= action_wait:
                            monster1.attack(witch)
                            current_fighter += 1
                            action_cooldown = 0
            if witch.speed < monster1.speed:
                if current_fighter == 1:
                    if monster1.alive == True:
                        action_cooldown += 1
                        if action_cooldown >= action_wait:
                            if attack == True:
                                monster1.attack(witch)
                                current_fighter += 1
                                action_cooldown = 0
                if witch.alive == True:
                    if current_fighter == 2:
                        action_cooldown += 1
                        if action_cooldown >= action_wait:
                            witch.attack(monster1)
                            current_fighter += 1
                            action_cooldown = 0
            if current_fighter > total_fighter:
                current_fighter = 1
        pygame.display.update()

bg_2 = pygame.image.load('bg_2.jpg')
bg_2 = pygame.transform.scale(bg_2,(1400,900))
def Background_2(char1, char2, char3, coin):
    current_fighter = 1
    total_fighter = 2
    action_cooldown = 0
    action_wait = 90
    check = 1
    while True:
        attack = False
        potion = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    Background_3(char1, char2, char3, coin)

        screen.blit(bg_2,(0,0))
        monster2.draw()
        monster2.update()
        draw_text(f'{monster2.name} HP: {monster2.hp}', font, white, 1000, 180)
        mon2_hpbar.draw(monster2.hp)
        screen.blit(money,(1150,100))
        draw_text('%d' %coin, font, white , 1200, 100)
        if potion_hp.draw():
            potion = True
        if attack_btn.draw():
            attack = True
        if char1:
            swordman.update()
            swordman.draw()
            sword_hpbar.draw(swordman.hp)
            draw_text(f'{swordman.name} HP: {swordman.hp}', font, white, 100, 180)
            draw_text(str(swordman.potion), font, white, 980, 710)
            if swordman.speed >= monster2.speed:
                if swordman.alive == True:
                    if current_fighter == 1:
                        action_cooldown += 1
                        if action_cooldown >= action_wait:
                            if attack == True:
                                swordman.attack(monster2)
                                current_fighter += 1
                                action_cooldown = 0
                            if potion == True:
                                if swordman.potion > 0:
                                    if swordman.max_hp - swordman.hp > potion_heal:
                                        heal = potion_heal
                                    else:
                                        heal = swordman.max_hp - swordman.hp
                                    swordman.hp += heal
                                    swordman.potion -= 1
                                    current_fighter += 1
                                    action_cooldown = 0
                if current_fighter == 2:
                    if monster2.alive == True:
                        action_cooldown += 1
                        if action_cooldown >= action_wait:
                            monster2.attack(swordman)
                            current_fighter += 1
                            action_cooldown = 0
            if swordman.speed < monster2.speed:
                if current_fighter == 1:
                    if monster2.alive == True:
                        action_cooldown += 1
                        if action_cooldown >= action_wait:
                                if attack == True or potion == True:
                                    monster2.attack(swordman)
                                    current_fighter += 1
                                    action_cooldown = 0
                                if potion == True:
                                    check += 1
                if swordman.alive == True:
                    if current_fighter == 2:
                        action_cooldown += 1
                        if action_cooldown >= action_wait:
                            if check == 1:
                                swordman.attack(monster2)
                                current_fighter += 1
                                action_cooldown = 0
                            else:
                                if swordman.potion > 0:
                                    if swordman.max_hp - swordman.hp > potion_heal:
                                        heal = potion_heal
                                    else:
                                        heal = swordman.max_hp - swordman.hp
                                    swordman.hp += heal
                                    swordman.potion -= 1
                                    current_fighter += 1
                                    action_cooldown = 0
                                    check = 1
                                else:
                                    check = 1
            if current_fighter > total_fighter:
                current_fighter = 1
        elif char2:
            archer.update()
            archer.draw()
            archer_hpbar.draw(archer.hp)
            draw_text(f'{archer.name} HP: {archer.hp}', font, white, 100, 180)
            if archer.speed >= monster2.speed:
                if archer.alive == True:
                    if current_fighter == 1:
                        action_cooldown += 1
                        if action_cooldown >= action_wait:
                            archer.attack(monster2)
                            current_fighter += 1
                            action_cooldown = 0
                if current_fighter == 2:
                    if monster2.alive == True:
                        action_cooldown += 1
                        if action_cooldown >= action_wait:
                            monster2.attack(archer)
                            current_fighter += 1
                            action_cooldown = 0
            if archer.speed < monster2.speed:
                if current_fighter == 1:
                    if monster2.alive == True:
                        action_cooldown += 1
                        if action_cooldown >= action_wait:
                            monster2.attack(archer)
                            current_fighter += 1
                            action_cooldown = 0
                if archer.alive == True:
                    if current_fighter == 2:
                        action_cooldown += 1
                        if action_cooldown >= action_wait:
                            archer.attack(monster2)
                            current_fighter += 1
                            action_cooldown = 0
            if current_fighter > total_fighter:
                current_fighter = 1
        elif char3:
            assasin.update()
            assasin.draw()
            ass_hpbar.draw(assasin.hp)
            draw_text(f'{assasin.name} HP: {assasin.hp}', font, white, 100, 180)
            if assasin.speed >= monster2.speed:
                if assasin.alive == True:
                    if current_fighter == 1:
                        action_cooldown += 1
                        if action_cooldown >= action_wait:
                            assasin.attack(monster2)
                            current_fighter += 1
                            action_cooldown = 0
                if current_fighter == 2:
                    if monster2.alive == True:
                        action_cooldown += 1
                        if action_cooldown >= action_wait:
                            monster2.attack(assasin)
                            current_fighter += 1
                            action_cooldown = 0
            if assasin.speed < monster2.speed:
                if current_fighter == 1:
                    if monster2.alive == True:
                        action_cooldown += 1
                        if action_cooldown >= action_wait:
                            monster2.attack(assasin)
                            current_fighter += 1
                            action_cooldown = 0
                if assasin.alive == True:
                    if current_fighter == 2:
                        action_cooldown += 1
                        if action_cooldown >= action_wait:
                            assasin.attack(monster2)
                            current_fighter += 1
                            action_cooldown = 0
            if current_fighter > total_fighter:
                current_fighter = 1
        else:
            witch.update()
            witch.draw()
            witch_hpbar.draw(witch.hp)
            draw_text(f'{witch.name} HP: {witch.hp}', font, white, 100, 180)
            if witch.speed >= monster2.speed:
                if witch.alive == True:
                    if current_fighter == 1:
                        action_cooldown += 1
                        if action_cooldown >= action_wait:
                            witch.attack(monster2)
                            current_fighter += 1
                            action_cooldown = 0
                if current_fighter == 2:
                    if monster2.alive == True:
                        action_cooldown += 1
                        if action_cooldown >= action_wait:
                            monster2.attack(witch)
                            current_fighter += 1
                            action_cooldown = 0
            if witch.speed < monster2.speed:
                if current_fighter == 1:
                    if monster2.alive == True:
                        action_cooldown += 1
                        if action_cooldown >= action_wait:
                            monster2.attack(witch)
                            current_fighter += 1
                            action_cooldown = 0
                if witch.alive == True:
                    if current_fighter == 2:
                        action_cooldown += 1
                        if action_cooldown >= action_wait:
                            witch.attack(monster2)
                            current_fighter += 1
                            action_cooldown = 0
            if current_fighter > total_fighter:
                current_fighter = 1
        pygame.display.update()

bg_3 = pygame.image.load('bg_3.jpg')
bg_3 = pygame.transform.scale(bg_3,(1400,900))
def Background_3(char1, char2, char3, coin):
    current_fighter = 1
    total_fighter = 2
    action_cooldown = 0
    action_wait = 90
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    Background_4(char1, char2, char3)

        screen.blit(bg_3,(0,0))
        monster3.update()
        monster3.draw()
        draw_text(f'{monster3.name} HP: {monster3.hp}', font, white, 1000, 180)
        mon3_hpbar.draw(monster3.hp)
        screen.blit(money,(1150,100))
        draw_text('%d' %coin, font, white , 1200, 100)
        if char1:
            swordman.update()
            swordman.draw()
            sword_hpbar.draw(swordman.hp)
            draw_text(f'{swordman.name} HP: {swordman.hp}', font, white, 100, 180)
            if swordman.speed >= monster3.speed:
                if swordman.alive == True:
                    if current_fighter == 1:
                        action_cooldown += 1
                        if action_cooldown >= action_wait:
                            swordman.attack(monster3)
                            current_fighter += 1
                            action_cooldown = 0
                if current_fighter == 2:
                    if monster3.alive == True:
                        action_cooldown += 1
                        if action_cooldown >= action_wait:
                            monster3.attack(swordman)
                            current_fighter += 1
                            action_cooldown = 0
            if swordman.speed < monster3.speed:
                if current_fighter == 1:
                    if monster3.alive == True:
                        action_cooldown += 1
                        if action_cooldown >= action_wait:
                            monster3.attack(swordman)
                            current_fighter += 1
                            action_cooldown = 0
                if swordman.alive == True:
                    if current_fighter == 2:
                        action_cooldown += 1
                        if action_cooldown >= action_wait:
                            swordman.attack(monster3)
                            current_fighter += 1
                            action_cooldown = 0
            if current_fighter > total_fighter:
                current_fighter = 1
        elif char2:
            archer.update()
            archer.draw()
            archer_hpbar.draw(archer.hp)
            draw_text(f'{archer.name} HP: {archer.hp}', font, white, 100, 180)
            if archer.speed >= monster3.speed:
                if archer.alive == True:
                    if current_fighter == 1:
                        action_cooldown += 1
                        if action_cooldown >= action_wait:
                            archer.attack(monster3)
                            current_fighter += 1
                            action_cooldown = 0
                if current_fighter == 2:
                    if monster3.alive == True:
                        action_cooldown += 1
                        if action_cooldown >= action_wait:
                            monster3.attack(archer)
                            current_fighter += 1
                            action_cooldown = 0
            if archer.speed < monster3.speed:
                if current_fighter == 1:
                    if monster3.alive == True:
                        action_cooldown += 1
                        if action_cooldown >= action_wait:
                            monster3.attack(archer)
                            current_fighter += 1
                            action_cooldown = 0
                if archer.alive == True:
                    if current_fighter == 2:
                        action_cooldown += 1
                        if action_cooldown >= action_wait:
                            archer.attack(monster3)
                            current_fighter += 1
                            action_cooldown = 0
            if current_fighter > total_fighter:
                current_fighter = 1
        elif char3:
            assasin.update()
            assasin.draw()
            ass_hpbar.draw(assasin.hp)
            draw_text(f'{assasin.name} HP: {assasin.hp}', font, white, 100, 180)
            if assasin.speed >= monster3.speed:
                if assasin.alive == True:
                    if current_fighter == 1:
                        action_cooldown += 1
                        if action_cooldown >= action_wait:
                            assasin.attack(monster3)
                            current_fighter += 1
                            action_cooldown = 0
                if current_fighter == 2:
                    if monster3.alive == True:
                        action_cooldown += 1
                        if action_cooldown >= action_wait:
                            monster3.attack(assasin)
                            current_fighter += 1
                            action_cooldown = 0
            if assasin.speed < monster3.speed:
                if current_fighter == 1:
                    if monster3.alive == True:
                        action_cooldown += 1
                        if action_cooldown >= action_wait:
                            monster3.attack(assasin)
                            current_fighter += 1
                            action_cooldown = 0
                if assasin.alive == True:
                    if current_fighter == 2:
                        action_cooldown += 1
                        if action_cooldown >= action_wait:
                            assasin.attack(monster3)
                            current_fighter += 1
                            action_cooldown = 0
            if current_fighter > total_fighter:
                current_fighter = 1
        else:
            witch.update()
            witch.draw()
            witch_hpbar.draw(witch.hp)
            draw_text(f'{witch.name} HP: {witch.hp}', font, white, 100, 180)
            if witch.speed >= monster3.speed:
                if witch.alive == True:
                    if current_fighter == 1:
                        action_cooldown += 1
                        if action_cooldown >= action_wait:
                            witch.attack(monster3)
                            current_fighter += 1
                            action_cooldown = 0
                if current_fighter == 2:
                    if monster3.alive == True:
                        action_cooldown += 1
                        if action_cooldown >= action_wait:
                            monster3.attack(witch)
                            current_fighter += 1
                            action_cooldown = 0
            if witch.speed < monster3.speed:
                if current_fighter == 1:
                    if monster3.alive == True:
                        action_cooldown += 1
                        if action_cooldown >= action_wait:
                            monster3.attack(witch)
                            current_fighter += 1
                            action_cooldown = 0
                if witch.alive == True:
                    if current_fighter == 2:
                        action_cooldown += 1
                        if action_cooldown >= action_wait:
                            witch.attack(monster3)
                            current_fighter += 1
                            action_cooldown = 0
            if current_fighter > total_fighter:
                current_fighter = 1
        pygame.display.update()

bg_4 = pygame.image.load('bg_4.jpg')
bg_4 = pygame.transform.scale(bg_4,(1400,900))
def Background_4(char1, char2, char3):
    current_fighter = 1
    total_fighter = 2
    action_cooldown = 0
    action_wait = 90
    archer = char(300, 670, 'Archer', 8, 4, 1, potion_have, 0.5)
    assasin = char(300, 670, 'Assasin', 7, 3, 1, potion_have, 0.5)
    witch = char(300, 670, 'Witch', 7, 5, 1, potion_have, 0.5)
    swordman = char(300, 670, 'Swordman', 10, 2, 4, potion_have, 0.5)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    Background_5(char1, char2, char3)

        screen.blit(bg_4,(0,0))
        monster4.update()
        monster4.draw()
        draw_text(f'{monster4.name} HP: {monster4.hp}', font, white, 1000, 180)
        mon4_hpbar.draw(monster4.hp)
        if char1:
            swordman.update()
            swordman.draw()
            sword_hpbar.draw(swordman.hp)
            draw_text(f'{swordman.name} HP: {swordman.hp}', font, white, 100, 180)
        elif char2:
            archer.update()
            archer.draw()
            archer_hpbar.draw(archer.hp)
            draw_text(f'{archer.name} HP: {archer.hp}', font, white, 100, 180)
        elif char3:
            assasin.update()
            assasin.draw()
            ass_hpbar.draw(assasin.hp)
            draw_text(f'{assasin.name} HP: {assasin.hp}', font, white, 100, 180)
        else:
            witch.update()
            witch.draw()
            witch_hpbar.draw(witch.hp)
            draw_text(f'{witch.name} HP: {witch.hp}', font, white, 100, 180)
        pygame.display.update()
        
bg_5 = pygame.image.load('bg_5.jpg')
bg_5 = pygame.transform.scale(bg_5,(1400,900))
def Background_5(char1, char2, char3):
    current_fighter = 1
    total_fighter = 2
    action_cooldown = 0
    action_wait = 90
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    Background_6(char1, char2, char3)

        screen.blit(bg_5,(0,0))
        monster5.draw()
        monster5.update()
        draw_text(f'{monster5.name} HP: {monster5.hp}', font, white, 1000, 180)
        mon5_hpbar.draw(monster5.hp)
        if char1:
            swordman.update()
            swordman.draw()
            sword_hpbar.draw(swordman.hp)
            draw_text(f'{swordman.name} HP: {swordman.hp}', font, white, 100, 180)
        elif char2:
            archer.update()
            archer.draw()
            archer_hpbar.draw(archer.hp)
            draw_text(f'{archer.name} HP: {archer.hp}', font, white, 100, 180)
        elif char3:
            assasin.update()
            assasin.draw()
            ass_hpbar.draw(assasin.hp)
            draw_text(f'{assasin.name} HP: {assasin.hp}', font, white, 100, 180)
        else:
            witch.update()
            witch.draw()
            witch_hpbar.draw(witch.hp)
            draw_text(f'{witch.name} HP: {witch.hp}', font, white, 100, 180)
        pygame.display.update()

bg_6 = pygame.image.load('bg_6.jpg')
bg_6 = pygame.transform.scale(bg_6,(1400,900))
def Background_6(char1, char2, char3):
    current_fighter = 1
    total_fighter = 2
    action_cooldown = 0
    action_wait = 90
    archer = char(300, 700, 'Archer', 8, 4, 1, 0.5)
    assasin = char(300, 700, 'Assasin', 7, 3, 1, 0.5)
    witch = char(300, 700, 'Witch', 7, 5, 1, 0.5)
    swordman = char(300, 700, 'Swordman', 10, 2, 4, 0.5)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    Background_7(char1, char2, char3)

        screen.blit(bg_6,(0,0))
        monster6.update()
        monster6.draw()
        draw_text(f'{monster6.name} HP: {monster6.hp}', font, white, 1000, 180)
        mon6_hpbar.draw(monster6.hp)
        if char1:
            swordman.update()
            swordman.draw()
            sword_hpbar.draw(swordman.hp)
            draw_text(f'{swordman.name} HP: {swordman.hp}', font, white, 100, 180)
        elif char2:
            archer.update()
            archer.draw()
            archer_hpbar.draw(archer.hp)
            draw_text(f'{archer.name} HP: {archer.hp}', font, white, 100, 180)
        elif char3:
            assasin.update()
            assasin.draw()
            ass_hpbar.draw(assasin.hp)
            draw_text(f'{assasin.name} HP: {assasin.hp}', font, white, 100, 180)
        else:
            witch.update()
            witch.draw()
            witch_hpbar.draw(witch.hp)
            draw_text(f'{witch.name} HP: {witch.hp}', font, white, 100, 180)
        pygame.display.update()

bg_7 = pygame.image.load('bg_7.png')
bg_7 = pygame.transform.scale(bg_7,(1400,900))
def Background_7(char1, char2, char3):
    current_fighter = 1
    total_fighter = 2
    action_cooldown = 0
    action_wait = 90
    archer = char(300, 600, 'Archer', 8, 4, 1, 0.5)
    assasin = char(300, 600, 'Assasin', 7, 3, 1, 0.5)
    witch = char(300, 600, 'Witch', 7, 5, 1, 0.5)
    swordman = char(300, 600, 'Swordman', 10, 2, 4, 0.5)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    Background_8(char1, char2, char3)

        screen.blit(bg_7,(0,0))
        monster7.update()
        monster7.draw()
        draw_text(f'{monster7.name} HP: {monster7.hp}', font, white, 1000, 180)
        mon7_hpbar.draw(monster7.hp)
        if char1:
            swordman.update()
            swordman.draw()
            sword_hpbar.draw(swordman.hp)
            draw_text(f'{swordman.name} HP: {swordman.hp}', font, white, 100, 180)
        elif char2:
            archer.update()
            archer.draw()
            archer_hpbar.draw(archer.hp)
            draw_text(f'{archer.name} HP: {archer.hp}', font, white, 100, 180)
        elif char3:
            assasin.update()
            assasin.draw()
            ass_hpbar.draw(assasin.hp)
            draw_text(f'{assasin.name} HP: {assasin.hp}', font, white, 100, 180)
        else:
            witch.update()
            witch.draw()
            witch_hpbar.draw(witch.hp)
            draw_text(f'{witch.name} HP: {witch.hp}', font, white, 100, 180)
        pygame.display.update()

bg_8 = pygame.image.load('bg_8.png')
bg_8 = pygame.transform.scale(bg_8,(1400,900))
def Background_8(char1, char2, char3):
    current_fighter = 1
    total_fighter = 2
    action_cooldown = 0
    action_wait = 90
    archer = char(460, 520, 'Archer', 8, 4, 1, 0.5)
    assasin = char(460, 520, 'Assasin', 7, 3, 1, 0.5)
    witch = char(460, 520, 'Witch', 7, 5, 1, 0.5)
    swordman = char(460, 520, 'Swordman', 10, 2, 4, 0.5)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    quit()

        screen.blit(bg_8,(0,0))
        monster8.draw()
        monster8.update()
        draw_text(f'{monster8.name} HP: {monster8.hp}', font, white, 1000, 180)
        mon8_hpbar.draw(monster8.hp)
        if char1:
            swordman.update()
            swordman.draw()
            sword_hpbar.draw(swordman.hp)
            draw_text(f'{swordman.name} HP: {swordman.hp}', font, white, 100, 180)
        elif char2:
            archer.update()
            archer.draw()
            archer_hpbar.draw(archer.hp)
            draw_text(f'{archer.name} HP: {archer.hp}', font, white, 100, 180)
        elif char3:
            assasin.update()
            assasin.draw()
            ass_hpbar.draw(assasin.hp)
            draw_text(f'{assasin.name} HP: {assasin.hp}', font, white, 100, 180)
        else:
            witch.update()
            witch.draw()
            witch_hpbar.draw(witch.hp)
            draw_text(f'{witch.name} HP: {witch.hp}', font, white, 100, 180)
        pygame.display.update()

intro()
story()
