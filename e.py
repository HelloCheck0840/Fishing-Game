import random
from items import item_data
# Fishing
number = 50
bar = min(number, 100)
center = random.randint(15, 75)

class Fish():
    def __init__(self, bar, center):
        self.bar = bar
        self.center = center
        self.area = [self.center - 15, self.center + 15]
        self.progress = 0

    def throw(self):
        pass

    def minigame(self, movement):
        self.bar += movement
        

    def catch(self, inventory):
        item = str(random.randint(1, 16))
        fish = item_data[item]
        inventory.add(item, 1)

    def render(self):
        print(self.bar)

fish = Fish(number, center)
fish.bar += 100

if fish.bar > 100:
    fish.bar = 100

print(fish.area)