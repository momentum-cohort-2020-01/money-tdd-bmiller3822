import itertools

# cards = [suit, rank]
suits = ["H", "S", "C", "D"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
# for (a, b) in zip(suits, ranks):
    # print(a+b)

# for (a, b, c) in zip(num, color, value): 
#      print a, b, c 


    # if rank in ranks 

# class Game:

#     def __init__(self, start, end, player_score, dealer_score, compare)

#     pass


class Card: 

    def __init__(self, suit, rank):

        self.suit = suit
        self.rank = rank

    def show(self):
        print("{} of {}".format(self.rank, self.suit))

    # pass


class Deck: 

    def __init__(self):  #, refresh, shuffle, deal, used_once
    
        self.cards = self.build()

    def build(self):
        for s in suits:
            for r in ranks:
                self.cards.append(Card(s, r))
                return self.cards

     print self.cards3               
    # def show(self):
    #     for c in self.cards:
    #         c.show()
    # deck = Deck()
    # deck.show()

    # pass



# class Dealer: 

#     def __init__(self, deal_cards, give_new_cards, hit, stay)

#     pass


# class Player: 

#     def __init__(self, hit, stay)

#     pass
    #===============Notes==========================

    # my_string = [word for word in my_string.split() if word not in STOP_WORDS]  #This becomes a list


    
    #1 we need to create a deck by making a list with one of each key value pair
    #2 Need to randomize the deck (shuffle)
    #3 Start a game
    #4 Give players 2 cards
    #5 Let player hit (give card) or stay (move on)
    #6 Count the player's value of their hand
    #7 Dealer hits or stays
    #8 Count the dealer's value of their hand
    #9 Compare the values to see who wins
    #10 Determine a winner
    #11 Start a new game