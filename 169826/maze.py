#создай игру "Лабиринт"!
from pygame import *


win_width = 700
win_height = 500

window = display.set_mode((win_width, win_height))
display.set_caption("Maze")
icon = transform.scale(image.load('icon_gold.png'),(32,32))
display.set_icon(icon)

mixer.init()
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65,65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.direction = 'right'
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def __init__(self, *args, **qwargs):
        super().__init__(*args, **qwargs)
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
        if keys_pressed[K_a]and self.rect.x > 5:
            if self.direction == 'right':
                self.image = transform.flip(self.image, True, False)
                self.direction = 'left'
            self.rect.x -= self.speed
        if keys_pressed[K_d]and self.rect.x < win_width - 80:
            if self.direction == 'left':
                self.image = transform.flip(self.image, True, False)
                self.direction = 'right'
            self.rect.x += self.speed
class Enemy(GameSprite):
    def __init__(self, *args, **qwargs):
        super().__init__(*args, **qwargs)
        self.direction_y = 'top'
    def update(self, start_x, start_y, end_x, end_y):
        if start_x != end_x:
            if self.rect.x <= start_x:
                self.direction = 'right'
                self.image = transform.flip(self.image, True, False)
            if self.rect.x >= end_x:
                self.direction = 'left'
                self.image = transform.flip(self.image, True, False)
            if self.direction == 'left':
                self.rect.x -= self.speed
            else:
                self.rect.x += self.speed
        if start_y != end_y:
            if self.rect.y <= start_y:
                self.direction_y = 'top'
            if self.rect.y >= end_y:
                self.direction_y = 'bottom'
            if self.direction_y == 'top':
                self.rect.y += self.speed
            else:
                self.rect.y -= self.speed
class wall(sprite.Sprite):
    def __init__(self, color, x, y, wall_width, wall_height):
        super().__init__()
        self.image = Surface((wall_width, wall_height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def draw_wall(self):
        window.blit(self.image,(self.rect.x, self.rect.y))



background = transform.scale(image.load("background.jpg"), (win_width, win_height))
pers = Player('player.png', 100,100,3)
enemy = Enemy('enemy1.png', 500,300,1)
gold = GameSprite('treasure1.png', 500,400,1)
mixer.music.load('song.mp3')
mixer.music.play(-1)
clock = time.Clock()
FPS = 60
Game = True
play_music = True
Finish = False
font.init()
font = font.Font(None, 70)
walls = []
walls.append(wall((255, 98, 72), 50, 50, 120, 10))
walls.append(wall((255, 98, 72), 170, 50, 10, 100))
walls.append(wall((255, 98, 72), 170, 150, 10, 100))
walls.append(wall((255, 98, 72), 170, 250, 10, 100))
walls.append(wall((255, 98, 72), 170, 340, 100, 10))
walls.append(wall((255, 98, 72), 250, 340, 100, 10))
walls.append(wall((255, 98, 72), 340, 240, 10, 100))
walls.append(wall((255, 98, 72), 340, 140, 10, 100))
walls.append(wall((255, 98, 72), 340, 140, 100, 10))
walls.append(wall((255, 98, 72), 430, 140, 10, 100))
walls.append(wall((255, 98, 72), 430, 240, 100, 10))
walls.append(wall((255, 98, 72), 500, 240, 125, 10))
walls.append(wall((255, 98, 72), 615, 340, 10, 100))
walls.append(wall((255, 98, 72), 615, 440, 10, 100))
walls.append(wall((255, 98, 72), 615, 240, 10, 115))
walls.append(wall((255, 98, 72), 50, 50, 10, 100))
walls.append(wall((255, 98, 72), 50, 150, 10, 100))
walls.append(wall((255, 98, 72), 50, 250, 10, 100))
walls.append(wall((255, 98, 72), 50, 340, 10, 100))
walls.append(wall((255, 98, 72), 50, 440, 10, 100))
walls.append(wall((255, 98, 72), 50, 490, 100, 10))
walls.append(wall((255, 98, 72), 150, 490, 100, 10))
walls.append(wall((255, 98, 72), 250, 490, 100, 10))
walls.append(wall((255, 98, 72), 350, 490, 100, 10))
walls.append(wall((255, 98, 72), 450, 400, 10, 100))
walls.append(wall((255, 98, 72), 450, 490, 175, 10))
while Game:
    if Finish == False:

        pers.update()
        enemy.update(400, 200, 500, 350)
        for e in event.get():
            if e.type == QUIT:
                Game = False
            if e.type == KEYDOWN and e.key == K_ESCAPE:
                play_music = not play_music
                if play_music:
                    mixer.music.unpause()
                else:
                    mixer.music.pause()
        window.blit(background,(0,0))
        for wall in walls:
            wall.draw_wall()
        pers.reset()
        enemy.reset()
        gold.reset()
        if sprite.collide_rect(pers, gold):
            Finish = True
            text = 'YOU WIN'
        if sprite.collide_rect(pers, enemy):
            Finish = True
            text = 'YOU LOSER'
        for wall in walls:
            if sprite.collide_rect(pers, wall):
                Finish = True
                text = 'YOU LOSER'
        
    else:
        finifh_text = font.render(text, True, (255, 215, 0))
        window.blit(finifh_text, (200,200))
        for e in event.get():
            if e.type == QUIT:
                Game = False
    display.update()
    clock.tick(FPS)