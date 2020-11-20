import random

class CardDeck:
    ranks = {2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14}
    suits = ['c', 'h', 's', 'd']
    cards = []
    for rank in ranks:
        for suit in suits:
            cards.append(str(str(rank) + str(suit)))
    def __init__(self):
        random.shuffle(self.cards)
    def ShowCards(self):
        for card in self.cards:
            print(card)
    def GiveCardByIndex(self, index):
        print(self.cards[index])
    def GiveCard(self):
        i = random.randint(0, len(self.cards)-1)
        print(self.cards[i])
        self.cards.pop(i)
    def Give5Card(self):
        self.GiveCard()
        self.GiveCard()
        self.GiveCard()
        self.GiveCard()
        self.GiveCard()
