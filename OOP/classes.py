import random


class Coin:
    def __init__(self, rare=False, clean=True, heads=True, **kwargs):

        for key, value in kwargs.items():
            setattr(self, key, value)  # set state/ set attribute
               
        self.heads = True
        self.is_rare = rare
        self.is_clean = clean

        if self.is_rare:
            self.value = self.original_value * 1.25
        else:
            self.value = self.original_value

        if self.is_clean:
            self.colour = self.original_colour
        else:
            self.colour = self.rusty_colour

        def rust(self):
            self.colour = "greenish"

        def clean(self):
            self.colour = "gold"

        def __del__(self):
            print("Coin spent")
       
        def flip(self):
            heads_options = [True, False]
            choice = random.choice(heads_options)
            self.heads = choice

        def __str__(self):
            if self.original_value > 1.00:
                return "{} coin".format(int(self.original_value))
            else:
                return "{}p Coin:".format(int(self.original_value * 100))
            


# Pound inherits from coin     
class Pound(Coin):
    def __init__(self):
        data = {
            "original_value": 1.00,
            "clean_colour": "gold",
            "rusty_colour": "greenish",
            "num_edges": 1,
            "diameter": 22.5,
            "thickness": 3.15,
            "mass": 9.5
        }
        super().__init__(**data)  # super = parent class 

class two_pence(Coin):
    def __init__(self):
        data = {
            "original_value": 0.05,
            "clean_colour": "silver",
            "rusty_colour": None,
            "num_edges": 1,
            "diameter": 18.0,
            "thickness": 1.77,
            "mass": 3.25
        }
        super().__init__(**data)  # super = parent class

        # override
        def rust(self):
            self.colour = self.clean_colour

        def clean(self):
            self.colour = self.clean_colour

coins = [two_pence, Pound]

for coin in coins:
    arguments = [coin, coin.colour, coin.value, coin.diameter, coin.thickness, coin.num_edges, coin.mass]
    
    string = "{}-Colour: {}, diameter(mm):{}, thickness(mm):{},
number of edges:{}, mass(g):{}".format(*arguments)

#  coin1 = Pound(rare=True)

#  coin1.value

#  coin1.colour = "greenish"

#  del coin1

#  coin2.colour  # Gold classes are base templates

#  print(type(coin1))
