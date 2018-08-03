import random

class Player:

    def __init__(self):
        self.hand = list(range(1,14))
        self.score = 0

    def get_card(self):
        return self.hand.pop(random.randint(0,len(self.hand)-1)), len(self.hand)

    def add_score(self, points):
        self.score += points

    def get_remaining_cards(self):
        return(self.hand)
