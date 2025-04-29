class Item:
    def __init__(self, name, value, count, icon, description, book):
        self.name = name
        self.value = value
        self.count = count
        self.icon = icon
        self.desc = description
        self.book = book

# Fish images are not made by me and
# The ones that are mine look bad
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