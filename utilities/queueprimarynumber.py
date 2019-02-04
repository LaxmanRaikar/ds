"""Prime Anagram using Queue Program
This program is used to find prime anagram within 0  to 1000 range and print through queue
Author:Laxman Raikar
Since:
    16 JAN,2019
"""

from utilities.utility import que
from utilities import abc
s = que()   # creating object of class

def prime_que():
    prime_list = abc.prime()  # storing the prime numbers
    anagram_list = abc.prime_anagram(prime_list)        # storing the anagram prime numbers
    s.queue(anagram_list)
    print(s.dequeue())


if __name__=="__main__":
    prime_que()
