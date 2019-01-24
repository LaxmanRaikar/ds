from utilities.utility import stack
from utilities import abc
s=stack()
prime_list = abc.prime()
anagram_list = abc.prime_anagram(prime_list)
s.queue(anagram_list)
print(s.dequeue())