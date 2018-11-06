import random

class Pound:

    def __init__(self, rare=False): # constructor
        
        self.rare = rare

        if self.rare:
            self.value = 1.25
        else:
            self.value = 1
            
        self.colour = "gold"
        self.num_edges = 1
        self.diameter = 22.5  # milimeters
        self.thickness = 3.15  # milimeters
        self.heads = True

    def __del__(self): # destructor
        print("Coin spent")

    def rust(self):
        self.colour = "greenish"

    def clean(self):
        self.colour = "gold"

    def flip(self):
        heads_options = [True, False]
        choice = random.choice(heads_options)
        self.heads = choice
    

  
coin1 = Pound(rare=True)

coin1.value

coin1.colour = "greenish"

del coin1

coin2.colour  # Gold classes are base templates

print(type(coin1))
