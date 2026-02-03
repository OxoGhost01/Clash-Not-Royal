from card import *

class Game:
    def __init__(self, player):
        self.player = player
        self.monster = None
        self.heros = []
        self.init_all_cards()

    def isDeckFull(self):
        return len(self.player.deck) == 3

    def printDeck(self):
        if not self.player.deck:
            print("Your deck is empty")
        else:
            for i, card in enumerate(self.player.deck, start=1):
                print(f"{i}. {card}")
        print("\n")

    def printPlayableCards(self, playable):
        for i, card in enumerate(playable, start=1):
            print(f"{i}. {card}")

    def getPlayableCards(self):
        return [card for card in self.heros if card not in self.player.deck]
    
    def deckConfirmation(self):
        print("\n\n====== Deck confirmation ======\n")
        for i, card in enumerate(self.player.deck, start=1):
            print(f"{i}. {card}")
        choice = verify_player_input("Is this your deck ? (0 = no, 1 = yes)", 0, 1)
        return choice

    def init_deck(self):
        print("\n\n====== Deck creation ======\n")
        while not self.isDeckFull():
            print("\nYour Deck : \n")
            self.printDeck()
            print("\nAvailable cards : \n")
            playable = self.getPlayableCards()
            self.printPlayableCards(playable)
            choice = verify_player_input("Please choose a card: ", 1, len(playable))
            self.player.add_card(playable[choice - 1])
        
        choice = self.deckConfirmation()
        if not choice: self.init_deck()
        self.player.update_health()

    def clash(self):
        print("\n\n====== Clash ======\n")
        wave = 0
        while self.playerIsAlive():
            wave += 1
            self.player.score += 1
            print(f"\n\n====== Wave {wave} ======\n")
            self.monster = self.choose_monster()
            self.wave()

    def init_all_cards(self):
        heros = get_all_heros()
        for hero in heros:
            self.heros.append(Card(hero["name"], hero["attack"], hero["defense"], hero["health"]))

    def choose_monster(self):
        monster = pick_monster()
        return Card(monster["name"], monster["attack"], monster["defense"], monster["health"])

    def wave(self):
        while self.isMonsterAlive():
            print("\nYour deck :")
            self.printDeck()
            print("\nMonster :")
            print(self.monster)
            self.playerTurn()
            self.monsterTurn()
            self.printDeck()

    def playerIsAlive(self):
        self.player.update_health()
        return self.player.health > 0
    
    def isMonsterAlive(self):
        return self.monster.health > 0

    def playerTurn(self):
        print("\n====== Player turn ======")
        for card in self.player.deck:
            card.attack_target(self.monster)
    
    def monsterTurn(self):
        print("\n====== Monster turn ======")
        for card in self.player.deck:
            self.monster.attack_target(card)
