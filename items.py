class Item:
    def __init__(self, name, value, count, icon, description):
        self.name = name
        self.value = value
        self.count = count
        self.icon = icon
        self.desc = description

    def render(self):
        pass

item_data = {
    '1': Item('Atlantic Bluefin Tuna', 100, 0, 'placeholder.png', 'facts about fish here'),
    '2': Item('Atlantic Cod', 100, 0, 'placeholder.png', 'facts about fish here'),
    '3': Item('Atlantic Goliath Grouper', 100, 0, 'placeholder.png', 'facts about fish here'),
    '4': Item('Atlantic Salmon', 100, 0, 'placeholder.png', 'facts about fish here'),
    '5': Item('Atlantic Trumpetfish', 100, 0, 'placeholder.png', 'facts about fish here'),
    '6': Item('Atlantic Wolffish', 100, 0, 'placeholder.png', 'facts about fish here'),
    '7': Item('Banded Butterflyfish', 100, 0, 'placeholder.png', 'facts about fish here'),
    '8': Item('Beluga Sturgeon', 100, 0, 'placeholder.png', 'facts about fish here'),
    '9': Item('Blue Marlin', 100, 0, 'placeholder.png', 'facts about fish here'),
    '10': Item('Blue Tang', 100, 0, 'placeholder.png', 'facts about fish here'),
    '11': Item('Bluebanded Goby', 100, 0, 'placeholder.png', 'facts about fish here'),
    '12': Item('Bluehead Wrasse', 100, 0, 'placeholder.png', 'facts about fish here'),
    '13': Item('California Grunion', 100, 0, 'placeholder.png', 'facts about fish here'),
    '14': Item('Chilean Common Hake', 100, 0, 'placeholder.png', 'facts about fish here'),
    '15': Item('Chilean Jack Mackerel', 100, 0, 'placeholder.png', 'facts about fish here'),
    '16': Item('Chinook Salmon', 100, 0, 'placeholder.png', 'facts about fish here')
}

print(item_data['1'].name)