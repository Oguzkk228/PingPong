from pygame import *
from random import randint
font.init()
font1 = font.Font(None, 36)
BlueMiss = 0
RedMiss = 0
window = display.set_mode((700, 500))
background = transform.scale(image.load('field.png'), (700, 600))
display.set_caption('PInGPoNg')
class GameSprite(sprite.Sprite):
    def __init__(self, filename, w, h, speed, x, y):
        super().__init__()
        self.image = transform.scale(image.load(filename), (w, h))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Wall1(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 400:
            self.rect.y += self.speed
class Wall2(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 400:
            self.rect.y += self.speed
class Ball(GameSprite):
    def __init__(self, filename, w, h, speed, Yspeed, x, y):
        super().__init__(filename, w, h, speed, x, y)
        self.Yspeed = Yspeed
    def update(self):
        global RedMiss
        global BlueMiss
        self.rect.y += self.Yspeed
        self.rect.x += self.speed
        if self.rect.y >= 465:
            self.Yspeed *= -1
        if self.rect.y <= 0:
            self.Yspeed *= -1
        if self.rect.x >= 700:
            Direction = randint(1, 2)
            if Direction == 1:
                self.rect.y = 250
                self.rect.x = 350
                self.speed = randint(3, 6)
                self.speed *= -1
            else:
                self.rect.y = 250
                self.rect.x = 350
                self.speed = randint(3, 6)
            RedMiss += 1
        if self.rect.x <= -35:
            Direction = randint(1, 2)
            if Direction == 1:
                self.rect.y = 250
                self.rect.x = 350
                self.speed = randint(3, 6)
                self.speed *= -1
            else:
                self.rect.y = 250
                self.rect.x = 350
                self.speed = randint(3, 6)
            BlueMiss += 1
Player1 = Wall1('bluroja.jpg', 20, 100, 5, 10, 150)
Player2 = Wall2('rojared.jpg', 20, 100, 5, 670, 150)
TheBall = Ball('ball.png', 35, 35, randint(3, 6), randint(1, 3), 250, 350)
game = True
clock = time.Clock()
FPS = 60
while game:
    text_BlueMiss = font1.render('Синий Пропустил:' +str(BlueMiss), 1, (0, 0, 255))
    text_RedMiss = font1.render('Красный Пропустил:' +str(RedMiss), 1, (255, 0, 0))
    if sprite.collide_rect(TheBall, Player1) == True:
            TheBall.speed *= -1
    if sprite.collide_rect(TheBall, Player2) == True:
        TheBall.speed *= -1
    window.blit(background, (0, -50))
    window.blit(text_BlueMiss, (250, 10))
    window.blit(text_RedMiss, (250, 35))
    Player1.update()
    Player1.reset()
    Player2.update()
    Player2.reset()
    TheBall.update()
    TheBall.reset()
    for e in event.get():
        if e.type == QUIT:
                game = False
    clock.tick(FPS)
    display.update()