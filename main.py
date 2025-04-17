import pygame
import random
from sys import exit
from items import item_data

pygame.init()

# settings
resolution = [1920, 1080]
FPS = 60
BASE_PATH = 'image/'
clock = pygame.time.Clock()

# screen
screen = pygame.display.set_mode(resolution)
display = pygame.Surface((480, 270))
inventory_display = pygame.Surface(resolution)

# text
def load_text(text = 'Hi HelloCheck!', size = 16, color = (255, 255, 255)):
    font = pygame.font.Font('text/m6x11.ttf', size)
    text = font.render(text, False, color)
    return text

text = load_text('hello', 16, (255, 255, 255))

# image
def load_image(path, size, rotation):
    image = pygame.image.load(BASE_PATH + path).convert()
    image.set_colorkey((0, 0, 0))
    image = pygame.transform.scale(image, size)
    image = pygame.transform.rotate(image, rotation)
    return image

def draw_surface(size, color):
    surf = pygame.Surface(size, pygame.SRCALPHA)
    surf.fill(color)
    return surf

assets = {
    'player': load_image('placeholder.png', (16, 40), 0),
    'ocean': load_image('Background/Ocean.png', (480, 94), 0),
    'dock': load_image('Background/Dock.png', (352, 72), 0),
    'sky': load_image('Background/8bit-pixel-graphic-blue-sky-background-with-clouds-vector.png', (480, 270), 0),
    'placeholder': load_image('placeholder.png', (100, 10), 0)
}

# player
class Entity():
    def __init__(self, pos):
        self.pos = list(pos)
        self.velocity = 0

    def update(self, movement = (0, 0)):
        move = [movement[0] + self.velocity, movement[1]]

        self.pos[0] += move[0]
        self.pos[1] += move[1]

    def render(self, surface):
        surface.blit(assets['player'], self.pos)

player = Entity([240, 100])
movement = [0, 0]

# inventory
class Inventory():
    def __init__(self):
        self.items = {}

    def add(self, num, count = 1):
        self.items[num] = item_data[num]
        self.items[num]['count'] += count

    def remove(self, id, count = 1):
        self.items[id]['count'] -= count

    def render(self):
        print(self.items)

inv_open = False
inv = Inventory()

'''inv = assets['inventory']
inv.set_alpha(240)
inv_r = inv.get_rect(center = (display.get_width() // 2, display.get_height() // 2))
slot = draw_surface((40, 40), ('white'))'''

# Index
class Index():
    def __init__(self):
        self.index = []
    
    def add(self, item_id):
        self.index.append(item_data[str(item_id)])

    def render(self):
        pass

# Fishing
class Fish():
    def __init__(self, bar, center, progress):
        self.bar = bar
        self.center = center
        self.area = [self.center - 15, self.center + 15]
        self.progress = progress

    def minigame(self, movement, check):
        self.bar += movement
        self.progress += check

    def render(self, surf, percent):
        surf.blit(assets['placeholder'], (0, 0))
        surf.blit(draw_surface((30, 10), ('orange')), (self.area[0], 0))
        surf.blit(draw_surface((2, 12), (255, 255, 255)), (self.bar, 0))
        surf.blit(draw_surface((percent, 7), (100, 255, 100)), (0, 12))

center = random.randint(15, 75)
bar_move = False
inside = 0
timer = 0
i = None
difference = 0
fishing = False
cooldown = 0

fish = Fish(50, center, 60)

# Background
ocean_r = assets['ocean'].get_rect(bottomleft = (0, 270))
dock_r = assets['dock'].get_rect(topleft = (64, 125))
sky_r = assets['sky'].get_rect(bottomleft = (ocean_r.left, ocean_r.top))

# main loop
while True:
    screen.blit(pygame.transform.scale(display, resolution), (0, 0))
    display.fill((0, 0, 0))
    display.blit(assets['sky'], sky_r)
    display.blit(assets['dock'], dock_r)
    display.blit(assets['ocean'], ocean_r)

    mouse_x, mouse_y = pygame.mouse.get_pos()
    mouse_x //= resolution[0] // display.get_width()
    mouse_y //= resolution[1] // display.get_height()

    cooldown -= 1
    cooldown = max(cooldown, 0)

    # event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if fishing == False:
                if event.key == pygame.K_d:
                    movement[1] = 1
                if event.key == pygame.K_a:
                    movement[0] = 1
                if event.key == pygame.K_TAB:
                    inv_open = not inv_open

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                movement[0] = 0
            if event.key == pygame.K_d:
                movement[1] = 0

        if event.type == pygame.MOUSEBUTTONDOWN:
            if cooldown == 0:
                if event.button == 1:
                    if fishing == False:
                        fishing = True
                    else:
                        if inv_open == False:
                            bar_move = True

            if event.button == 3:
                fishing = False
                print(inv.items)

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                if inv_open == False:
                    bar_move = -True

    
    player.update((movement[1] - movement[0], 0))
    player_rect = pygame.Rect(player.pos[0], player.pos[1], assets['player'].get_width(), assets['player'].get_height())

    if player_rect.right > 407:
        player.pos[0] = 391
    if player.pos[0] < 73:
        player.pos[0] = 73

    player.render(display)
    
    

    # Fishing
    percentage = (fish.progress / 300) * 100

    if fishing == True:

        fish.render(display, percentage)
        timer += 1
        if timer == 120:
            timer = 0
            i = random.randint(-30, 30)
            fish.area = [(fish.center - 15) + i, (fish.center + 15) + i]

            if fish.area[0] < 0:
                difference = fish.area[0] + 100
                fish.area[0] += difference
                fish.area[1] += difference

            if fish.area[1] > 100:
                difference = fish.area[1] - 100
                fish.area[0] -= difference
                fish.area[1] -= difference

        if fish.bar >= fish.area[0] and fish.bar <= fish.area[1]:
            inside = 1
        else:
            if fish.progress <= 0:
                fish.progress = 0
            if fish.progress > 0:
                inside = -1
                
        fish.minigame(bar_move, inside)

        if fish.bar > 100:
            fish.bar = 100
        if fish.bar < 0:
            fish.bar = 0
        if fish.progress > 300:
            fishing = False
            inv.add(str(random.randint(1, 16)), 1)
            cooldown = 60
        if fish.progress < 0:
            fishing = False
    else:
        fish.progress = 60
            

    keys = pygame.key.get_pressed()

    if inv_open == True:
        pass

    if player_rect.collidepoint((mouse_x, mouse_y)):
        display.blit(text, (mouse_x, mouse_y))

    clock.tick(FPS)
    pygame.display.flip()