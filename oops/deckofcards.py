import random


class Cards:

    def __init__(self):
        pass

    def shuffle(self):
        suits = ["C", "D", "H", "S"]  # for (Clubs Diamonds Hearts Spades)
        Rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]  # for 13 cards (2-10 and face cards)

        list_cards = []  # for taking


        while len(list_cards) < 37:

                card_rank = " "
                random_int = random.randint(0, 12) #generating random values from 0 to 12

                card_rank = Rank[random_int ]

                random_suit = random.randint(0, 3) #generating random values from 0 to 4

                card_rank = card_rank + ' ' + suits[random_suit]
                # storing the values from list as per index value generated from random number
                if list_cards.__contains__(card_rank) is False:
                #checks whether the list contains the same value if it contains it will not add
                # or else it will add to the list
                    if len(list_cards) < 37:
                        # add the elements to the list till the list size is 36
                        list_cards.append(card_rank)
                        #adding element to the lsit


        row = 4
        #number of playes 4
        column = 9
        #number of cards for each player 9
        two_d_array = [[0 for j in range(column)] for i in range(row)]  # create blank 2d array
        index = 0
        for i in range(row):
            for j in range(column):
                two_d_array[i][j] = list_cards[index]  # append
                index += 1

        player1 = []
        player2 = []
        player3 = []
        player4 = []

        for i, j, k, l in zip(list_cards[:9], list_cards[9:18], list_cards[18:27], list_cards[27:]):
        #The purpose of zip() is to map the similar index of multiple containers 
        # so that they can be used just using as single entity
            player1.append(i)
            player2.append(j)
            player3.append(k)
            player4.append(l)

        print("Player 1 cards:")
        print(player1)
        print()
        print("Player 2 cards:")
        print(player2)
        print()
        print("Player 3 cards:")
        print(player3)
        print()
        print("Player 4 cards:")
        print(player4)
        print()


if __name__ == "__main__":
    c = Cards()
    c.shuffle()