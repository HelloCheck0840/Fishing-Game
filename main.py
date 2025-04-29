import pygame, time
import random
import re
from sys import exit
from items import item_data
from image import *

pygame.init()

# settings
resolution = [1920, 1080]
res = [480, 270]
FPS = 60
clock = pygame.time.Clock()
tutorial = True
step = 0

# screen
screen = pygame.display.set_mode(resolution)
pygame.display.set_caption('Fishing Game')
fish_ico = pygame.image.load('image/fish.ico')
pygame.display.set_icon(fish_ico)
display = pygame.Surface(res)

# text
def load_text(text = 'Hi HelloCheck!', size = 16, color = (255, 255, 255)):
    font = pygame.font.Font('text/m6x11.ttf', size)
    text = font.render(text, False, color)
    return text

# Credits to CrazyChucky for these 2 lines of code in stack overflow
def new_line(text, length):
    lines = [text[i:i+length] + '\n' for i in range(0, len(text), length)]
    text = ''.join(lines)
    return text

def cen_surface(surfa, display = res):
    cen = [(display[0] // 2) - (surfa.get_width() // 2), (display[1] // 2) - (surfa.get_height() // 2)]
    return cen

text = load_text('hello', 16, (255, 255, 255))

assets = {
    'player': load_image_alpha('player.png'),
    'ocean': load_image('Background/Ocean.png'),
    'dock': load_image('Background/Dock.png'),
    'sky': load_image('Background/Cloud/1.png'),
    'cloud1': load_image_alpha('Background/Cloud/2.png'),
    'cloud2': load_image_alpha('Background/Cloud/4.png'),
    'bar': load_image_alpha('UI/bar.png'),
    'bar_area': load_image_alpha('UI/area.png'),
    'bar_bar': load_image_alpha('UI/bar2.png'),
    'progress_bar': load_image_alpha('UI/progress-bar.png'),
    'book': load_image_alpha('UI/book.png'),
    'inside': load_image('House/Inside.png'),
    'outside': load_image('House/Outside.png')
}

# Animation Handler
# Code from Coding With Russ on youtube
class SpriteSheet():
    def __init__(self, image):
        self.sheet = image
    
    def get_image(self, frame, width, height):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.sheet, (0, 0), ((frame * width), 0, width, height))
        image.set_colorkey((0, 0, 0))
        return image

player = load_image_alpha('player.png')
sprite_sheet = SpriteSheet(player)

animation_list = []
animation_steps = [4, 2]
last_update = pygame.time.get_ticks()
animation_cooldown = 250
step_counter = 0

for animation in animation_steps:
    temp_list = []
    for _ in range(animation):
        temp_list.append(sprite_sheet.get_image(step_counter, 16, 40))
        step_counter += 1
    animation_list.append(temp_list)

# player
class Entity():
    def __init__(self, pos, e_type, animations, frame, reverse, action):
        self.pos = list(pos)
        self.velocity = 0
        self.type = e_type
        self.animation = animations
        self.frame = frame
        self.flip = reverse
        self.action = action

    def update(self, movement = (0, 0)):
        move = [movement[0] + self.velocity, movement[1]]

        self.pos[0] += move[0]
        self.pos[1] += move[1]

    def render(self, surf):
        surf.blit(pygame.transform.flip(self.animation[self.action][self.frame], self.flip, False), self.pos)

player = Entity([240, 100], 'player', animation_list, 0, False, 0)

movement = [0, 0]

# inventory
class Inventory():
    def __init__(self, cols, pos):
        self.items = {}
        self.cols = cols
        self.pos = list(pos)

    def add(self, num, count = 1):
        self.items[num] = item_data[num]
        self.items[num].count += count

    def remove(self, id, count = 1):
        self.items[id].count -= count

    def render(self, surf):
        idx_items = {key: i for i, key in enumerate(inv.items)}
        size = [480 // 1.2, 270 // 1.2]
        box = pygame.Surface(size)
        box.fill((102, 57, 49))
        slot_size = size[0] // self.cols
        row = 0
        x = 0
        inv_text = load_text('Inventory', 20)
        
        surf.blit(box, (self.pos[0] - 1, self.pos[1]))
        surf.blit(inv_text, (cen_surface(inv_text, size)[0] + self.pos[0], 2 + self.pos[1]))
        for i in self.items:
            image_icon = load_image('Fish/' + self.items[str(i)].icon)
            image_icon = pygame.transform.scale(image_icon, (int(slot_size * 0.975), int(slot_size * 0.975)))
            surf.blit(image_icon, ((idx_items[str(i)] - (row * self.cols)) * slot_size + self.pos[0], (row * slot_size) + 22 + self.pos[1]))
            surf.blit(load_text(str(self.items[str(i)].count), int(slot_size) // 3, (255, 255, 255)), ((idx_items[str(i)] - (row * self.cols)) * slot_size + 2 + self.pos[0], (row * slot_size) + 24 + self.pos[1]))
            surf.blit(load_text(str(self.items[str(i)].value), int(slot_size) // 5, (255, 255, 255)), ((idx_items[str(i)] - (row * self.cols)) * slot_size + 2 + self.pos[0], (row * slot_size) + 60 + self.pos[1]))
            x += 1
            if x == self.cols:
                x = 0
                row += 1

inv_open = False
inv = Inventory(8, cen_surface(pygame.Surface((480 // 1.2, 270 // 1.2)), res))

# Index
book = assets['book']
book = pygame.transform.scale(book, (book.get_width() * 2, book.get_height() * 2))
class Index():
    def __init__(self):
        self.index = []
    
    def add(self, item_id):
        self.index.append(item_data[str(item_id)])
        self.index = list(dict.fromkeys(self.index))

    def open(self, surf, page, pos = [0, 0]):
        surf.blit(load_text(self.index[page].name, 16, 'black'), (30 + pos[0], 30 + pos[1]))
        surf.blit(load_image('BookFish/' + self.index[page].book), (30 + pos[0], 50 + pos[1]))
        surf.blit(load_text(new_line(self.index[page].desc, 25), 14, 'black'), (190 + pos[0], 25 + pos[1]))

    def render(self, surf, pos = [0, 0]):
        surf.blit(book, (0 + pos[0], 0 + pos[1]))

idx = Index()
page = 0
op = True

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
cloud1 = assets['cloud1'].get_rect(bottomleft = (ocean_r.left, ocean_r.top))
cloud2 = assets['cloud2'].get_rect(bottomleft = (ocean_r.left, ocean_r.top))

# House
exterior_r = assets['outside'].get_rect(bottomleft = (dock_r.centerx - (assets['outside'].get_width() // 2), dock_r.top))
interior_r = assets['inside'].get_rect(bottomleft = (dock_r.centerx - (assets['inside'].get_width() // 2), dock_r.top))

# main loop
while True:
    current_time = pygame.time.get_ticks()
    if current_time - last_update >= animation_cooldown:
        last_update = current_time
        player.frame += 1
        if player.frame >= len(animation_list[player.action]):
            player.frame = 0

    screen.blit(pygame.transform.scale(display, resolution), (0, 0))
    display.fill((0, 0, 0))
    display.blit(assets['sky'], sky_r)
    display.blit(assets['cloud1'], cloud1)
    display.blit(assets['cloud2'], cloud2)
    display.blit(assets['inside'], (0, 0))
    if player.pos[0] < 144 or player.pos[0] > 320:
        display.blit(assets['outside'], (0, 0))
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
            if inv_open == False and op == True and fishing == False:
                if event.key == pygame.K_d:
                    movement[1] = 1
                    player.flip = False
                    player.action = 1
                    player.frame = 0
                if event.key == pygame.K_a:
                    movement[0] = 1
                    player.flip = True
                    player.action = 1
                    player.frame = 0

            if op == True:
                if event.key == pygame.K_TAB:
                    inv_open = not inv_open
                    if tutorial and step == 1 and inv_open:
                        step += 1
                    elif tutorial and step == 2 and not inv_open:
                        step += 1
            if inv_open == False:
                if event.key == pygame.K_j:
                    op = not op
                    if tutorial and step == 3 and not op:
                       step += 1
                    if tutorial and step == 4 and op:
                       step += 1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                movement[0] = 0
            if event.key == pygame.K_d:
                movement[1] = 0

        if event.type == pygame.MOUSEBUTTONDOWN:
            if cooldown == 0 and inv_open == False:
                if event.button == 1:
                    if player.pos[0] > 387 or player.pos[0] < 78:
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
    if movement[0] or movement[1] == 0:
        player.action = 0
    if movement[0] or movement[1] == 1:
        player.action = 1

    if player.pos[0] > 391:
        player.pos[0] = 391
    if player.pos[0] < 73:
        player.pos[0] = 73

    player.render(display)

    # Fishing
    percentage = (fish.progress / 300) * 100

    if fishing == True:
        fish.render(display, percentage)
        fish_id = random.randint(1, 16)
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
            inv.add(str(fish_id), 1)
            idx.add(fish_id)
            cooldown = 60
            if tutorial and step == 0:
                step += 1
        if fish.progress < 0:
            fishing = False
    else:
        fish.progress = 90
        if inv_open == True:
            inv.render(display)

    keys = pygame.key.get_just_pressed()

    if page < 0:
        page = 0
    if page > len(idx.index) - 1:
        page = len(idx.index) - 1 

    if op == False:
        idx.render(display, [65, 25])
        if len(idx.index) > 0:
            idx.open(display, page, [65, 25])

        if keys[pygame.K_a]:
            page -= 1
        if keys[pygame.K_d]:
            page += 1

    if tutorial == True:
        if step == 0:
            display.blit(load_text('Go to one of the sides to fish!', color = 'black'), (0, 0))
        elif step == 1:
            display.blit(load_text('Press "Tab" to open the inventory.', color = 'black'), (0, 0))
        elif step == 2:
            display.blit(load_text('Press "Tab" again to close the inventory.', color = 'black'), (0, 0))
        elif step == 3:
            display.blit(load_text('Press "J" to learn about the fishes you caught.', color = 'black'), (0, 0))
        elif step == 4:
            display.blit(load_text("Press 'a and d' to change pages. (For now you don't have enough pages)", color = 'black'), (0, 0))
            display.blit(load_text('Press "J" again to close the book.', color = 'black'), (0, 20))
        else:
            tutorial = False
    clock.tick(FPS)
    pygame.display.flip()