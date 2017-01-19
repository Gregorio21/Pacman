import pygame
import random
width = 1200
height = 600
BLACK = (0,0,0)
WHITE = (255, 255, 255)
BLUE = (0,0,128)
GREY = (220,220,220)
RED = (255,0,0)
YELLOW = (255,255,0)
PINK = (255, 0, 255)
BLUE2 = (0, 0, 255)
GREEN = (0, 255, 0)
BLUE3 = (30,144,255)
score = 0
lives = 3
killed = 1
powerup = 0
winner = False
travel = 0
class Player(pygame.sprite.Sprite):
    left_boundary = 0
    right_boundary = width
    top_boundary = 0
    bottom_boundary = height
    change_x = 0
    change_y = 0
    previous_y = 0
    previous_x = 0
    ticks = 0
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("pacman_right.jpg").convert() 
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        previous_x = 0
        previous_y = 0
        self.x = x
        self.y = y
    def update(self):
        self.rect.x += self.change_x
        self.rect.y += self.change_y        
        if pygame.sprite.spritecollideany(self, walls):
            self.rect.x -= self.change_x
            self.rect.y -= self.change_y            
            if self.change_x != 0:
                self.rect.y += self.previous_y
                if self.previous_y > 0:
                    if self.ticks <= 15 and self.ticks >= 0:
                        self.ticks += 1
                        player.down()
                    elif self.ticks >= 15 and self.ticks <= 30:
                        player.open_down()
                        self.ticks += 1
                    elif self.ticks >= 30:
                        self.ticks = 0
                elif self.previous_y < 0:
                    if self.ticks <= 15 and self.ticks >= 0:
                        self.ticks += 1
                        player.up()
                    elif self.ticks >= 15 and self.ticks <= 30:
                        player.open_up()
                        self.ticks += 1
                    elif self.ticks >= 30:
                        self.ticks = 0
                if pygame.sprite.spritecollideany(self, walls):
                    self.rect.y -= self.previous_y                                        
            elif self.change_y != 0:
                self.rect.x += self.previous_x
                if self.previous_x > 0:
                    if self.ticks <= 15 and self.ticks >= 0:
                        self.ticks += 1
                        player.right()
                    elif self.ticks >= 15 and self.ticks <= 30:
                        player.open_right()
                        self.ticks += 1
                    elif self.ticks >= 30:
                        self.ticks = 0
                elif self.previous_x < 0:
                    if self.ticks <= 15 and self.ticks >= 0:
                        self.ticks += 1
                        player.left()
                    elif self.ticks >= 15 and self.ticks <= 30:
                        player.open_left()
                        self.ticks += 1
                    elif self.ticks >= 30:
                        self.ticks = 0
                if pygame.sprite.spritecollideany(self, walls):                    
                    self.rect.x -= self.previous_x                    
        else:            
            if self.change_x != 0:
                if self.change_x > 0:
                    if self.ticks <= 15 and self.ticks >= 0:
                        self.ticks += 1
                        player.right()
                    elif self.ticks >= 15 and self.ticks <= 30:
                        player.open_right()
                        self.ticks += 1
                    elif self.ticks >= 30:
                        self.ticks = 0
                elif self.change_x < 0:
                    if self.ticks <= 15 and self.ticks >= 0:
                        self.ticks += 1
                        player.left()
                    elif self.ticks >= 15 and self.ticks <= 30:
                        player.open_left()
                        self.ticks += 1
                    elif self.ticks >= 30:
                        self.ticks = 0
                self.previous_x = self.change_x
                self.previous_y = 0
            elif self.change_y != 0:
                if self.change_y > 0:
                    if self.ticks <= 15 and self.ticks >= 0:
                        self.ticks += 1
                        player.down()
                    elif self.ticks >= 15 and self.ticks <= 30:
                        player.open_down()
                        self.ticks += 1
                    elif self.ticks >= 30:
                        self.ticks = 0
                elif self.change_y < 0:
                    if self.ticks <= 15 and self.ticks >= 0:
                        self.ticks += 1
                        player.up()
                    elif self.ticks >= 15 and self.ticks <= 30:
                        player.open_up()
                        self.ticks += 1
                    elif self.ticks >= 30:
                        self.ticks = 0
                self.previous_y = self.change_y
                self.previous_x = 0
    def right(self):
        self.image = pygame.image.load("pacman_right.jpg").convert()
    def left(self):
        self.image = pygame.image.load("pacman.jpg").convert()
    def up(self):
        self.image = pygame.image.load("pacman_up.jpg").convert()
    def down(self):
        self.image = pygame.image.load("pacman_down.jpg").convert()
    def open_right(self):
        self.image = pygame.image.load("pacman_open_right.jpg").convert()
    def open_left(self):
        self.image = pygame.image.load("pacman_open.jpg").convert()
    def open_up(self):
        self.image = pygame.image.load("pacman_open_up.jpg").convert()
    def open_down(self):
        self.image = pygame.image.load("pacman_open_down.jpg").convert()
    def stage1(self):
        self.image = pygame.image.load("pacman_stage1.jpg").convert()
    def stage2(self):
        self.image = pygame.image.load("pacman_stage2.jpg").convert()
    def stage3(self):
        self.image = pygame.image.load("pacman_stage3.jpg").convert()
    def stage4(self):
        self.image = pygame.image.load("pacman_stage4.jpg").convert()
    def stage5(self):
        self.image = pygame.image.load("pacman_stage5.jpg").convert()
    def stage6(self):
        self.image = pygame.image.load("pacman_stage6.jpg").convert()
    def reset(self):
        players.add(self)
        self.rect.x = self.x
        self.rect.y = self.y
class Life(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("pacman_right.jpg").convert() 
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x = x
        self.y = y
        
class Pellet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 10))
        self.image.fill(BLACK)
        pygame.draw.circle(self.image, YELLOW, (5, 5), 3, 0)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
class Ghost(pygame.sprite.Sprite):
    change_x = 0
    change_y = 0
    previous_x = 0
    previous_y = 0
    ticks = 0
    died = False
    flip = False
    corner = False
    gate_up = False
    gate_down = False
    gate_left = False
    gate_right = False
    def __init__(self, x, y, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x = x
        self.y = y
        self.orimage = filename 
    def power(self):
        self.flip = True
        if not self.died:
            self.image = pygame.image.load("blue.jpg").convert()
    def white(self):
        if not self.died:
            self.image = pygame.image.load("white.jpg").convert()
    def nopower(self):
        self.image = pygame.image.load(self.orimage).convert()
    def update(self):
        num = 5
        left = False
        right = False
        up = False
        down = False
        if self.flip:
            num = -num
        if self.ticks < 9 and self.ticks > -1:
            self.ticks += 1
            self.rect.y -= num
        elif self.ticks < 0:
            self.ticks += 1
        elif self.ticks > 8:
            self.rect.x += num
            if pygame.sprite.spritecollideany(self, walls):
                self.rect.x -= num
            else:
                self.rect.x -= num
                right = True
            self.rect.x -= num
            if pygame.sprite.spritecollideany(self, walls):
                self.rect.x += num
            else:
                self.rect.x += num
                left = True
            self.rect.y += num
            if pygame.sprite.spritecollideany(self, walls):
                self.rect.y -= num
            else:
                self.rect.y -= num
                down = True
            self.rect.y -= num
            if pygame.sprite.spritecollideany(self, walls):
                self.rect.y += num
            else:
                self.rect.y += num
                up = True
            if left and up:
                if not right and not down:
                    self.corner = True
                    self.previous_x = 0
                    self.previous_y = 0
                    number = random.randint(1,2)
                    if number == 1:
                        self.rect.x -= num
                    elif number == 2:
                        self.rect.y -= num
            if left and down:
                if not right and not up:
                    self.corner = True
                    self.previous_x = 0
                    self.previous_y = 0
                    number = random.randint(1,2)
                    if number == 1:
                        self.rect.x -= num
                    elif number == 2:
                        self.rect.y += num   
            if right and up:
                if not left and not down:
                    self.corner = True
                    self.previous_x = 0
                    self.previous_y = 0
                    number = random.randint(1,2)
                    if number == 1:
                        self.rect.x += num
                    elif number == 2:
                        self.rect.y -= num
            if right and down:
                if not left and not up:
                    self.corner = True
                    self.previous_x = 0
                    self.previous_y = 0
                    number = random.randint(1,2)
                    if number == 1:
                        self.rect.x += num
                    elif number == 2:
                        self.rect.y += num
            if left and right:
                if not up and not down:
                    self.gate_up = False
                    self.gate_down = False
                    self.previous_y = 0
                    if self.previous_x > 0:
                        number = random.randint(1,60)
                        if number > 0 and number < 60:
                            self.previous_x = 5
                            self.rect.x += num
                        elif number == 600:
                            self.previous_x = -5
                            self.rect.x -= num
                    elif self.previous_x < 0:
                        number = random.randint(1,60)
                        if number > 0 and number < 60:
                            previous_x = -5
                            self.rect.x -= num
                        elif number == 600:
                            previous_x = 5
                            self.rect.x += num
                    else:
                        number = random.randint(1,2) 
                        if number == 1:
                            self.previous_x = 5
                            self.rect.x += num
                        elif number == 2:
                            self.previous_x = -5
                            self.rect.x -= num
                    
            if up and down:
                if not left and not right:
                    self.gate_left = False
                    self.gate_right = False
                    self.previous_x = 0
                    if self.previous_y > 0:
                        number = random.randint(1,60)
                        if number > 0 and number < 60:
                            self.previous_y = 5
                            self.rect.y += num
                        elif number == 600:
                            self.previous_y = -5
                            self.rect.y -= num
                    elif self.previous_y < 0:
                        number = random.randint(1,60)
                        if number > 0 and number < 60:
                            previous_y = -5
                            self.rect.y -= num
                        elif number == 600:
                            previous_y = 5
                            self.rect.y += num
                    else:
                        number = random.randint(1,2) 
                        if number == 1:
                            self.previous_y = 5
                            self.rect.y += num
                        elif number == 2:
                            self.previous_y = -5
                            self.rect.y -= num
            if left and right and up:
                if not down:
                    self.gate_up = True
                    number = random.randint(1,90)
                    if number > 75:
                        self.rect.x -= num
                    elif number > 60 and number < 76:
                        self.rect.x += num
                    elif number > 0 and number < 61:
                        if self.gate_down:
                            pass
                        else:
                            self.previous_y = -5
                            self.rect.y -= num
            if left and right and down:
                if not up:
                    self.gate_down = True
                    number = random.randint(1,90)
                    if number > 75:
                        self.rect.x -= num
                    elif number > 60 and number < 76:
                        self.rect.x += num
                    elif number > 0 and number < 61:
                        if self.gate_up:
                            pass
                        else:
                            self.previous_y = 5
                            self.rect.y += num 
            if up and down and right:
                if not left:
                    self.gate_right = True
                    number = random.randint(1,90)
                    if number > 75:
                        self.rect.y -= num
                    elif number > 60 and number < 76:
                        self.rect.y += num
                    elif number > 0 and number < 61:
                        if self.gate_left:
                            pass
                        else:
                            self.previous_x = 5
                            self.rect.x += num
            if up and down and left:
                if not right:
                    self.gate_left = True
                    number = random.randint(1,90)
                    if number > 75:
                        self.rect.y -= num
                    elif number > 60 and number < 76:
                        self.rect.y += num
                    elif number > 0 and number < 61:
                        if self.gate_right:
                            pass
                        else:
                            self.previous_x = -5
                            self.rect.x -= num
    def reset(self):
        ghosts.add(self)
        self.rect.x = self.x
        self.rect.y = self.y
        self.ticks = 0
        self.nopower()
        if powerup > 0:
            self.died = True
        self.flip = False
        if self.died:
            self.ticks = -150
class Walls(pygame.sprite.Sprite):
    def __init__(self, x, y, length, thickness, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([length, thickness])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
class Power_up(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 10))
        self.image.fill(BLACK)
        pygame.draw.circle(self.image, PINK, (5, 5), 3, 0)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
pygame.init()
font = pygame.font.Font(None, 36)
font2 = pygame.font.Font(None, 36)
screen = pygame.display.set_mode([width,height])
pygame.display.set_caption("Pacman")
all_sprites = pygame.sprite.Group()
walls = pygame.sprite.Group()
pellets = pygame.sprite.Group()
ghosts = pygame.sprite.Group()
borders = pygame.sprite.Group()
players = pygame.sprite.Group()
powerups = pygame.sprite.Group()
dead = pygame.sprite.Group()

"""         walls          """
"""    borders    """
wall1 = Walls(0, 0, 5, 600, GREY)
walls.add(wall1)
all_sprites.add(wall1)
borders.add(wall1)
wall1 = Walls(1195, 0, 5, 600, GREY)
walls.add(wall1)
all_sprites.add(wall1)
borders.add(wall1)
wall1 = Walls(0, 0, 1200, 5, GREY)
walls.add(wall1)
all_sprites.add(wall1)
borders.add(wall1)
wall1 = Walls(0, 595, 1200, 5, GREY)
walls.add(wall1)
all_sprites.add(wall1)
borders.add(wall1)
"""    borders    """
""" layer1  """
wall1 = Walls(25, 25, 460, 10, BLUE)
walls.add(wall1)
all_sprites.add(wall1)
wall1 = Walls(25, 25, 10, 265, BLUE)
walls.add(wall1)
all_sprites.add(wall1)
wall1 = Walls(505, 565, 460, 10, BLUE)
walls.add(wall1)
all_sprites.add(wall1)
wall1 = Walls(955, 310, 10, 265, BLUE)
walls.add(wall1)
all_sprites.add(wall1)
wall1 = Walls(25, 565, 460, 10, BLUE)
walls.add(wall1)
all_sprites.add(wall1)
wall1 = Walls(25, 310, 10, 265, BLUE)
walls.add(wall1)
all_sprites.add(wall1)
wall1 = Walls(955, 25, 10, 265, BLUE)
walls.add(wall1)
all_sprites.add(wall1)
wall1 = Walls(505, 25, 460, 10, BLUE)
walls.add(wall1)
all_sprites.add(wall1)
"""  layer2  """
wall1 = Walls(55, 55, 220, 10, BLUE)
walls.add(wall1)
all_sprites.add(wall1)
wall1 = Walls(55, 55, 10, 490, BLUE)
walls.add(wall1)
all_sprites.add(wall1)
wall1 = Walls(295, 55, 400, 10, BLUE)
walls.add(wall1)
all_sprites.add(wall1)
wall1 = Walls(715, 55, 220, 10, BLUE)
walls.add(wall1)
all_sprites.add(wall1)
wall1 = Walls(925, 55, 10, 490, BLUE)
walls.add(wall1)
all_sprites.add(wall1)
wall1 = Walls(55, 535, 220, 10, BLUE)
walls.add(wall1)
all_sprites.add(wall1)
wall1 = Walls(295, 535, 400, 10, BLUE)
walls.add(wall1)
all_sprites.add(wall1)
wall1 = Walls(715, 535, 220, 10, BLUE)
walls.add(wall1)
all_sprites.add(wall1)
"""  layer3   """
wall1 = Walls(85, 85, 400, 10, BLUE)
walls.add(wall1)
all_sprites.add(wall1)
wall1 = Walls(85, 85, 10, 205, BLUE)
walls.add(wall1)
all_sprites.add(wall1)
wall1 = Walls(85, 310, 10, 205, BLUE)
walls.add(wall1)
all_sprites.add(wall1)
wall1 = Walls(85, 505, 400, 10, BLUE)
walls.add(wall1)
all_sprites.add(wall1)
wall1 = Walls(505, 85, 400, 10, BLUE)
walls.add(wall1)
all_sprites.add(wall1)
wall1 = Walls(505, 505, 400, 10, BLUE)
walls.add(wall1)
all_sprites.add(wall1)
wall1 = Walls(895, 310, 10, 205, BLUE)
walls.add(wall1)
all_sprites.add(wall1)
wall1 = Walls(895, 85, 10, 205, BLUE)
walls.add(wall1)
all_sprites.add(wall1)
"""  layer4  """
wall1 = Walls(115, 115, 160, 10, BLUE)
walls.add(wall1)
all_sprites.add(wall1)
wall1 = Walls(115, 115, 10, 370, BLUE)
walls.add(wall1)
all_sprites.add(wall1)
wall1 = Walls(115, 475, 160, 10, BLUE)
walls.add(wall1)
all_sprites.add(wall1)
wall1 = Walls(295, 475, 400, 10, BLUE)
walls.add(wall1)
all_sprites.add(wall1)
wall1 = Walls(715, 475, 160, 10, BLUE)
walls.add(wall1)
all_sprites.add(wall1)
wall1 = Walls(295, 115, 400, 10, BLUE)
walls.add(wall1)
all_sprites.add(wall1)
wall1 = Walls(715, 115, 160, 10, BLUE)
walls.add(wall1)
all_sprites.add(wall1)
wall1 = Walls(865, 115, 10, 370, BLUE)
walls.add(wall1)
all_sprites.add(wall1)
"""  layer5  """
wall1 = Walls(145, 145, 340, 10, BLUE)
walls.add(wall1)
all_sprites.add(wall1)
wall1 = Walls(505, 145, 340, 10, BLUE)
walls.add(wall1)
all_sprites.add(wall1)
wall1 = Walls(145, 145, 10, 145, BLUE)
walls.add(wall1)
all_sprites.add(wall1)
wall1 = Walls(145, 310, 10, 145, BLUE)
walls.add(wall1)
all_sprites.add(wall1)
wall1 = Walls(835, 145, 10, 145, BLUE)
walls.add(wall1)
all_sprites.add(wall1)
wall1 = Walls(835, 310, 10, 145, BLUE)
walls.add(wall1)
all_sprites.add(wall1)
wall1 = Walls(145, 445, 340, 10, BLUE)
walls.add(wall1)
all_sprites.add(wall1)
wall1 = Walls(505, 445, 340, 10, BLUE)
walls.add(wall1)
all_sprites.add(wall1)
"""  layer6  """
wall1 = Walls(175, 175, 100, 10, BLUE)
walls.add(wall1)
all_sprites.add(wall1)
wall1 = Walls(295, 175, 400, 10, BLUE)
walls.add(wall1)
all_sprites.add(wall1)
wall1 = Walls(715, 175, 95, 10, BLUE)
walls.add(wall1)
all_sprites.add(wall1)
wall1 = Walls(175, 175, 10, 250, BLUE)
walls.add(wall1)
all_sprites.add(wall1)
wall1 = Walls(175, 415, 100, 10, BLUE)
walls.add(wall1)
all_sprites.add(wall1)
wall1 = Walls(295, 415, 400, 10, BLUE)
walls.add(wall1)
all_sprites.add(wall1)
wall1 = Walls(715, 415, 95, 10, BLUE)
walls.add(wall1)
all_sprites.add(wall1)
wall1 = Walls(805, 175, 10, 250, BLUE)
walls.add(wall1)
all_sprites.add(wall1)
"""  layer7  """
wall1 = Walls(205, 205, 280, 10, BLUE)
walls.add(wall1)
all_sprites.add(wall1)
wall1 = Walls(505, 205, 280, 10, BLUE)
walls.add(wall1)
all_sprites.add(wall1)
wall1 = Walls(205, 205, 10, 85, BLUE)
walls.add(wall1)
all_sprites.add(wall1)
wall1 = Walls(205, 310, 10, 85, BLUE)
walls.add(wall1)
all_sprites.add(wall1)
wall1 = Walls(775, 205, 10, 85, BLUE)
walls.add(wall1)
all_sprites.add(wall1)
wall1 = Walls(775, 310, 10, 85, BLUE)
walls.add(wall1)
all_sprites.add(wall1)
wall1 = Walls(505, 385, 280, 10, BLUE)
walls.add(wall1)
all_sprites.add(wall1)
wall1 = Walls(205, 385, 280, 10, BLUE)
walls.add(wall1)
all_sprites.add(wall1)
"""  layer8  """
wall1 = Walls(235, 235, 40, 10, BLUE)
walls.add(wall1)
all_sprites.add(wall1)
wall1 = Walls(295, 235, 400, 10, BLUE)
walls.add(wall1)
all_sprites.add(wall1)
wall1 = Walls(715, 235, 40, 10, BLUE)
walls.add(wall1)
all_sprites.add(wall1)
wall1 = Walls(235, 235, 10, 130, BLUE)
walls.add(wall1)
all_sprites.add(wall1)
wall1 = Walls(235, 355, 40, 10, BLUE)
walls.add(wall1)
all_sprites.add(wall1)
wall1 = Walls(295, 355, 400, 10, BLUE)
walls.add(wall1)
all_sprites.add(wall1)
wall1 = Walls(715, 355, 40, 10, BLUE)
walls.add(wall1)
all_sprites.add(wall1)
wall1 = Walls(745, 235, 10, 130, BLUE)
walls.add(wall1)
all_sprites.add(wall1)
"""  center  """
wall1 = Walls(265, 265, 460, 70, BLUE)
walls.add(wall1)
all_sprites.add(wall1)


"""         walls          """

wall2 = Walls(985, 0, 5, 600, GREY)
walls.add(wall2)
all_sprites.add(wall2)
player = Player(5,5)
all_sprites.add(player)
players.add(player)
"""       pellets        """
x = -20
y = -20
for h in range(1,34):
    y = 10
    x += 30
    for k in range(1,34):
        if h==2 and k==19:
            pwrup = Power_up(x,y)
            powerups.add(pwrup)
            all_sprites.add(pwrup)            
        elif h==4 and k==17:
            pwrup = Power_up(x,y)
            powerups.add(pwrup)
            all_sprites.add(pwrup)
        elif h==4 and k==4:
            pwrup = Power_up(x,y)
            powerups.add(pwrup)
            all_sprites.add(pwrup)
        elif h==6 and k==6:
            pwrup = Power_up(x,y)
            powerups.add(pwrup)
            all_sprites.add(pwrup)
        elif h==6 and k==15:
            pwrup = Power_up(x,y)
            powerups.add(pwrup)
            all_sprites.add(pwrup)
        elif h==8 and k==13:
            pwrup = Power_up(x,y)
            powerups.add(pwrup)
            all_sprites.add(pwrup)
        elif h==8 and k==8:
            pwrup = Power_up(x,y)
            powerups.add(pwrup)
            all_sprites.add(pwrup)
        elif h==26 and k==8:
            pwrup = Power_up(x,y)
            powerups.add(pwrup)
            all_sprites.add(pwrup)
        elif h==26 and k==13:
            pwrup = Power_up(x,y)
            powerups.add(pwrup)
            all_sprites.add(pwrup)
        elif h==28 and k==15:
            pwrup = Power_up(x,y)
            powerups.add(pwrup)
            all_sprites.add(pwrup)
        elif h==28 and k==6:
            pwrup = Power_up(x,y)
            powerups.add(pwrup)
            all_sprites.add(pwrup)
        elif h==30 and k==4:
            pwrup = Power_up(x,y)
            powerups.add(pwrup)
            all_sprites.add(pwrup)
        elif h==30 and k==17:
            pwrup = Power_up(x,y)
            powerups.add(pwrup)
            all_sprites.add(pwrup)
        elif h==32 and k==2:
            pwrup = Power_up(x,y)
            powerups.add(pwrup)
            all_sprites.add(pwrup)
        elif h==32 and k==19:
            pwrup = Power_up(x,y)
            powerups.add(pwrup)
            all_sprites.add(pwrup)
        elif h==2 and k == 2:
            pwrup = Power_up(x,y)
            powerups.add(pwrup)
            all_sprites.add(pwrup)
        else:
            pellet = Pellet(x, y)
            pellets.add(pellet)
            all_sprites.add(pellet)
        y += 30
for i in walls:    
    pygame.sprite.spritecollide(i,pellets,True)
red = Ghost(485,290,"cyan.jpg")
ghosts.add(red)
red = Ghost(485,290,"green.jpg")
ghosts.add(red)
red = Ghost(485,290,"orange.jpg")
ghosts.add(red)
red = Ghost(485,290,"original.jpg")
ghosts.add(red)
red = Ghost(485,290,"pink.jpg")
ghosts.add(red)
red = Ghost(485,290,"purple.jpg")
ghosts.add(red)
red = Ghost(485,290,"red.jpg")
ghosts.add(red)
red = Ghost(485,290,"yellow.jpg")
ghosts.add(red)

"""       pellets        """
life = Life(1120,60)
all_sprites.add(life)
life2 = Life(1095,60)
all_sprites.add(life2)
clock = pygame.time.Clock()
done = False
game_over = False
time = -210
reset = 0
flash = 0
dieing = 0
channel = pygame.mixer.Channel(1)
channel2 = pygame.mixer.Channel(2)
eat_pellet = pygame.mixer.Sound("pacman_chomp.ogg")
eat_ghost = pygame.mixer.Sound("pacman_eatghost.wav")
intro = pygame.mixer.Sound("pacman_beginning.wav")
siren = pygame.mixer.Sound("pacman_siren.wav")
death = pygame.mixer.Sound("pacman_death.wav")
intro.play()
while not done:
    
    collider = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
            elif event.key == pygame.K_a:
                if player.rect.left <= player.left_boundary:
                    pass
                else:
                    player.change_x = -5
                    player.change_y = 0
                    
            elif event.key == pygame.K_d:
                if player.rect.right >= player.right_boundary:
                    pass                               
                else:
                    player.change_x = 5
                    player.change_y = 0
                
            elif event.key == pygame.K_w:
                if player.rect.top <= player.top_boundary:
                    pass                
                else:
                    player.change_x = 0
                    player.change_y = -5                                           
                         
            elif event.key == pygame.K_s:
                if player.rect.bottom >= player.bottom_boundary:
                    pass                                
                else:
                    player.change_x = 0
                    player.change_y = 5                
    
    if pygame.sprite.spritecollide(player, pellets, True):
        if channel.get_busy():
            pass
        else:
            channel.queue(eat_pellet)
        score += 10
    
    if pygame.sprite.spritecollide(player, powerups, True):
        score += 50
        killed = 1
        dead.empty()
        for i in ghosts:
            i.died = False
        powerup = 450
        
    if powerup > 0:
        if powerup < 151 and flash < 11 and flash > -1:
            flash += 1
            for i in ghosts:
                i.white()
        elif flash == 11:
            flash = -10
        else:
            flash += 1
            for i in ghosts:
                i.power()
        
        powerup -= 1
        for i in dead:
            if pygame.sprite.spritecollideany(i,players):
                pygame.sprite.spritecollide(i,players,True)
                dieing = 150
                if lives == 3: 
                    all_sprites.remove(life)
                elif lives == 2:
                    all_sprites.remove(life2)
                lives -= 1
                powerup = 0
                if lives > 0 or lives < 0:
                    all_sprites.add(player)
                    for i in ghosts:
                        i.reset()                    
                elif lives == 0:
                    game_over = True
        if pygame.sprite.spritecollideany(player, ghosts):
            collider = pygame.sprite.spritecollideany(player, ghosts)
            pygame.sprite.spritecollide(player, ghosts, True)
            eat_ghost.play()            
            collider.reset()
            dead.add(collider)
            score += (2^killed)*100
            killed += 1
        
    else:
        for i in ghosts:
            i.nopower()
            i.died = False
        dead.empty()
        killed = 1
        for i in ghosts:
            if pygame.sprite.spritecollide(i,players,True) and not lives <= 0:
                dieing = 150
                if lives == 3: 
                    all_sprites.remove(life)
                elif lives == 2:
                    all_sprites.remove(life2)
                else:
                    pygame.sprite.spritecollide(player, ghosts, True)
                lives -= 1
                
                if lives > 0 or lives < 0:
                    all_sprites.add(player)
                    for i in ghosts:
                        i.reset()
                    
                elif lives == 0:
                    players.add(player)
                    game_over = True
    if len(pellets) == 429:        
        if len(powerups) == 0:
            print "Game over"
            winner = True
            time = 0
    if dieing > 0 and not lives <= 0:
        dieing -= 1
        if dieing >= 110 and dieing <= 120:
            if channel.get_busy():
                pass
            else:
                channel.queue(death)
            player.stage1()
        elif dieing >= 100 and dieing < 110:
            player.stage2()
        elif dieing >= 90 and dieing < 100:
            player.stage3()
        elif dieing >= 80 and dieing < 90:
            player.stage4()
        elif dieing >= 70 and dieing < 80:
            player.stage5()
        elif dieing >= 60 and dieing < 70:
            player.stage6()
        if dieing == 1 and lives != 0:
            player.reset()
            player.right()
        background = pygame.Surface(screen.get_size())
        text = font.render("Score: " + str(score), True, RED)
        textpos = text.get_rect(centerx=background.get_width()/2)
        textpos.top = 30
        textpos.left = 1020
        text2 = font2.render("Lives: ", True, RED)
        textpos2 = text2.get_rect(centerx=background.get_width()/2)
        textpos2.top = 60
        textpos2.left = 1020
        font3 = pygame.font.Font(None, 50)
        screen.fill(BLACK)
        all_sprites.draw(screen)
        ghosts.draw(screen)
        if dieing >= 10 and dieing < 60 and lives != 0:
            text3 = font3.render("Get Ready!", True, WHITE)
            textpos3 = text.get_rect(centerx=background.get_width()/2)
            textpos3.top = 275
            textpos3.left = 400
            screen.blit(text3, textpos3)
        elif dieing >= 10 and dieing < 60 and lives == 0:
            dieing = 0
        screen.blit(text, textpos)
        screen.blit(text2, textpos2)        
        pygame.display.flip()
    elif game_over and time < 301:
        time += 1
        dieing -= 1
        if dieing >= 110 and dieing <= 120:
            players.add(player)
            if channel.get_busy():
                pass
            else:
                channel.queue(death)
            player.stage1()
        elif dieing >= 100 and dieing < 110:
            player.stage2()
        elif dieing >= 90 and dieing < 100:
            player.stage3()
        elif dieing >= 80 and dieing < 90:
            player.stage4()
        elif dieing >= 70 and dieing < 80:
            player.stage5()
        elif dieing >= 60 and dieing < 70:
            player.stage6()
        background = pygame.Surface(screen.get_size())
        text = font.render("Score: " + str(score), True, RED)
        textpos = text.get_rect(centerx=background.get_width()/2)
        textpos.top = 30
        textpos.left = 1020
        text2 = font2.render("Lives: ", True, RED)
        textpos2 = text2.get_rect(centerx=background.get_width()/2)
        textpos2.top = 60
        textpos2.left = 1020
        font3 = pygame.font.Font(None, 50)
        text3 = font3.render("GAME OVER: " + str(score), True, WHITE)
        textpos3 = text.get_rect(centerx=background.get_width()/2)
        textpos3.top = 275
        textpos3.left = 350
        screen.fill(BLACK)
        all_sprites.draw(screen)
        ghosts.draw(screen)
        players.draw(screen)
        screen.blit(text3, textpos3)
        screen.blit(text, textpos)
        screen.blit(text2, textpos2)        
        pygame.display.flip()
    elif winner and time < 301:
        time += 1
        background = pygame.Surface(screen.get_size())
        text = font.render("Score: " + str(score), True, RED)
        textpos = text.get_rect(centerx=background.get_width()/2)
        textpos.top = 30
        textpos.left = 1020
        text2 = font2.render("Lives: ", True, RED)
        textpos2 = text2.get_rect(centerx=background.get_width()/2)
        textpos2.top = 60
        textpos2.left = 1020
        font3 = pygame.font.Font(None, 50)
        text3 = font3.render("YOU WIN: " + str(score), True, WHITE)
        textpos3 = text.get_rect(centerx=background.get_width()/2)
        textpos3.top = 280
        textpos3.left = 400
        screen.fill(BLACK)
        all_sprites.draw(screen)
        ghosts.draw(screen)
        screen.blit(text3, textpos3)
        screen.blit(text, textpos)
        screen.blit(text2, textpos2)        
        pygame.display.flip()
    elif time < 0:
        time += 1
        background = pygame.Surface(screen.get_size())
        text = font.render("Score: " + str(score), True, RED)
        textpos = text.get_rect(centerx=background.get_width()/2)
        textpos.top = 30
        textpos.left = 1020
        text2 = font2.render("Lives: ", True, RED)
        textpos2 = text2.get_rect(centerx=background.get_width()/2)
        textpos2.top = 60
        textpos2.left = 1020
        font3 = pygame.font.Font(None, 50)
        text3 = font3.render("Begin!", True, WHITE)
        textpos3 = text.get_rect(centerx=background.get_width()/2)
        textpos3.top = 275
        textpos3.left = 450
        screen.fill(BLACK)
        all_sprites.draw(screen)
        screen.blit(text3, textpos3)
        screen.blit(text, textpos)
        screen.blit(text2, textpos2)        
        pygame.display.flip()
    
        
    else:
        if channel2.get_busy():
            pass
        else:
            channel2.queue(siren)
        background = pygame.Surface(screen.get_size())
        text = font.render("Score: " + str(score), True, RED)
        textpos = text.get_rect(centerx=background.get_width()/2)
        textpos.top = 30
        textpos.left = 1020
        text2 = font2.render("Lives: ", True, RED)
        textpos2 = text2.get_rect(centerx=background.get_width()/2)
        textpos2.top = 60
        textpos2.left = 1020
        screen.fill(BLACK)
        screen.blit(text, textpos)
        screen.blit(text2, textpos2)
        all_sprites.update()
        all_sprites.draw(screen)
        ghosts.update()
        ghosts.draw(screen)
        pygame.display.flip()
        clock.tick(30)
    if time > 300:
        done = True
    if lives == 0:
        game_over = True
pygame.quit()

