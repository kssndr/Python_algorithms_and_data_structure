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
            return self.cards.pop()


# desk = Desk()
# for card in desk.cards:
#     print(card)


class Player:
    def __init__(self, name):
        self.name = name
        self.wins = 0
        self.cards = None


# alex = Player("Alexander")
# print(alex.name)

class Game:
    def __init__(self):
        name1 = input("Player 1: ")
        name2 = input("Player 2: ")
        self.desk = Desk()
        self.p1 = Player(name1)
        self.p2 = Player(name2)

    def wins(self, winner):
        w = "{} take the cards"
        w = w.format(winner)
        print(w)

    def draw(self, p1n, p1c, p2n, p2c):
        d = "{} puts {} and {} puts {}"
        d = d.format(p1n, p1c, p2n, p2c)
        print(d)

    def play_game(self):
        cards = self.desk.cards
        print("Play!")
        while len(cards) > 2:
            m = "Play game or press X to exit"
            responce = input(m)
            if responce == "X":
                break
            p1c = self.desk.rm_card()
            p2c = self.desk.rm_card()
            p1n = self.p1.name
            p2n = self.p2.name
            self.draw(p1n, p1c, p2n, p2c)
            if p1c > p2c:
                self.p1.wins += 1
                self.wins(self.p1.name)
            else:
                self.p2.wins += 1
                self.wins(self.p2.name)

        win = self.winner(self.p1, self.p2)

        print("Game over. {} winner! {}/{}".format(win, self.p1.wins, self.p2.wins))

    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p2.wins > p1.wins:
            return p2.name
        return "No winner"


game = Game()
game.play_game()


