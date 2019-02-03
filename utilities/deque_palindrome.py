"""Palindrome Checker Program
This program is used to check for palindrome.
here user can give their string to know whether
given string is palindrome or not
Example:
    Enter String to Check for Palindrome :: madam
    True
Author:Laxman Raikar
Since:16 jan,2019
"""
from utilities.utility import Deq


def pal_check(string):
    try:
        '''Palindrome checker using Deque'''
        pal_dq = Deq()  # creating the object of class
        for character in string:
            pal_dq.add_front(character)
        match = True
        while pal_dq.size() > 1 and match:
            front = pal_dq.remove_front() # eliminating  one element from front
            rear = pal_dq.remove_rear()     # eliminating one element from rare
            if front != rear:               # if front and rear element is not equal than it will return false
                match = False
        return match
    except  ValueError:
        print(ValueError)


string_to_check_palindrome = input("enter the string to check the palindrome :")

print(pal_check(string_to_check_palindrome))
