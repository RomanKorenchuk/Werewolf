from pygame import *
from pygame.math import Vector2

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
 
    def __init__(self, pos, *groups):
        super().__init__(*groups)
        sprite.Sprite.__init__(self)
        self.image = image.load('Assets/Camerman_moves.png')
        self.image.set_clip(Rect(0, 0, 64, 64))
        self.image = self.image.subsurface(self.image.get_clip())
        self.rect = self.image.get_rect(center=pos)
        self.pos = Vector2(pos)
        self.vel = Vector2(0, 0)
        self.frame = 0
        self.left_states = { 0: (0, 64, 64, 64), 1: (64, 64, 64, 64), 2: (128, 64, 64, 64), 3: (192, 64, 64, 64) }
        self.right_states = { 0: (0, 128, 64, 64), 1: (64, 128, 64, 64), 2: (128, 128, 64, 64), 3: (192, 128, 64, 64) }
        self.up_states = { 0: (0, 192, 64, 64), 1: (64, 192, 64, 64), 2: (128, 192, 64, 64), 3: (192, 192, 64, 64)  }
        self.down_states = { 0: (0, 0, 64, 64), 1: (64, 0, 64, 64), 2: (128, 0, 64, 64), 3: (192, 0, 64, 64) }
 
    def get_frame(self, frame_set):
        self.frame += 1
        if self.frame > (len(frame_set) - 1):
            self.frame = 0
        return frame_set[self.frame]
 
    def clip(self, clipped_rect):
        if type(clipped_rect) is dict:
            self.image.set_clip(Rect(self.get_frame(clipped_rect)))
        else:
            self.image.set_clip(Rect(clipped_rect))
        return clipped_rect
    
    def handle_event(self, e):
        if e.type == KEYDOWN:
            if e.key == K_d:
                self.vel.x = 5
            elif e.key == K_a:
                self.vel.x = -5
            elif e.key == K_w:
                self.vel.y = -5
            elif e.key == K_s:
                self.vel.y = 5
                
        elif e.type == KEYUP:
            if e.key == K_d and self.vel.x > 0:
                self.vel.x = 0
            elif e.key == K_a and self.vel.x < 0:
                self.vel.x = 0
            elif e.key == K_w and self.vel.y < 0:
                self.vel.y = 0
            elif e.key == K_s and self.vel.y > 0:
                self.vel.y = 0
  
    def animation_event(self, event):
        if self.vel.x > 0:
            self.clip(self.right_states)
        elif self.vel.x < 0:
            self.clip(self.left_states)
        elif self.vel.y < 0:
            self.clip(self.up_states)
        elif self.vel.y > 0:
            self.clip(self.down_states)
 
        elif event.type == KEYUP:
            if event.key == K_d:
                self.clip(self.right_states[0])
            elif event.key == K_a:
                self.clip(self.left_states[0])  
            elif event.key == K_w:
                self.clip(self.up_states[0])
            elif event.key == K_s:
                self.clip(self.down_states[0])
 
        self.imagee = self.image.subsurface(self.image.get_clip())
 
    def update(self):
        self.pos += self.vel
        self.rect.center = self.pos
        
 
 
def main():
    init()
    screen = display.set_mode((800, 600))
 
    clock = time.Clock()
    all_sprites = sprite.Group()
    camera = Vector2(400, 300)
    player = Player((415, 315), all_sprites)
 
 
    background_rects = GameSprite("Assets/Temnosiri_fon.jpg", 800, 600, 0, 0) 
    
 
 
    while True:
        for e in event.get():
            if e.type == QUIT:
                return
 
            player.handle_event(e)
        player.animation_event(e)
            
 
        all_sprites.update()
        offset = camera - player.pos
        screen.fill((50, 180, 150))
 
     
        screen.blit(background_rects.image, background_rects.rect.topleft+offset)
        screen.blit(player.image, player.rect.topleft+offset)
        
        display.flip()
        clock.tick(24)
 
 
if __name__ == '__main__':
    main()
    quit()