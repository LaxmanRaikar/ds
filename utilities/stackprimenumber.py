"""Prime Numbers that are Anagram in the Range of 0 ­ 1000 in a Stack using
the Linked List
author: Laxman Raikar
Since:16 JAN,2019
"""
from utilities import abc

class Node:
    def __init__(self, data, next=None):

        # This is the constructor of Node class

        self.data = data
        self.next = next


class linked_list:
    def __init__(self):
        self.head=None

    def add(self,data):
        node = Node(data)           # creation of node
        if self.head is None:
            self.head = node        # if head is null then assign new node to head
        else:
            traverse = self.head
            while traverse.next is not None:        # else traverse pointer till last node and
                traverse = traverse.next            # append new node at end
            traverse.next = node

    def dis(self):
        list = []
        traverse = self.head
        if self.head is None:
            return None  # if empty then return None
        while traverse.next is not None:
            list.append(traverse.data)  # append element in list till linked list not end
            traverse = traverse.next

        return list  # return Linked List

    def pop(self):

        # This method is used to delete last data which is inserted into the stack.
        # actually stack follow the Last in First Out order to pop the data from the stack

        traverse = self.head
        if self.head is None:  # if stack empty return -1
            return -1
        if self.head.next is None:
            self.head = None  # if only one element in stack then
            return traverse.data  # set head as none and delete that element and return data
        while traverse.next is not None:
            t1 = traverse.next
            if t1.next is None:  # else delete last node which is top on the stack
                traverse.next = None
                return t1.data
            traverse = traverse.next


a = linked_list()


def printlink():
    prime_list = abc.prime()
    anagram_list = abc.prime_anagram(prime_list)                # getting anagram prime number list
    arr2=[]

    for i in anagram_list:                      # loop to print the prime number values
        a.add(i)
    e=a.dis()
    print("prime anagram numbers:",e)

    for j in anagram_list:                  # loop to print in reverse order
        m=a.pop()
        arr2.append(m)
    print("reversed order:",arr2)



if __name__=="__main__":
    printlink()