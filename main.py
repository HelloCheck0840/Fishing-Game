import pygame, time
import random
from sys import exit
from items import item_data
from image import *
import e

pygame.init()

# settings
resolution = [1920, 1080]
FPS = 60
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

assets = {
    'player': load_image('placeholderp.png'),
    'ocean': load_image('Background/Ocean.png'),
    'dock': load_image('Background/Dock.png'),
    'sky': load_image('Background/8bit-pixel-graphic-blue-sky-background-with-clouds-vector.png'),
    'bar': load_image_alpha('UI/bar.png'),
    'bar_area': load_image_alpha('UI/area.png'),
    'bar_bar': load_image_alpha('UI/bar2.png'),
    'progress_bar': load_image_alpha('UI/progress-bar.png'),
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
    def __init__(self, cols):
        self.items = {}
        self.cols = cols

    def add(self, num, count = 1):
        self.items[num] = item_data[num]
        self.items[num].count += count

    def remove(self, id, count = 1):
        self.items[id].count -= count

    def render(self, surf, icon):
        idx_items = {key: i for i, key in enumerate(inv.items)}
        size = [480 // 1.2, 270 // 1.2]
        box = pygame.Surface(size)
        slot_size = size[0] // self.cols
        row = 0
        x = 0
        
        surf.blit(box, (0, 0))
        for i in self.items:
            #image_icon = load_image(self.items[str(i)].icon)
            #image_icon = pygame.transform.scale(image_icon, (int(slot_size * 0.975), int(slot_size * 0.975)))
            image_icon = pygame.Surface((int(slot_size * 0.975), int(slot_size * 0.975)))
            image_icon.fill('gray')
            surf.blit(image_icon, ((idx_items[str(i)] - (row * self.cols)) * slot_size, (row * slot_size) + 20))
            surf.blit(load_text(str(self.items[str(i)].count), int(slot_size) // 2, (255, 255, 255)), ((idx_items[str(i)] - (row * self.cols)) * slot_size + 2, (row * slot_size) + 22))
            x += 1
            if x == self.cols:
                x = 0
                row += 1

inv_open = False
inv = Inventory(8)

for i in range(1, 17):
    inv.add(str(i), 1)

#slot = draw_surface((40, 40), ('white'))

# Index
class Index():
    def __init__(self):
        self.index = []
    
    def add(self, item_id):
        self.index.append(item_data[str(item_id)])
        self.index = list(dict.fromkeys(self.index))
        print(self.index)
    
    def open(self, check):
        for i in self.index:
            load_text(self.index[str(i)].desc, 50, 'black')

    def render(self):
        pass

idx = Index()
for i in range(1, 17):
    idx.add(i)

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
        surf.blit(assets['bar'], (140, 202))
        surf.blit(assets['bar_area'], ((self.area[0] * 2) + 140, 202))
        surf.blit(assets['bar_bar'], (min((self.bar * 2) + 140, 337), 201))
        surf.blit(assets['progress_bar'], (140, 217))
        surf.blit(draw_surface((percent * 2, 4), (153, 229, 80, 158)), (141, 218))

center = random.randint(15, 75)
bar_move = False
inside = 0
timer = 0
i = None
difference = 0
fishing = False
cooldown = 0

fish = Fish(50, center, 90)

# Background
ocean_r = assets['ocean'].get_rect(bottomleft = (0, 270))
dock_r = assets['dock'].get_rect(topleft = (64, 125))
sky_r = assets['sky'].get_rect(bottomleft = (ocean_r.left, ocean_r.top))

prevtime = time.time()

# main loop
while True:
    dt = time.time() - prevtime
    prevtime = time.time()

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
            if inv_open == False:
                if event.key == pygame.K_d:
                    movement[1] = 1
                if event.key == pygame.K_a:
                    movement[0] = 1
                if event.key == pygame.K_g:
                    inv.add('1', 1)
            if event.key == pygame.K_TAB:
                inv_open = not inv_open
            

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                movement[0] = 0
            if event.key == pygame.K_d:
                movement[1] = 0

        if event.type == pygame.MOUSEBUTTONDOWN:
            if cooldown == 0 and inv_open == False:
                if event.button == 1:
                    if fishing == False:
                        fishing = True
                    else:
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
            fish_id = random.randint(1, 16)
            fishing = False
            inv.add(str(fish_id), 1)
            idx.add(fish_id)
            print(idx.index)
            cooldown = 60
        if fish.progress < 0:
            fishing = False
    else:
        fish.progress = 90
        if inv_open == True:
            inv.render(display, 'e')

    if player_rect.collidepoint((mouse_x, mouse_y)):
        display.blit(text, (mouse_x, mouse_y))

    clock.tick(FPS)
    pygame.display.flip()