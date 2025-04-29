import pygame, time
import random
from sys import exit

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
fish_ico = pygame.image.load('image/icon.ico')
pygame.display.set_icon(fish_ico)
display = pygame.Surface(res)

###########################################################################

# Images
BASE_PATH = 'image/'

# Loads images and removes any black color
def load_image(path):
    image = pygame.image.load(BASE_PATH + path).convert()
    image.set_colorkey((0, 0, 0))
    return image

# Loads images that have transparency
def load_image_alpha(path):
    image = pygame.image.load(BASE_PATH + path).convert_alpha()
    return image

# Makes a Surface and colors it in
def draw_surface(size, color):
    surf = pygame.Surface(size, pygame.SRCALPHA)
    surf.fill(color)
    return surf

###########################################################################

# Text
# Creates text
def load_text(text = 'Hi HelloCheck!', size = 16, color = (255, 255, 255)):
    font = pygame.font.Font('text/m6x11.ttf', size)
    text = font.render(text, False, color)
    return text

# Creates new line when it reaches a certain length
# Credits to CrazyChucky for these 2 lines of code in stack overflow
def new_line(text, length):
    lines = [text[i:i+length] + '\n' for i in range(0, len(text), length)]
    text = ''.join(lines)
    return text

###########################################################################

# Returns the numbers that centers a surface on another Surface
def cen_surface(surfa, display = res):
    cen = [(display[0] // 2) - (surfa.get_width() // 2), (display[1] // 2) - (surfa.get_height() // 2)]
    return cen

text = load_text('hello', 16, (255, 255, 255))

###########################################################################

# Assets
# The sky and the clouds are from https://free-game-assets.itch.io/free-sky-with-clouds-background-pixel-art-set
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

###########################################################################

# Item Data
class Item:
    def __init__(self, name, value, count, icon, description, book):
        self.name = name
        self.value = value
        self.count = count
        self.icon = icon
        self.desc = description
        self.book = book

    # Fish images that are inside the BookFish folder is from 
    # https://oceana.org/ocean-fishes/ turned into pixelated images
    # Also data

    # Blue Bandedgoby, California Grunion, Chilean Common Hake, Chilean Jack Mackerel, Blue Marlin, 
    # Atlantic Trumpetfish, Bluehead Wrasse fish icons are drawn by me
    # The rest of the fish icons are taken off of https://www.shutterstock.com/ royalty-free images and turned into pixelated images

    # Fish information is from ChatGPT

item_data = {
    '1': Item('Atlantic Bluefin Tuna', 100, 0, 'BluefinTuna.png',
              'Atlantic Bluefin Tuna are the largest tunas, growing up to 13 feet long and weighing as much as 2,000 pounds. They can live up to 40 years and are known for their incredible speed and deep diving abilities.',
              'AtlanticBluefinTuna.png'),
    '2': Item('Atlantic Cod', 100, 0, 'Cod.png',
              'Atlantic Cod can live more than 20 years and grow up to 51 inches and 77 pounds. They are top predators in the bottom ocean community, feeding on a variety of invertebrates and fish.',
              'AtlanticCod.png'),
    '3': Item('Atlantic Goliath Grouper', 100, 0, 'Grouper.png',
              'The Atlantic Goliath Grouper is the largest species of grouper in the Atlantic Ocean, reaching up to 8 feet in length and over 800 pounds in weight.',
              'AtlanticGoliathGrouper.png'),
    '4': Item('Atlantic Salmon', 100, 0, 'Salmon.png',
              'Atlantic Salmon are anadromous, hatching in freshwater and migrating to the ocean to grow. They return to freshwater to spawn, and larger individuals have more eggs, aiding population sustainability.',
              'AtlanticSalmon.png'),
    '5': Item('Atlantic Trumpetfish', 100, 0, 'Trumpetfish.png',
              'The Atlantic Trumpetfish uses its large snout and triangle-shaped head to create suction, allowing it to suck in prey like small fishes and mobile invertebrates.',
              'AtlanticTrumpetfish.png'),
    '6': Item('Atlantic Wolffish', 100, 0, 'Wolffish.png',
              'Atlantic Wolffish produce natural antifreeze to keep their blood flowing in cold waters. They are important predators, controlling populations of green crabs and sea urchins.',
              'AtlanticWolffish.png'),
    '7': Item('Banded Butterflyfish', 100, 0, 'Butterflyfish.png',
              'Banded Butterflyfish reproduce through broadcast spawning, where a female releases eggs and a male releases sperm into the water column above the reef simultaneously.',
              'BandedButterflyfish.png'),
    '8': Item('Beluga Sturgeon', 100, 0, 'Sturgeon.png',
              'The Beluga Sturgeon is the largest living freshwater fish, capable of growing up to 20 feet in length and weighing over 3,000 pounds.',
              'BelugaSturgeon.png'),
    '9': Item('Blue Marlin', 100, 0, 'Marlin.png',
              'Blue Marlins are among the largest and fastest fish, reaching up to 14 feet in length and weighing nearly 2,000 pounds. They are known for their spear-shaped upper jaws.',
              'BlueMarlin.png'),
    '10': Item('Blue Tang', 100, 0, 'Tang.png',
               'Blue Tangs can raise a pair of razor-sharp, venomous spines on either side of their tails when threatened, using them to deter predators.',
               'BlueTang.png'),
    '11': Item('Bluebanded Goby', 100, 0, 'BluebandedGoby.png',
               'Bluebanded Gobies are microcarnivores that eat small crustaceans on the reef surface and from the water column directly above the reef surface.',
               'BluebandedGoby.png'),
    '12': Item('Bluehead Wrasse', 100, 0, 'Wrasse.png',
               'Bluehead Wrasses are generalist foragers, eating a variety of prey including small invertebrates and crustaceans on the reef surface.',
               'BlueheadWrasse.png'),
    '13': Item('California Grunion', 100, 0, 'Grunion.png',
               'California Grunions are slender, silver fish measuring an average of 5 to 6 inches long. They are known for their unique spawning behavior on sandy beaches.',
               'CaliforniaGrunion.png'),
    '14': Item('Chilean Common Hake', 100, 0, 'Hake.png',
               'The Chilean Common Hake is a merluccid hake found along the coast of South America, from Peru to the Chilean coasts north to the Chiloé Archipelago.',
               'ChileanCommonHake.png'),
    '15': Item('Chilean Jack Mackerel', 100, 0, 'Mackerel.png',
               'Chilean Jack Mackerels are commonly 45 cm long, though they can grow to 70 cm. They have elongated and laterally compressed bodies.',
               'ChileanJackMackerel.png'),
    '16': Item('Chinook Salmon', 100, 0, 'ChinookSalmon.png',
               'Chinook Salmon, also known as King Salmon, are the largest species of Pacific salmon, known for their rich flavor and high oil content.',
               'ChinookSalmon.png'),
}

###########################################################################

# Animation Handler
# Code from Coding With Russ on youtube
# The video https://www.youtube.com/watch?v=nXOVcOBqFwM
# And www.youtube.com/watch?v=M6e3_8LHc7A

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

###########################################################################

# Player
class Entity():
    def __init__(self, pos, animations, frame, reverse, action):
        self.pos = list(pos)
        self.velocity = 0
        self.animation = animations
        self.frame = frame
        self.flip = reverse
        self.action = action
    
    # Movement
    # Update method from DaFluffyPotato on Youtube
    def update(self, movement = (0, 0)):
        move = [movement[0] + self.velocity, movement[1]]

        self.pos[0] += move[0]
        self.pos[1] += move[1]

    def render(self, surf):
        surf.blit(pygame.transform.flip(self.animation[self.action][self.frame], self.flip, False), self.pos)

player = Entity([240, 100], animation_list, 0, False, 0)

movement = [0, 0]

###########################################################################

# Inventory
class Inventory():
    def __init__(self, cols, pos):
        self.items = {}
        self.cols = cols
        self.pos = list(pos)

    # Adds item
    def add(self, num, count = 1):
        self.items[num] = item_data[num]
        self.items[num].count += count

    # Removes item
    def remove(self, id, count = 1):
        self.items[id].count -= count

    # Draws the whole inventory
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

###########################################################################

# Index
book = assets['book']
# Scales the book by 2
book = pygame.transform.scale(book, (book.get_width() * 2, book.get_height() * 2))
class Index():
    def __init__(self):
        self.index = []
    
    # Adds item to index
    def add(self, item_id):
        self.index.append(item_data[str(item_id)])
        self.index = list(dict.fromkeys(self.index))

    # renders the information
    def open(self, surf, page, pos = [0, 0]):
        surf.blit(load_text(self.index[page].name, 16, 'black'), (30 + pos[0], 30 + pos[1]))
        surf.blit(load_image('BookFish/' + self.index[page].book), (30 + pos[0], 50 + pos[1]))
        surf.blit(load_text(new_line(self.index[page].desc, 25), 14, 'black'), (190 + pos[0], 25 + pos[1]))

    # Opens book
    def render(self, surf, pos = [0, 0]):
        surf.blit(book, (0 + pos[0], 0 + pos[1]))

idx = Index()
page = 0
op = True

###########################################################################

# Fishing
class Fish():
    def __init__(self, bar, center, progress):
        self.bar = bar
        self.center = center
        self.area = [self.center - 15, self.center + 15]
        self.progress = progress

    # Handles minigame
    def minigame(self, movement, check):
        self.bar += movement
        self.progress += check

    # Shows minigame
    def render(self, surf, percent):
        surf.blit(assets['bar'], (140, 202))
        surf.blit(assets['bar_area'], ((self.area[0] * 2) + 140, 202))
        surf.blit(assets['bar_bar'], (min((self.bar * 2) + 140, 337), 201))
        surf.blit(assets['progress_bar'], (140, 217))
        surf.blit(draw_surface((percent * 2, 4), (153, 229, 80, 158)), (141, 218))

# variables for minigame
center = random.randint(15, 75)
bar_move = False
inside = 0
timer = 0
i = None
difference = 0
fishing = False
cooldown = 0

fish = Fish(50, center, 90)

###########################################################################

# Background
ocean_r = assets['ocean'].get_rect(bottomleft = (0, 270))
dock_r = assets['dock'].get_rect(topleft = (64, 125))
sky_r = assets['sky'].get_rect(bottomleft = (ocean_r.left, ocean_r.top))
cloud1 = assets['cloud1'].get_rect(bottomleft = (ocean_r.left, ocean_r.top))
cloud2 = assets['cloud2'].get_rect(bottomleft = (ocean_r.left, ocean_r.top))

# House
exterior_r = assets['outside'].get_rect(bottomleft = (dock_r.centerx - (assets['outside'].get_width() // 2), dock_r.top))
interior_r = assets['inside'].get_rect(bottomleft = (dock_r.centerx - (assets['inside'].get_width() // 2), dock_r.top))

# Main loop
while True:
    # Updates animation
    current_time = pygame.time.get_ticks()
    if current_time - last_update >= animation_cooldown:
        last_update = current_time
        player.frame += 1
        if player.frame >= len(animation_list[player.action]):
            player.frame = 0

    # Background
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

    # Cooldown for fishing
    cooldown -= 1
    cooldown = max(cooldown, 0)

    # event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if inv_open == False and op == True and fishing == False:
                # Movement
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
                # Opens inventory
                if event.key == pygame.K_TAB:
                    inv_open = not inv_open

                    # Tutorial
                    if tutorial and step == 1 and inv_open:
                        step += 1
                    elif tutorial and step == 2 and not inv_open:
                        step += 1

            if inv_open == False:
                # Opens book
                if event.key == pygame.K_j:
                    op = not op

                    # Tutorial
                    if tutorial and step == 3 and not op:
                       step += 1
                    if tutorial and step == 4 and op:
                       step += 1

        # Stops movement
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                movement[0] = 0
            if event.key == pygame.K_d:
                movement[1] = 0

        # Fishing
        if event.type == pygame.MOUSEBUTTONDOWN:
            if cooldown == 0 and inv_open == False:
                if event.button == 1:
                    if player.pos[0] > 387 or player.pos[0] < 78:
                        if fishing == False:
                            fishing = True
                        else:
                            bar_move = True
            
            # Cancels fishing
            if event.button == 3:
                fishing = False

        # Moves the bar to the left if the mouse is not held
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                if inv_open == False:
                    bar_move = -True

    # Movement for player
    player.update((movement[1] - movement[0], 0))
    # Animation change for player
    if movement[0] or movement[1] == 0:
        player.action = 0
    if movement[0] or movement[1] == 1:
        player.action = 1

    # Limits the player into a area
    if player.pos[0] > 391:
        player.pos[0] = 391
    if player.pos[0] < 73:
        player.pos[0] = 73

    # Renders the player
    player.render(display)

    # Fishing
    percentage = (fish.progress / 300) * 100

    if fishing == True:
        fish.render(display, percentage)
        fish_id = random.randint(1, 16)
        timer += 1

        # Changes position every 2 seconds
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

        # Makes progress go up if the bar is in the area
        if fish.bar >= fish.area[0] and fish.bar <= fish.area[1]:
            inside = 1
        
        # Makes progress go down if the bar is not in the area
        else:
            # Prevents progress from going below 0
            if fish.progress <= 0:
                fish.progress = 0
            if fish.progress > 0:
                inside = -1
                
        fish.minigame(bar_move, inside)

        # Limits where the bar can go
        if fish.bar > 100:
            fish.bar = 100
        if fish.bar < 0:
            fish.bar = 0

        # Fish is caught
        if fish.progress > 300:
            fishing = False
            inv.add(str(fish_id), 1)
            idx.add(fish_id)
            cooldown = 60

            # Tutorial
            if tutorial and step == 0:
                step += 1

        # Fish is not caught
        if fish.progress < 0:
            fishing = False
    else:
        # Resets the fish
        fish.progress = 90

        # Can open inventory when not fishing
        if inv_open == True:
            inv.render(display)

    keys = pygame.key.get_just_pressed()

    # Prevents page from going out of bounds
    if page < 0:
        page = 0
    if page > len(idx.index) - 1:
        page = len(idx.index) - 1 

    # Opens and closes the book
    if op == False:
        idx.render(display, [65, 25])
        if len(idx.index) > 0:
            idx.open(display, page, [65, 25])
        
        # Changes page number
        if keys[pygame.K_a]:
            page -= 1
        if keys[pygame.K_d]:
            page += 1

    # The tutorial
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
    
    # Updates the screen
    clock.tick(FPS)
    pygame.display.flip()