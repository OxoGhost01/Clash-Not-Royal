class Player:
    def __init__(self, name):
        self.name = name
        self.deck = []
        self.score = 0
        self.health = None

    def add_card(self, card):
        self.deck.append(card)

    def set_score(self, score):
        self.score = score

    def update_health(self):
        total_health = 0
        for card in self.deck:
            total_health += card.health
        self.health = total_health

    def add_card(self, card):
        self.deck.append(card)