class Card(object):

    FACES = {11: 'Jack', 12: 'Queen', 13: 'King', 14: 'Ace'}

    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        value = self.FACES.get(self.rank, self.rank)
        return "{0} of {1}".format(value, self.suit)

    def __lt__(self, other):
        return self.rank < other.rank

# for (a, b, c) in zip(num, color, value):
#      print a, b, c

    # if rank in ranks

# class Game:

#     def __init__(self, start, end, player_score, dealer_score, compare)


# class Card:

#     def __init__(self, suit, rank)


# class Deck:

#     def __init__(self, refresh, shuffle, deal, used_once)


# class Dealer:

#     def __init__(self, deal_cards, give_new_cards, hit, stay)


# class Player:

#     def __init__(self, hit, stay)

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
