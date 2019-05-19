from random import shuffle


class Card:
    suits = ["Heart", "Diamonds", "Crosses", "Peaks"]
    values = [None, None, "2", "3", "4", "5", "6", "7", "8","9", "10", "Jack", "Queen", "King", "Ace"]

    def __init__(self, v, s):
        self.value = v
        self.suit = s

    def __lt__(self, c2):
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.value:
                return True
            else:
                return False
        return False

    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.value:
                return True
            else:
                return False
        return False

    def __repr__(self):
        return str(self.values[self.value]) + " " + str(self.suits[self.suit])


"""
my_hand = Card(3, 2)
your_hand = Card(10, 1)
print(my_hand)
print(my_hand > your_hand)
print(my_hand < your_hand)
"""


class Desk:
    def __init__(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(0, 3):
                self.cards.append(Card(i, j))
        shuffle(self.cards)

    def rm_card(self):
        if len(self.cards) == 0:
            return None
        else:
            self.cards.pop()


desk = Desk()
for card in desk.cards:
    print(card)


class Player:
    def __init__(self, name):
        self.name = name
        self.wins = 0
        self.cards = None

