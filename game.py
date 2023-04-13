from pygame import *
from pygame.math import Vector2

class GameSprite(sprite.Sprite):
    def __init__(self, picture, w, h, x, y):
        super().__init__()
        self.start_image = transform.scale(image.load(picture), [w, h])
        self.image = self.start_image
        self.rect = self.image.get_rect()
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
        self.rect.x = x
        self.rect.y = y
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.w = w
        self.h = h
        self.frame = 0
        self.position = position

    def update(self):
        if camerman.rect.x <= 1280-100 and camerman.x_speed > 0 or camerman.rect.x >= 0 and camerman.x_speed < 0:
            self.rect.x += self.x_speed
        platforms_touched = sprite.spritecollide(self, barriers, False)
        if self.x_speed > 0:
            for p in platforms_touched:
                self.rect.right = min(self.rect.right, p.rect.left)
        elif self.x_speed < 0:
            for p in platforms_touched:
                self.rect.left = max(self.rect.left, p.rect.right)
        if camerman.rect.y <= 720-90 and camerman.y_speed > 0 or camerman.rect.y >= 0 and camerman.y_speed < 0:
            self.rect.y += self.y_speed
        platforms_touched = sprite.spritecollide(self, barriers, False)
        if self.y_speed > 0: 
            for p in platforms_touched:
                self.y_speed = 0              
                if p.rect.top < self.rect.bottom:
                    self.rect.bottom = p.rect.top
        elif self.y_speed < 0: 
            for p in platforms_touched:
                self.y_speed = 0
                self.rect.top = max(self.rect.top, p.rect.bottom)
        
        self.x_speed = 0
        self.y_speed = 0

    def draw(self):
        if self.position == 0:
            mw.blit(self.image,(self.rect.x,self.rect.y))
        elif self.position == 1:
            mw.blit(transform.flip(self.image,True,False),(self.rect.x,self.rect.y))
    
    def moves(self):
        self.image = transform.scale(image.load(self.pictures[self.move]), [self.w, self.h])


mw = display.set_mode((1280, 720))
display.set_caption(("Werewolf"))
picture = image.load("Assets/Temnosiri_fon.jpg").convert()
picture = transform.scale(picture, [1280, 720])

barriers = sprite.Group()

derevo = GameSprite('Assets/Derevo.png', 200, 200, 900, 500)

camerman_pictures = list()
for i in range(15):
    i += 1
    camerman_pictures.append("Assets/Camerman/Camerman_move_" + str(i) + ".png")
camerman = Player(camerman_pictures, 70, 100, 100, 500, 0, 0, 0, 0)

barriers.add(derevo)

clock = time.Clock()
run = True

while run:
    time.delay(50)
    for e in event.get():
        if e.type == QUIT:
            run = False
        keys = key.get_pressed()
        camerman.move += 1
        if camerman.move >= 15:
            camerman.move = 0
        if keys[K_a] and keys[K_w]:
            camerman.x_speed = -10
            camerman.y_speed = -10
        elif keys[K_a] and keys[K_s]:
            camerman.x_speed = -10
            camerman.y_speed = 10
        elif keys[K_d] and keys[K_w]:
            camerman.x_speed = 10
            camerman.y_speed = -10
        elif keys[K_s] and keys[K_d]:
            camerman.x_speed = 10
            camerman.y_speed = 10   
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
      
    mw.blit(picture, [0, 0])
    barriers.draw(mw)
    camerman.draw()
    camerman.update()
    camerman.moves()
    display.update()
    clock.tick(40)
