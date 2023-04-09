from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, picture, w, h, x, y, ):
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
        self.move = move
        self.image = transform.scale(image.load(self.pictures[self.move]), [w, h])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.w = w
        self.h = h
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

camerman_pictures = ("Assets/Camerman_move1.png", "Assets/Camerman_move2.png", "Assets/Camerman_move3.png", "Assets/Camerman_move4.png")
camerman = Player(camerman_pictures, 70, 100, 100, 500, 0, 0, 0, 0)

barriers.add(derevo)

clock = time.Clock()

run = True

while run:
    time.delay(50)
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            camerman.move += 1
            if camerman.move > 3:
                camerman.move = 0
            
            if e.key == K_a:
                camerman.x_speed = -10
                camerman.position = 1     
            elif e.key == K_d:
                camerman.x_speed = 10
                camerman.position = 0
            elif e.key == K_w :
                camerman.y_speed = -10
            elif e.key == K_s :
                camerman.y_speed = 10
        elif e.type == KEYUP:
            if e.key == K_a :
                camerman.x_speed = 0
            elif e.key == K_d:
                camerman.x_speed = 0
            elif e.key == K_w:
                camerman.y_speed = 0
            elif e.key == K_s:
                camerman.y_speed = 0  

        mw.blit(picture, [0, 0])
        barriers.draw(mw)
        camerman.draw()
        camerman.update()
        camerman.moves()

    display.update()
    clock.tick(40)
