#створи гру "Лабіринт"!
from pygame import*

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

class Enemy(GameSprite):
    direction = "left"

    def update(self):
        if self.rect.x <= 470:
            self.direction = "right"
        if self.rect.x >= win_width - 85:
            self.direction = "left"
        
        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height

        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))

        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

w1 = Wall(38, 66, 9,100, 0, 12, 200)
w2 = Wall(38, 66, 9,100, 350, 12, 400)
w3 = Wall(38, 66, 9,110, 200, 200, 12)
w4 = Wall(38, 66, 9,400, 0, 50, 400)
w5 = Wall(38, 66, 9,110, 100, 200, 12)
w6 = Wall(38, 66, 9,200, 350, 200, 12)
w7 = Wall(38, 66, 9,550, 100, 12, 700)
w8 = Wall(38, 66, 9,650, 0, 12, 500)
w9 = Wall(38, 66, 9,750, 190, 12, 500)
win_width = 1000
win_height = 700

window = display.set_mode((win_width, win_height))
display.set_caption("Maze")
background = transform.scale(image.load("arena.jpg"), (win_width, win_height))

player = Player("gg.png", 5, win_height - 120, 4)
monster = Enemy("ryr.png", win_width - 80, 200, 2)
final = GameSprite("win.jpg", win_width - 120, win_height - 80, 0)

game = True
clock = time.Clock()
FPS = 60


mixer.init()
mixer.music.load("muski.mp3")
mixer.music.play()   

finish = False

font.init()
font = font.SysFont('Arial', 70)
win = font.render("YOU WIN", True, (255, 215, 0)) 
lose = font.render("YOU LOSE", True, (180, 0, 0)) 

money = mixer.Sound("money.ogg")
kick = mixer.Sound("kick.ogg")
while game:

    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background,(0, 0))
        player.update()
        monster.update()

        player.reset()


        monster.reset()
        final.reset()

        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        w6.draw_wall()
        w7.draw_wall()
        w8.draw_wall()
        w9.draw_wall()

        if sprite.collide_rect(player, monster) or sprite.collide_rect(player, w1) or sprite.collide_rect(player, w2)or sprite.collide_rect(player, w3) or sprite.collide_rect(player, w4) or sprite.collide_rect(player, w5) or sprite.collide_rect(player, w6) or sprite.collide_rect(player, w7) or sprite.collide_rect(player, w8) or sprite.collide_rect(player, w9):
            finish = True
            window.blit(lose, (400,300))
            kick.play()
        if sprite.collide_rect(player, final):
            finish = True
            window.blit(win, (400,300))
            money.play()
            
    display.update()
    clock.tick(FPS)









            
            


