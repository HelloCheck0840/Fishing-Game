'''
# backup
class Item():
    def __init__(self, fish_id, fish_name, fish_value, fish_count, fish_icon, fish_description):
        self.id = fish_id
        self.name = fish_name
        self.value = fish_value
        self.count = fish_count
        self.icon = fish_icon
        self.description = fish_description

cod = Item('1', 'Cod', 100, 0, 'cod', 'facts about cods here')
salmon = Item('2', 'Salmon', 100, 0, 'salmon', 'facts about salmon here')
tuna = Item('3', 'Tuna', 100, 0, 'tuna', 'A large, fast swimming ocean fish.')
trout = Item('4', 'Trout', 100, 0, 'trout', 'A freshwater fish often found in rivers and lakes.')
sardine = Item('5', 'Sardine', 100, 0, 'sardine', 'A freshwater fish often found in rivers and lakes.')
sea_bass = Item('6', 'Sea bass', 100, 0, 'seabass', 'A freshwater fish often found in rivers and lakes.')
herring = Item('7', 'Herring', 100, 0, 'herring', 'A freshwater fish often found in rivers and lakes.')
catfish = Item('8', 'Catfish', 100, 0, 'catfish', 'A freshwater fish often found in rivers and lakes.')
bluegill = Item('9', 'Bluegill', 100, 0, 'fish', 'A small freshwater sunfish commonly found in North American lakes and ponds.')
rainbow_trout = Item('10', 'Rainbow Trout', 100, 0, 'fish', 'A colorful freshwater fish prized by anglers, native to North America.')
northern_pike = Item('11', 'Northern Pike', 100, 0, 'fish', 'A long, predatory fish known for its sharp teeth and aggressive behavior.')
channel_catfish = Item('12', 'Channel Catfish', 100, 0, 'fish', 'A bottom-dwelling freshwater fish known for its whisker-like barbels.')
largemouth_bass = Item('13', 'Largemouth Bass', 100, 0, 'fish', 'A freshwater fish with large, pointed teeth, prized for its meat.')
atlantic_mackerel = Item('14', 'Atlantic Mackerel', 100, 0, 'fish', 'A freshwater fish often found in rivers and lakes.')
yellow_perch = Item('15', 'Yellow Perch', 100, 0, 'fish', 'A small freshwater fish with yellow and black vertical stripes, commonly found in North America.')
walleye = Item('16', 'Walleye', 100, 0, 'fish', 'A nocturnal freshwater predator with excellent low-light vision, prized for its meat.')
'''

item_data = {
    '1': {
        'name': 'Cod',
        'value': 100,
        'count': 0,
        'icon': 'cod',
        'description': 'facts about cods here'
    },
    '2': {
        'name': 'Salmon',
        'value': 100,
        'count': 0,
        'icon': 'salmon',
        'description': 'facts about salmon here'
    },
    '3': {
        'name': 'Tuna',
        'value': 100,
        'count': 0,
        'icon': 'tuna',
        'description': 'A large, fast swimming ocean fish.'
    },
    '4': {
        'name': 'Trout',
        'value': 100,
        'count': 0,
        'icon': 'trout',
        'description': 'A freshwater fish often found in rivers and lakes.'
    },
    '5': {
        'name': 'Sardine',
        'value': 100,
        'count': 0,
        'icon': 'sardine',
        'description': 'Small, oily fish often packed in cans.'
    },
    '6': {
        'name': 'Sea Bass',
        'value': 100,
        'count': 0,
        'icon': 'seabass',
        'description': 'A common name for various saltwater fish.'
    },
    '7': {
        'name': 'Herring',
        'value': 100,
        'count': 0,
        'icon': 'herring',
        'description': 'Forage fish often found in large schools.'
    },
    '8': {
        'name': 'Catfish',
        'value': 100,
        'count': 0,
        'icon': 'fish',
        'description': 'Named for their whisker-like barbels, often found in rivers.'
    },
    '9': {
        'name': 'Bluegill',
        'value': 100,
        'count': 0,
        'icon': 'fish',
        'description': 'A small freshwater sunfish commonly found in North American lakes and ponds.'
    },
    '10': {
        'name': 'Rainbow Trout',
        'value': 100,
        'count': 0,
        'icon': 'fish',
        'description': 'A colorful freshwater fish prized by anglers, native to North America.'
    },
    '11': {
        'name': 'Northern Pike',
        'value': 100,
        'count': 0,
        'icon': 'fish',
        'description': 'A long, predatory fish known for its sharp teeth and aggressive behavior.'
    },
    '12': {
        'name': 'Channel Catfish',
        'value': 100,
        'count': 0,
        'icon': 'fish',
        'description': 'A bottom-dwelling freshwater fish known for its whisker-like barbels.'
    },
    '13': {
        'name': 'Largemouth Bass',
        'value': 100,
        'count': 0,
        'icon': 'fish',
        'description': 'A popular game fish in freshwater, known for its fighting spirit.'
    },
    '14': {
        'name': 'Atlantic Salmon',
        'value': 100,
        'count': 0,
        'icon': 'fish',
        'description': 'A migratory fish species known for returning to its birthplace to spawn.'
    },
    '15': {
        'name': 'Yellow Perch',
        'value': 100,
        'count': 0,
        'icon': 'fish',
        'description': 'A small freshwater fish with yellow and black vertical stripes, commonly found in North America.'
    },
    '16': {
        'name': 'Walleye',
        'value': 100,
        'count': 0,
        'icon': 'fish',
        'description': 'A nocturnal freshwater predator with excellent low-light vision, prized for its meat.'
    }
}

