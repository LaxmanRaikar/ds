""" this program is used to distribute the deck of cards to four players using queue
@ author : Laxman Raikar
Since:28 JAN,2019"""
import random
from utilities.utility import Queue
import numpy as np
q = Queue()


class Cards:

    def shuffle(self):
        suits = ["C", "D", "H", "S"]  # for (Clubs Diamonds Hearts Spades)
        Rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]  # for 13 cards (2-10 and face cards)

        list_cards = []  # for taking

        while len(list_cards) < 37:
            card_rank = " "
            random_int = random.randint(0, 12)  # generating random values from 0 to 12

            card_rank = Rank[random_int]

            random_suit = random.randint(0, 3)  # generating random values from 0 to 4

            card_rank = card_rank + ' ' + suits[random_suit]
            # storing the values from list as per index value generated from random number
            if list_cards.__contains__(card_rank) is False:

                # checks whether the list contains the same value if it contains it will not add
                #  or else it will add to the list
                if len(list_cards) < 37:
                    # add the elements to the list till the list size is 36
                    list_cards.append(card_rank)
                    # adding element to the list

        row = 4
        column = 9
        two_d_array = [[0 for j in range(column)] for i in range(row)]
        index = 0
        for i in range(row):

            for j in range(column):
                two_d_array[i][j] = list_cards[index]
                index += 1

        a = np.array(two_d_array)
        print(a)
        limit = 9
        player1 = []
        player2 = []
        player3 = []
        player4 = []
        for i in list_cards[0:9]:
            player1.append(i)
        player1.sort()
        print()
        print("Queue data")
        print()
        print("Player 1 Cards")

        for j in player1:
            q.enqueue(j)  # adding to the queue
        q.show()          # printing from queue
        print()
        for i in list_cards[9:18]:

            player2.append(i)
        player2.sort()
        print("Player 2 Cards")
        for l in player2:
            q.enqueue(l)        # adding to the queue
        q.show()                # printing from queue
        print()
        for i in list_cards[18:27]:
            player3.append(i)
        player3.sort()
        print("Player 3 Cards")
        for m in player3:
            q.enqueue(m)        # adding to the queue
        q.show()                # printing from queue
        print()
        for i in list_cards[27:]:
            player4.append(i)
        player4.sort()
        print("Player 4 Cards")
        for n in player4:
            q.enqueue(n)        # adding to the queue
        q.show()                # printing from queue


def deck_of_card():
    p = Cards()
    p.shuffle()


if __name__ == "__main__":
    deck_of_card()