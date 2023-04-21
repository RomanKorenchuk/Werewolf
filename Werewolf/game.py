from pygame import *
init()

class GameSprite(sprite.Sprite):
    def __init__(self, picture, w, h, x, y):
        super().__init__()
        self.image = transform.scale(image.load(picture), [w, h])
        self.rect = self.image.get_rect()
        self.picture = picture
        self.w = w
        self.h = h
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        mw.blit(self.image, self.rect)

class Player(sprite.Sprite):
    def __init__(self, pictures, w, h, x, y, x_speed, y_speed, position, move):
        self.pictures = pictures
        self.image = transform.scale(image.load(pictures[move]), [w, h])
        self.move = move
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = self.x
        self.rect.y = self.y
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.w = w
        self.h = h
        self.position = position

    def update(self, barriers):
        if self.rect.x <= 1500-78 and self.x_speed > 0 or self.rect.x >= 0 and self.x_speed < 0:
            self.rect.x += self.x_speed
        platforms_touched = sprite.spritecollide(self, barriers, False)
        if self.x_speed > 0:
            for p in platforms_touched:
                self.rect.right = min(self.rect.right, p.rect.left)
        elif self.x_speed < 0:
            for p in platforms_touched:
                self.rect.left = max(self.rect.left, p.rect.right)
        if self.rect.y <= 900-103 and self.y_speed > 0 or self.rect.y >= 0 and self.y_speed < 0:
            self.rect.y += self.y_speed
        platforms_touched = sprite.spritecollide(self, barriers, False)
        if self.y_speed > 0: 
            for p in platforms_touched:
                self.y_speed = 0              
                if p.rect.top - 100 < self.rect.bottom:
                    self.rect.bottom = p.rect.top
        elif self.y_speed < 0: 
            for p in platforms_touched:
                self.y_speed = 0
                self.rect.top = max(self.rect.top, p.rect.bottom)
        
        self.x_speed = 0
        self.y_speed = 0

    def rect_x(self):
        return self.rect.x
    
    def rect_y(self):
        return self.rect.y
    def level_update(self, level):
        if level == 2:
            self.rect.y = 770
        if level == 1:
            self.rect.y = 20

    def draw(self):
        if self.position == 0:
            mw.blit(self.image,(self.rect.x,self.rect.y))
        elif self.position == 1:
            mw.blit(transform.flip(self.image,True,False),(self.rect.x,self.rect.y))
    
    def moves(self):
        self.image = transform.scale(image.load(self.pictures[self.move]), [self.w, self.h])
    
class Colide(GameSprite):
    def __init__(self, picture, w, h, x, y, x_speed, y_speed):
        GameSprite.__init__(self, picture, w, h, x, y)
        self.x_speed = x_speed
        self.y_speed = y_speed
    def update(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed
        self.x_speed = 0
        self.y_speed = 0

class Button(GameSprite):
    def __init__(self, picture, w, h, x, y):
        GameSprite.__init__(self, picture, w, h, x, y)
        self.x = x
        self.y = y

    def colidepoint(self, x, y):
        return self.rect.collidepoint(x, y)
   
'''class Enemy(Player):
    def __init__(self, pictures, w, h, x, y, x_speed, y_speed, position, move):
        Player.__init__(self, picture, w, h, x, y, x_speed, y_speed, position, move)
        self.pictures = pictures
        self.image = transform.scale(image.load(pictures[move]), [w, h])
        self.move = move
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = self.x
        self.rect.y = self.y
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.w = w
        self.h = h
        self.position = position'''

mw = display.set_mode((1500, 900))
display.set_caption(("Werewolf"))

#test_level:
picture = image.load("Assets/Temnosiri_fon_light.jpg").convert()
picture = transform.scale(picture, [3000, 2700])

barriers = sprite.Group()

lights = sprite.Group()
light_1 = GameSprite('Assets/Temnosiri_fon.jpg', 525, 235, 380, 240)
light_2 = GameSprite('Assets/Temnosiri_fon.jpg', 179, 250, 560, 470)
lights.add(light_1)
lights.add(light_2)

#level_1:
fon_1 = image.load("Assets/Fon.png").convert()
fon_1 = transform.scale(fon_1, [750, 450])

#групки спрайтів 1:
barriers_1 = sprite.Group()
kushchi_1 = sprite.Group()
trees_1 = sprite.Group()
objects = sprite.Group()

#дерева:
tree_1 = GameSprite("Assets/Trees/Tree_1.png", 186, 272, -10, -10)
tree_2 = GameSprite("Assets/Trees/Tree_2.png", 238, 238, 10, 100)
tree_3 = GameSprite("Assets/Trees/Tree_3.png", 172, 248, 30, 210)
tree_4 = GameSprite("Assets/Trees/Tree_4.png", 196, 250, 170, -30)
tree_5 = GameSprite("Assets/Trees/Tree_5.png", 172, 272, 210, 150)
tree_6 = GameSprite("Assets/Trees/Tree_6.png", 190, 254, 500, 400)
tree_7 = GameSprite("Assets/Trees/Tree_7.png", 168, 238, 600, 450)
tree_8 = GameSprite("Assets/Trees/Tree_8.png", 176, 246, 430, 520)
tree_9 = GameSprite("Assets/Trees/Tree_9.png", 166, 274, 510, 570)
tree_10 = GameSprite("Assets/Trees/Tree_10.png", 180, 270, 600, 620)
tree_11 = GameSprite("Assets/Trees/Tree_1.png", 186, 272, 620, 360)
tree_12 = GameSprite("Assets/Trees/Tree_2.png", 238, 238, 350, 650)
tree_13 = GameSprite("Assets/Trees/Tree_3.png", 172, 248, 750, 350)
tree_14 = GameSprite("Assets/Trees/Tree_4.png", 196, 250, 700, -50)
tree_15 = GameSprite("Assets/Trees/Tree_5.png", 172, 272, 650, 0)
tree_16 = GameSprite("Assets/Trees/Tree_6.png", 190, 254, 750, 50)
tree_17 = GameSprite("Assets/Trees/Tree_7.png", 168, 238, 1350, -100)
tree_18 = GameSprite("Assets/Trees/Tree_8.png", 176, 246, 1250, -80)
tree_19 = GameSprite("Assets/Trees/Tree_9.png", 166, 274, 1320, 50)
tree_20 = GameSprite("Assets/Trees/Tree_10.png", 180, 270, 1350, 230)
tree_21 = GameSprite("Assets/Trees/Tree_1.png", 186, 272, 850, -80)

trees_1.add(tree_1)
trees_1.add(tree_2)
trees_1.add(tree_3)
trees_1.add(tree_4)
trees_1.add(tree_5)
trees_1.add(tree_11)
trees_1.add(tree_13)
trees_1.add(tree_6)
trees_1.add(tree_7)
trees_1.add(tree_8)
trees_1.add(tree_9)
trees_1.add(tree_10)
trees_1.add(tree_12)
trees_1.add(tree_21)
trees_1.add(tree_14)
trees_1.add(tree_15)
trees_1.add(tree_16)
trees_1.add(tree_17)
trees_1.add(tree_18)
trees_1.add(tree_19)
trees_1.add(tree_20)
#невидимі барєри:
nevidimka_1 = GameSprite("Assets/Colide.jpg", 380, 150, 0, 0)
nevidimka_2 = GameSprite("Assets/Colide.jpg", 330, 420, 0, 0)
nevidimka_3 = GameSprite("Assets/Colide.jpg", 160, 460, 0, 0)
nevidimka_4 = GameSprite("Assets/Colide.jpg", 380, 10, 450, 600)
nevidimka_13 = GameSprite("Assets/Colide.jpg", 10, 300, 450, 600)
nevidimka_5 = GameSprite("Assets/Colide.jpg", 30, 30, 830, 570)
nevidimka_6 = GameSprite("Assets/Colide.jpg", 190, 280, 670, 0)
nevidimka_7 = GameSprite("Assets/Colide.jpg", 280, 200, 670, 0)
nevidimka_8 = GameSprite("Assets/Colide.jpg", 10, 10, 840, 300)
nevidimka_9 = GameSprite("Assets/Colide.jpg", 150, 350, 1380, 0)
nevidimka_10 = GameSprite("Assets/Colide.jpg", 200, 60, 1140, 220)
nevidimka_11 = GameSprite("Assets/Colide.jpg", 200, 200, 1330, 0)
nevidimka_12 = GameSprite("Assets/Colide.jpg", 20, 20, 1425, 480)
nevidimka_level_2 = GameSprite("Assets/Colide.jpg", 50, 10, 540, 0)
nevidimka_level_1 = GameSprite("Assets/Colide.jpg", 50, 10, 540, 899)
barriers_1.add(nevidimka_1)
barriers_1.add(nevidimka_2)
barriers_1.add(nevidimka_3)
barriers_1.add(nevidimka_4)
barriers_1.add(nevidimka_5)
barriers_1.add(nevidimka_6)
barriers_1.add(nevidimka_7)
barriers_1.add(nevidimka_8)
barriers_1.add(nevidimka_9)
barriers_1.add(nevidimka_10)
barriers_1.add(nevidimka_11)
barriers_1.add(nevidimka_12)

#кущі і камні:
kushch_1 = GameSprite("Assets/Greens/Kushch_1.png",100, 100, 250, 250)
kushch_2 = GameSprite("Assets/Greens/Kushch_2.png",100, 100, 750, 600)
kushch_3 = GameSprite("Assets/Greens/Kushch_3.png",100, 100, 300, 50)
kushch_4 = GameSprite("Assets/Greens/Kushch_1.png",100, 100, 450, 770)
kushch_5 = GameSprite("Assets/Greens/Kushch_2.png",100, 100, 150, 300)
kushch_6 = GameSprite("Assets/Greens/Kushch_3.png",100, 100, -10, 350)
kushch_7 = GameSprite("Assets/Greens/Kushch_1.png",100, 100, 650, 150)
kushch_8 = GameSprite("Assets/Greens/Kushch_2.png",100, 100, 150, 300)
kushch_9 = GameSprite("Assets/Greens/Kushch_3.png",100, 100, -10, 350)
rock = GameSprite("Assets/Rock.png", 200, 125, 1150, 150)
kushchi_1.add(kushch_1)
kushchi_1.add(kushch_2)
kushchi_1.add(kushch_3)
kushchi_1.add(kushch_4)
kushchi_1.add(kushch_5)
kushchi_1.add(kushch_6)
kushchi_1.add(kushch_7)
kushchi_1.add(kushch_8)
kushchi_1.add(kushch_9)
kushchi_1.add(rock)

car = GameSprite("Assets/Car.png", 300, 100, 100, 700)
car_colide = GameSprite("Assets/Colide.jpg", 340, 140, 80, 680)
tablichka = GameSprite("Assets/Tablichka.png", 65, 100, 400, 50)
park_txt = GameSprite("Assets/Park.png", 402, 75, 600, 700)
tablichka_colide = GameSprite("Assets/Colide.jpg",100, 135, 400, 50)
tent_1 = GameSprite("Assets/Tent_orange.png", 184, 140, 1200, 700)
tent_2 = GameSprite("Assets/Tent_y.png", 210, 180, 780, 650)
tent_3 = GameSprite("Assets/Tent_p.png", 150, 140, 1050, 590)
fire = GameSprite("Assets/fire.png", 56, 70, 1050, 750)
pazori = GameSprite("Assets/Wolf_pazori.png", 75, 75, 820, 690)
head = GameSprite("Assets/head.png", 40, 28, 1150, 200)
strilka_lvl_1 = GameSprite("Assets/Strilka_lvl_1.png", 50, 50, 550, 20)

barriers_1.add(car)
barriers_1.add(tablichka)
barriers_1.add(tent_1)
barriers_1.add(tent_2)
barriers_1.add(tent_3)
barriers_1.add(fire)

objects.add(car)
objects.add(tablichka)
objects.add(tent_1)
objects.add(tent_2)
objects.add(tent_3)
objects.add(fire)
objects.add(pazori)
#objects.add(car)

#діалоги:
camerman_dlg_1 = GameSprite("Assets/Dialogue/Camerman_dlg_1.png", 780, 156, 0, 744)
camerman_dlg_2 = GameSprite("Assets/Dialogue/Camerman_dlg_2.png", 780, 156, 0, 744)
camerman_dlg_3 = GameSprite("Assets/Dialogue/Camerman_dlg_3.png", 780, 156, 0, 744)
camerman_dlg_4 = GameSprite("Assets/Dialogue/Camerman_dlg_4.png", 780, 156, 0, 744)
werewolf_dlg_1 = GameSprite("Assets/Dialogue/Werewolf_dlg_1.png", 780, 156, 720, 744)

#обєкти для виклику діалогів:
colide_dialogue_1 = GameSprite("Assets/Colide.jpg", 200, 200, 0, 400)
colide_dialogue_2 = GameSprite("Assets/Colide.jpg", 600, 300, 800, 600)
colide_dialogue_3 = GameSprite("Assets/Colide.jpg", 250, 200, 1050, 100)

#квадрати доказів:
dokaz_1 = GameSprite("Assets/dokazi.png", 50, 50, 10, 10)
dokaz_2 = GameSprite("Assets/dokazi.png", 50, 50, 70, 10)
dokaz_3 = GameSprite("Assets/dokazi.png", 50, 50, 130, 10)
dokaz_4 = GameSprite("Assets/dokazi.png", 50, 50, 190, 10)

#level_2:
#грпки спрайтів:
barriers_2 = sprite.Group()
kushchi_2 = sprite.Group()
trees_2 = sprite.Group()
objects_2 = sprite.Group()

#дерева:
tree_1 = GameSprite("Assets/Trees/Tree_1.png", 186, 272, -50, -10)
tree_2 = GameSprite("Assets/Trees/Tree_2.png", 238, 238, 10, 100)
tree_3 = GameSprite("Assets/Trees/Tree_3.png", 172, 248, 80, 130)
tree_4 = GameSprite("Assets/Trees/Tree_4.png", 196, 250, 170, -30)
tree_5 = GameSprite("Assets/Trees/Tree_5.png", 172, 272, 0, 200)
tree_6 = GameSprite("Assets/Trees/Tree_6.png", 190, 254, -10, 400)
tree_7 = GameSprite("Assets/Trees/Tree_7.png", 168, 238, 60, 550)
tree_8 = GameSprite("Assets/Trees/Tree_8.png", 176, 246, 50, 550)
tree_9 = GameSprite("Assets/Trees/Tree_9.png", 166, 274, -20, 600)
tree_10 = GameSprite("Assets/Trees/Tree_10.png", 180, 270, 110, 620)
tree_11 = GameSprite("Assets/Trees/Tree_1.png", 186, 272, 210, 630)#дерево яке можливо теж буде падати
tree_12 = GameSprite("Assets/Trees/Tree_9.png", 166, 274, 600, 620)#дерево яке має падати
tree_13 = GameSprite("Assets/Trees/Tree_3.png", 172, 248, 700, 550)
tree_14 = GameSprite("Assets/Trees/Tree_4.png", 196, 250, 800, 630)
tree_15 = GameSprite("Assets/Trees/Tree_5.png", 172, 272, 880, 550)
tree_16 = GameSprite("Assets/Trees/Tree_6.png", 190, 254, 950, 630)
tree_17 = GameSprite("Assets/Trees/Tree_7.png", 168, 238, 1350, -100)
tree_18 = GameSprite("Assets/Trees/Tree_8.png", 176, 246, 1250, -80)
tree_19 = GameSprite("Assets/Trees/Tree_9.png", 166, 274, 1320, 50)
tree_20 = GameSprite("Assets/Trees/Tree_10.png", 180, 270, 1350, 230)
trees_2.add(tree_1)
trees_2.add(tree_2)
trees_2.add(tree_3)
trees_2.add(tree_4)
trees_2.add(tree_5)
trees_2.add(tree_6)
trees_2.add(tree_7)
trees_2.add(tree_8)
trees_2.add(tree_9)
trees_2.add(tree_10)
trees_2.add(tree_11)
trees_2.add(tree_13)
trees_2.add(tree_14)
trees_2.add(tree_12)
trees_2.add(tree_15)
trees_2.add(tree_16)
trees_2.add(tree_17)
trees_2.add(tree_18)
trees_2.add(tree_19)
trees_2.add(tree_20)

#кущі:
kushch_1 = GameSprite("Assets/Greens/Kushch_1.png",100, 100, 720, 800)
kushch_2 = GameSprite("Assets/Greens/Kushch_2.png",100, 100, 200, 750)
kushch_3 = GameSprite("Assets/Greens/Kushch_3.png",100, 100, 300, 50)
kushchi_2.add(kushch_1)
kushchi_2.add(kushch_2)
kushchi_2.add(kushch_3)

#Невидимі барєри:
nevidimka_1 = GameSprite("Assets/Colide.jpg",380, 150, 0, 0)
nevidimka_2 = GameSprite("Assets/Colide.jpg", 280, 220, 0, 0)
nevidimka_3 = GameSprite("Assets/Colide.jpg", 190, 380, 0, 0)
nevidimka_4 = GameSprite("Assets/Colide.jpg", 110, 470, 0, 0)
nevidimka_5 = GameSprite("Assets/Colide.jpg", 310, 140, 0, 760)
nevidimka_6 = GameSprite("Assets/Colide.jpg", 110, 150, 0, 630)
nevidimka_7 = GameSprite("Assets/Colide.jpg", 400, 50, 660, 850)
nevidimka_8 = GameSprite("Assets/Colide.jpg", 200, 100, 780, 780)
nevidimka_9 = GameSprite("Assets/Colide.jpg", 150, 350, 1380, 0)
nevidimka_10 = GameSprite("Assets/Colide.jpg", 200, 200, 1330, 0)
nevidimka_11 = GameSprite("Assets/Colide.jpg", 30, 20, 1425, 480)

barriers_2.add(nevidimka_1)
barriers_2.add(nevidimka_2)
barriers_2.add(nevidimka_3)
barriers_2.add(nevidimka_4)
barriers_2.add(nevidimka_5)
barriers_2.add(nevidimka_6)
barriers_2.add(nevidimka_7)
barriers_2.add(nevidimka_8)
barriers_2.add(nevidimka_9)
barriers_2.add(nevidimka_10)
barriers_2.add(nevidimka_11)

strilka_lvl_2 = GameSprite("Assets/Strilka_lvl_2.png", 50, 50, 550, 830)


camerman_pictures = list()
for i in range(15):
    i += 1
    camerman_pictures.append("Assets/Camerman/Camerman_move_" + str(i) + ".png")
camerman = Player(camerman_pictures, 78, 103, 100, 500, 0, 0, 0, 0)
# 78, 103

werewolf_pictures = list()
for i in range(4):
    i += 1
    werewolf_pictures.append("Assets/Werewolf/Werewolfs_move_" + str(i) + ".png")
werewolf = Player(werewolf_pictures, 165, 168, 900, 100, 0, 0, 1, 0)
#165, 168

svidok_pictures = list()
for i in range(9):
    svidok_pictures.append("Assets/Svidok/Svidok_move_" + str(i) + ".png")
    i += 1
svidok = Player(svidok_pictures, 84, 104, 1210, 110, 0, 0, 0, 0)
svidok_stop = GameSprite("Assets/Svidok/Svidok_move_0.png", 84, 104, 1210, 110)
klitka = GameSprite("Assets/Klitka.png", 150, 150, 1175, 75)

#звуки:
s_camera = mixer.Sound("sounds/Fotka.ogg")
s_werewolf = mixer.Sound("sounds/Werewolf_sound.ogg")
s_dokaz = mixer.Sound("sounds/Dokaz_sound.ogg")
s_werewolf_angry = mixer.Sound("sounds/Werwolf_angry.ogg")
s_zamok = mixer.Sound("sounds/Zamok_sound.ogg")
s_car = mixer.Sound("sounds/Car_sound.ogg")
s_car_start = mixer.Sound("sounds/Car_start_sound.ogg")

clock = time.Clock()
run = True
finish = False
level_1 = True
level_2 = False
escape = False
start_sound = True
loose_sound = True
win_sound = True
d_1 = 0
d_2 = 0
d_3 = 0
d_4 = 0
dokazi = 0
werewolf_dlg = False
j = 0
k = 0

while run:
    time.delay(50)
    for e in event.get():
        if e.type == QUIT:
            run = False
    if start_sound:
        s_werewolf.play()
        start_sound = False
    keys = key.get_pressed()
    if keys[K_a] or keys[K_w] or keys[K_s] or keys[K_d]:
        camerman.move += 1       
    if camerman.move >= 15:
        camerman.move = 0
    if keys[K_a] and keys[K_w]:
        camerman.x_speed = -10
        camerman.y_speed = -10
        camerman.position = 1
    elif keys[K_a] and keys[K_s]:
        camerman.x_speed = -10
        camerman.y_speed = 10
        camerman.position = 1
    elif keys[K_d] and keys[K_w]:
        camerman.x_speed = 10
        camerman.y_speed = -10
        camerman.position = 0
    elif keys[K_s] and keys[K_d]:
        camerman.x_speed = 10
        camerman.y_speed = 10
        camerman.position = 0 
    elif keys[K_a]:
        camerman.x_speed = -10
        camerman.position = 1
    elif keys[K_d]:
        camerman.x_speed = 10
        camerman.position = 0
    elif keys[K_w]:
        camerman.y_speed = -10
    elif keys[K_s]:
        camerman.y_speed = 10
    if (keys[K_a] or keys[K_w] or keys[K_s] or keys[K_d]) == False:
        camerman.move = 0
    if escape:
        svidok.x_speed = camerman.x_speed
        svidok.y_speed = camerman.y_speed
        svidok.position = camerman.position
        if (keys[K_a] or keys[K_w] or keys[K_s] or keys[K_d]):
            svidok.move += 1
        else:
            svidok.move = 0
        if svidok.move >= 9:
            svidok.move = 1

    '''if escape:
        if keys[K_a] or keys[K_w] or keys[K_s] or keys[K_d]:
            camerman.move += 1       
        if camerman.move >= 15:
            camerman.move = 0
        if keys[K_a] and keys[K_w]:
            camerman.x_speed = -10
            camerman.y_speed = -10
            camerman.position = 1
        elif keys[K_a] and keys[K_s]:
            camerman.x_speed = -10
            camerman.y_speed = 10
            camerman.position = 1
        elif keys[K_d] and keys[K_w]:
            camerman.x_speed = 10
            camerman.y_speed = -10
            camerman.position = 0
        elif keys[K_s] and keys[K_d]:
            camerman.x_speed = 10
            camerman.y_speed = 10
            camerman.position = 0 
        elif keys[K_a]:
            camerman.x_speed = -10
            camerman.position = 1
        elif keys[K_d]:
            camerman.x_speed = 10
            camerman.position = 0
        elif keys[K_w]:
            camerman.y_speed = -10
        elif keys[K_s]:
            camerman.y_speed = 10
        if (keys[K_a] or keys[K_w] or keys[K_s] or keys[K_d]) == False:
            camerman.move = 0'''

    move_wolf = 400 >= (camerman.rect_x() - werewolf.rect_x()) >= -400 and 400 >= (camerman.rect_y() - werewolf.rect_y()) >= -400
    if move_wolf:
        j += 1
        if j == 5:
            werewolf.move += 1
            j = 0
        if werewolf.move > 3:
            werewolf.move = 0
        if  camerman.rect_x() < werewolf.rect_x() and camerman.rect_y() < werewolf.rect_y():
            werewolf.x_speed = -5
            werewolf.y_speed = -5
            werewolf.position = 0
        elif camerman.rect_x() < werewolf.rect_x() and camerman.rect_y() > werewolf.rect_y():
            werewolf.x_speed = -5
            werewolf.y_speed = 5
            werewolf.position = 0
        elif camerman.rect_x() > werewolf.rect_x() and camerman.rect_y() < werewolf.rect_y():
            werewolf.x_speed = 5
            werewolf.y_speed = -5
            werewolf.position = 1
        elif camerman.rect_x() > werewolf.rect_x() and camerman.rect_y() > werewolf.rect_y():
            werewolf.x_speed = 5
            werewolf.y_speed = 5
            werewolf.position = 1
        elif camerman.rect_y() < werewolf.rect_y():
           werewolf.y_speed = -5
        elif camerman.rect_y() > werewolf.rect_y():
            werewolf.y_speed = 5
        elif camerman.rect_x() < werewolf.rect_x():
            werewolf.x_speed = -5
            werewolf.position = 0
        elif camerman.rect_x() > werewolf.rect_x():
            werewolf.x_speed = 5
            werewolf.position = 1

    '''if start_menu:
        fon_start_menu = transform.scale(image.load("Assets/werewolf_fon.jpg"), [1500, 900])
        mw.fill((255, 255, 255))
        mw.blit(fon_start_menu, (0, 0))
        button_story = Button("Assets/Buttons/Story_button.png", 280, 88, 1000, 250)
        button_story.reset()
        button_test_level = Button("Assets/Buttons/Test_Level_button.png", 280, 88, 1000, 400)
        button_test_level.reset()
        if e.type == MOUSEBUTTONDOWN and e.button == 1:
            x, y = e.pos
            if button_story.colidepoint(x, y):
                start_menu = False
                level_1 = True
        if e.type == MOUSEBUTTONDOWN and e.button == 1:
            x, y = e.pos
            if button_test_level.colidepoint(x, y):
                start_menu = False
                test_level = True'''
     
    '''if not level_1 and sprite.collide_rect(camerman, werewolf):
        finish = True
        test_level = False
        level_1 = False
        lose = transform.scale(image.load("Assets/game_over.jpg"), [1500, 900])
        mw.fill((255, 255, 255))
        mw.blit(lose, (0, 0))'''

    if not finish:
        mw.blit(fon_1, [0, 0])
        mw.blit(fon_1, [0, 450])
        mw.blit(fon_1, [750, 0])
        mw.blit(fon_1, [750, 450])
        if keys[K_SPACE]:
            s_camera.play()
        if level_1:
            if sprite.collide_rect(nevidimka_level_2, camerman):
                level_1 = False
                level_2 = True
                camerman.level_update(2)
                if escape:
                    svidok.level_update(2)
            #barriers_1.draw(mw)
            strilka_lvl_1.reset()
            if escape:
                svidok.draw()
                svidok.moves()
                svidok.update(barriers_1)
            camerman.draw()
            camerman.moves()
            camerman.update(barriers_1)
            head.reset()
            kushchi_1.draw(mw)
            objects.draw(mw)
            trees_1.draw(mw)
            if sprite.collide_rect(camerman, tablichka_colide):
                park_txt.reset()
            if sprite.collide_rect(colide_dialogue_1, camerman):
                camerman_dlg_1.reset()
            if sprite.collide_rect(colide_dialogue_2, camerman):
                camerman_dlg_2.reset()
                if keys[K_SPACE] and d_1 == 0:
                    dokazi += 1
                    d_1 = 1
                    s_dokaz.play()
            if sprite.collide_rect(colide_dialogue_3, camerman):
                camerman_dlg_3.reset()
                if keys[K_SPACE] and d_2 == 0:
                    dokazi += 1
                    d_2 =1
                    s_dokaz.play()
            elif sprite.collide_rect(car_colide, camerman) and keys[K_SPACE]:
                camerman_dlg_4.reset()
   
        if level_2:
            camerman.update(barriers_2)
            if sprite.collide_rect(nevidimka_level_1, camerman):
                level_2 = False
                level_1 = True
                camerman.level_update(1)
                if escape:
                    svidok.level_update(1)
            if (((camerman.position == 0 and werewolf.position == 0) or (werewolf.position == 1 and camerman.position == 1))) and move_wolf:
                if keys[K_SPACE] and d_3 == 0:
                    dokazi += 1
                    d_3 = 1
                    s_dokaz.play()
            if keys[K_f] and sprite.collide_rect(camerman, klitka):
                escape = True
            strilka_lvl_2.reset()
            if not escape:
                svidok_stop.reset()
            klitka.reset()
            if escape:
                svidok.draw()
                svidok.moves()
                svidok.update(barriers_2)
            if escape and d_4 == 0:
                dokazi += 1
                d_4 = 1
                s_dokaz.play()
                s_zamok.play()

            camerman.draw()
            camerman.moves()
            werewolf.draw()
            werewolf.moves()
            werewolf.update(barriers_2)
            kushchi_2.draw(mw)
            trees_2.draw(mw)

            #barriers_2.draw(mw)
        if dokazi == 1:
            dokaz_1.reset()
        elif dokazi == 2:
            dokaz_1.reset()
            dokaz_2.reset()
        elif dokazi == 3:
            dokaz_1.reset()
            dokaz_2.reset()
            dokaz_3.reset()
        elif dokazi == 4:
            dokaz_1.reset()
            dokaz_2.reset()
            dokaz_3.reset()
            dokaz_4.reset()
        if move_wolf and level_2:
            werewolf_dlg_1.reset()

    if level_2 and (sprite.collide_rect(camerman, werewolf) or sprite.collide_rect(svidok, werewolf)):
        if loose_sound:
            s_werewolf_angry.play()
            loose_sound = False
        finish = True
        lose = transform.scale(image.load("Assets/game_over.jpg"), [1500, 900])
        mw.fill((255, 255, 255))
        mw.blit(lose, (0, 0))
    if level_1 and (sprite.collide_rect(car_colide, camerman) and keys[K_f] and dokazi == 4):
        s_zamok.play()
        if win_sound:
            s_car_start.play()
            win_sound = False
        finish = True
        win = transform.scale(image.load("Assets/win_fon.jpg"), [1500, 900])
        mw.fill((255, 255, 255))
        mw.blit(win, (0, 0))


    '''if test_level:
        mw.blit(picture, [0, 0])
        barriers.draw(mw)
        camerman.draw()
        werewolf.draw()
        camerman.update(barriers)
        werewolf.update(barriers)
        camerman.moves()
        werewolf.moves()'''
    display.update()
    clock.tick(40)
