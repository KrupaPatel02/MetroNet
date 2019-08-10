import random


class Card():

    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    def __init__(self, suit=0, value=2):
        self.suit = suit
        self.value = value

    def __str__(self):
        return '%s of %s' % (Card.values[self.value], Card.suits[self.suit])

    def __lt__(self, other):
        if self.value < other.value:
            return True
        elif self.value > other.value:
            return False

        if self.suit < other.suit:
            return True
        elif self.suit > other.suit:
            return False

        return 0


class Deck():

    def __init__(self):
        self.cards = []
        for suit in range(4):
            for value in range(1, 14):
                card = Card(suit, value)
                self.cards.append(card)

    def __str__(self):
        s = []
        for card in self.cards:
            s.append(str(card))
        return '\n'.join(s)

    def addCard(self, card):
        self.cards.append(card)

    def removeCard(self, card):
        self.cards.remove(card)

    def popCard(self, i=-1):
        return self.cards.pop(i)

    def shuffle(self):
        random.shuffle(self.cards)

    def sort(self):
        sorting_method = input("Enter 'a' for ascending sort and 'd' for descending sort")
        if sorting_method == 'a':
            self.cards.sort()
        else:
            self.cards.sort(reverse=True)

    def moveCard(self, hand, num):
        for i in range(num):
            hand.addCard(self.popCard())



class Hand(Deck):

    def __init__(self, label=''):
        self.cards = []
        self.label = label


if __name__ == '__main__':

    deck = Deck()
    deck.shuffle()

    hand = Hand()

    deck.moveCard(hand, 7)
    hand.sort()
    print(hand)
