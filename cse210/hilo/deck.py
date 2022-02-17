import random
class Deck:
    def __init__(self):
        self.cards = [1,2,3,4,5,6,7,8,9,10,11,12,13]

    def draw(self):
        return random.choice(self.cards)