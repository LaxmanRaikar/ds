class Node:
    # This class is used to create Node
    def __init__(self, data, next = None):

        # This is the constructor of Node class

        self.data = data
        self.next = next


class LinkedList:
    # This class is used to create LinkedList

    def __init__(self):
        self.head=None

    def append(self, data):

        # This method is used to append data given by user at the end of the LinkedList

        node = Node(data)  # creation of node
        if self.head is None:
            self.head = node  # if head is null then assign new node to head
        else:
            traverse = self.head
            while traverse.next is not None:  # else traverse pointer till last node and
                traverse = traverse.next  # append new node at end
            traverse.next = node

    def search_item(self, data):

        # This method is used to search data given by user.

        traverse = self.head
        if self.head is None:  # execute if list empty
            return False
        while traverse.next is not None:
            if traverse.data == data:  # checks for matching data
                return True
            traverse = traverse.next
        if traverse.data == data:
            return True  # for single node
        else:
            return False

    def remove(self, data):

        # This method is used to remove data from the Linked list specified by the user

        traverse = self.head
        #  assignments of head
        if self.head is None:
            return None
        if traverse.data == data:
            self.head = traverse.next  # for first node of linked list
            return
        while traverse.next is not None:
            temp = traverse.next
            if temp.data == data:  # matching
                traverse.next = temp.next  # if data match with node then delete
                return
            traverse = traverse.next

    def display(self):

        # This method is used to display content of Linked list.
        # this method return data present in each node of LinkedList
        # and its also useful in HashTable to display each data stored
        # in HashTable data structure

        list = []
        traverse = self.head
        if self.head is None:
            return None  # if empty then return None
        while traverse.next is not None:
            list.append(traverse.data)  # append element in list till linked list not end
            traverse = traverse.next
        list.append(traverse.data)
        return list  # return Linked List

    def file_update(self, data):

        # This method is used to update file after any operation performed on LinkedList
        # and it saves the data into the file.

        file = open("word", "r+")
        file.truncate(0)
        """The method truncate() truncates the file's size. 
        If the optional size argument is present, the file is truncated to (at most) that size."""
        file.close()
        if self.search_item(data) is True:  # search data using search method
            self.remove(data)  # if found then remove

            file = open("word", "a+")
            linkedlist_content = []
            linkedlist_content = self.display()  # assign linked list to a list
            for i in linkedlist_content:
                file.write(i + " ", )  # write data into file
            file.close()
            file = open("word", "r")
            for i in file:
                print(i)  # print file
            file.close()
        else:
            self.append(data)  # if data not found then append data into file
            file = open("word", "a+")
            linkedlist_content = []
            linkedlist_content = self.display()
            for i in linkedlist_content:
                file.write(i + " ")  # write file data into list
            file.close()
            file = open("word", "r")
            for i in file:
                print(i)  # print list contents
            file.close()


class OrderedList(LinkedList):

    # This is used to create OrderedList.

    def __init__(self):
       self.head=None

    def add(self, data):

        # This method is used to put data in OrderedList in increasing order

        node = Node(data)  # create node
        if self.head is None:  # if list is empty
            self.head = node  # assign node to head
        else:
            traverse = self.head
            if int(self.head.data) > int(node.data):  # compare data before adding it
                self.head = node  # for ascending order if head is greater
                node.next = traverse  # than given data then simply add it.
            if int(self.head.data) < int(node.data):  # if head of data less than new node of data
                temp = self.head
                while traverse.next is not None:
                    if traverse.data < node.data:
                        temp = traverse  # check where new node of data is less than
                    traverse = traverse.next  # next one and if condition satisfy then add
                if traverse.data < node.data:
                    temp = traverse
                temp1 = temp.next
                temp.next = node
                node.next = temp1

    def file_update(self, data):

        # This method is used to update file after any operation performed on OrderedList
        # and it saves the data into the file.

        file = open("number", "r+")
        file.truncate(0)
        """The method truncate() truncates the file's size. 
                If the optional size argument is present, the file is truncated to (at most) that size."""
        file.close()
        if self.search_item(data) is True:  # if element found
            self.remove(data)  # remove it using remove()
            file = open("number", "a+")

            orderedlist_content = []
            orderedlist_content = self.display()  # assign data to list return by
            for i in orderedlist_content:  # display()  method
                file.write(i + " ", )  # write data into file
            file.close()
            res = [int(i) for i in orderedlist_content]
            res.sort()  # sort linked list
            print(res)  # print linked list
        else:
            self.add(data)  # if data not found in list then add it
            file = open("number", "a+")
            orderedlist_content = []  # assign data to list return by
            orderedlist_content = self.display()  # display() method
            for i in orderedlist_content:
                file.write(i)  # write data into file
            file.close()
            res = [int(i) for i in orderedlist_content]
            print(res)  # print data of linked list


class Stack:
    top = 0

    def __init__(self):
        self.head=None

    def push(self, data):

        # This method is used to insert data in stack.

        node = Node(data)  # create new node
        if self.head is None:
            self.head = node  # if head is empty then assign new node to head
        else:
            traverse = self.head
            while traverse.next is not None:  # else add to next null position
                traverse = traverse.next
            traverse.next = node

    def size(self):

        # This method is used to find the size of Stack

        traverse = self.head
        if self.head is None:
            return 0
        size = 1
        while traverse.next is not None:  # traverse pointer till last node and
            traverse = traverse.next  # for each node size increment by 1
            size += 1
        return size  # return count of element in the list

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

    def peek(self):

        # This method is used to return the last inserted item in the stack.

        traverse = self.head
        if self.head is None:
            return "empty stack"  # print if stack is empty
        self.top = self.size() - 1
        for i in range(0, self.top):
            traverse = traverse.next  # traverse pointer till last node
        return traverse.data  # return last node which is top element

    def is_empty(self):

        # This method is used to know whetHer stack is empty or not

        if self.size() == 0:
            return True
        else:
            return False

    def show(self):  # display stack
        traverse = self.head

        if self.top <= -1:  # initially starting node is -1 then stack is underflow
            print(" Stack Underflow")
            return
        if traverse == None:
            print("Stack is empty")  # empty stack
            return

        while traverse.next != None:
            print(traverse.data)
            traverse = traverse.next

        # print(traverse.data)
        return traverse.data

    def balanced_parentheses(self, string):

        # This method is used to check whether expression is balanced or not.

        for i in string:
            if i == '(' or i == '[' or i == '{':
                stack.push(i)  # adding element into stack
            if ((stack.peek() == '(' and i == ')') or (stack.peek() == '[' and i == ']') or (
                    stack.peek() == '{' and i == '}')) and stack.size() > 0:
                stack.pop()
                continue

        if stack.size() == 0:
            print("Balanced Parenthesis ")  # after push and pop operation if stack size
        else:  # is zero then balanced otherwise unbalanced
            print("Parenthesis is not Balanced ")


stack = Stack()


class Queue:

    # This Queue class is used to create Queue.
    front=None
    rear=None

    def __init__(self):
        pass



    def enqueue(self, data):

        # This method is used to insert data in the Queue .
        # data will be given by user which data to be inserted ,
        # queue follows First in First Out Principle.

        node = Node(data)

        if self.front is None and self.rear is None:

            self.front = node       # front and rear assign to new node
            self.rear = node

        else:

            self.rear.next = node        # else add element in queue by rear
            self.rear = self.rear.next

    def show(self):

        # This method is used to display content of queue .

        if self.front is None:
            print("Queue is empty")     # print if queue is empty
            return

        while self.front.next is not None:
            print(self.front.data)          # print queue data
            self.front = self.front.next

        print(self.front.data)

    def dequeue(self):

        # This method is used to delete data from the Queue.
        # data will deleted according to FIFO principle

        temp = self.front
        self.front = self.front       # delete data which is pointed by front pointer
        return temp.data                # return deleted data

    def is_empty(self):

        # This method is used to know whether Queue is empty or not.

        if self.front is None:
            return True
        else:
            return False

    def size(self):

        # This method is used to display content of queue.

        size = 1
        traverse = self.front
        if self.front is None:      # return 0 if queue is empty
            return 0

        while traverse.next is not None:
            traverse = traverse.next        # traverse till last element and count size
            size += 1
        return size


class que():
    def __init__(self):
        self.list = []

    def queue(self, data):
        """"this method is used to insert data into the list"""
        self.list.insert(0, data)

    def peek(self):
        """this method is used to show the value which is present at first"""
        return self.list[0]

    def dequeue(self):
        """this method is used to remove the value which was pushed first"""
        return self.list.pop()

    def size(self):
        """this method gives the size of the list"""
        return len(self.list)

    def show(self):
        """"this method will print the values of list"""
        for i in self.list:
            print(self.list[i])


class dequeue:
    def __init__(self, front=None, rear=None):
        self.front = front
        self.rear = rear

    def add_front(self, data):
        node = Node(data)
        if self.front is None and self.rear is None:
            self.front = node
        else:
            node.next = self.front
            self.front = node

    def add_rear(self, data):
        node = Node(data)
        if self.front is None and self.rear is None:
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def remove_front(self):
        if self.front.next is None:
            temp = self.front
            self.front = None  # if only one element in queue
            return temp.data

        temp = self.front
        self.front = self.front.next  # delete element of queue which is on front
        return temp.data

    def remove_rear(self):
        # This is used to remove data which is at rear position in deque.

        traverse = self.front
        if self.rear == self.front:
            self.rear = None  # if queue contains only one element
            self.front = None
            return traverse.data

        while traverse.next != self.rear:
            traverse = traverse.next  # go till second last position

        rear_value = self.rear
        self.rear = traverse  # delete last element
        traverse.next = None
        return rear_value.data

    def is_empty(self):

        # This method is used to know whether Deque is empty or not.
        # return this will return True if Deque is empty or else  return False.

        if self.front is None:
            return True
        else:
            return False

    def size(self):

        # This method is used to calculate size of Deque
        # return this will return size of Deque
        size = 1
        traverse = self.front

        if self.front == None:
            return 0
        while traverse.next != None:  # traverse till last element
            traverse = traverse.next
            size += 1
        return size


class calenarray:

    def calender(self, m, y):
        day = ['S', ' M', ' T', ' W', ' Th', 'F', ' S']
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        values = 1
        d = 1

        y0 = y - (14 - m) // 12
        x = y0 + y0 // 4 - y0 // 100 + y0 // 400
        m0 = m + 12 * ((14 - m) // 12) - 2
        d0 = (d + x + 31 * m0 // 12) % 7

        if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:  # check leap year
            days[1] = 29
        row = 6
        column = 7
        two_d_array = [[0 for j in range(column)] for i in range(row)]  # create empty 2d array
        print('Your Calender is\n')
        for i in range(0, 7):
            print(day[i], end=' ')  # print day's for calender
        print()
        for i in range(row):
            for j in range(column):
                if values <= days[m - 1]:
                    if i == 0 and j < d0:  # while d0 is less than j
                        two_d_array[i][j] = ' '  # it will print blank space
                        continue
                    two_d_array[i][j] = values  # add days into calender
                    values += 1  # increment counter"""
        for i in range(row):
            for j in range(column):
                if two_d_array[i][j] != 0:
                    x = two_d_array[i][j]  # ljust() method returns the string
                    x1 = str(x).ljust(2)  # left justified in a string of length width.
                    print(x1, end=" ")
            print()


class calen_queue:

    def calender(self, m, y):
        day = ['S', ' M', ' T', ' W', ' T', ' F', ' S']
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        values = 1
        d = 1
        b="0"

        y0 = y - (14 - m) // 12
        x = y0 + y0 // 4 - y0 // 100 + y0 // 400
        m0 = m + 12 * ((14 - m) // 12) - 2
        d0 = (d + x + 31 * m0 // 12) % 7
        if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:  # check leap year
            days[1] = 29
        row = 6
        column = 7
        two_d_array = [[0 for j in range(column)] for i in range(row)]
        print("your calender is\n")
        for i in range(row + 1):
            print(day[i], end=" ")
        print()
        for i in range(row):
            for j in range(column):
                if values <= days[m - 1]:
                    if i == 0 and j < d0:
                        Queue.enqueue(' ')
                        continue
                    else:
                        Queue.enqueue(values)
                    values += 1
        for i in range(row):
            for j in range(column):
                if Queue.size() > 0:
                    x = Queue.dequeue()  # remove element from queue and store it in x variable
                    x1 = str(x).ljust(2)  # using ljust() method print formatted calender
                    print(x1, end=" ")
            print()


class bintree:

    def search_tree(self, list):
        number_list = []  # empty list to add the values
        for n in list:
            fact1 = 1
            for l in range(1, (2 * n) + 1):
                fact1 = fact1 * l
            fact2 = 1
            num = n + 1
            for m in range(1, num + 1):
                fact2 = fact2 * m
            fact3 = 1
            for k in range(1, n + 1):
                fact3 = fact3 * k

            number_list.append((fact1 // (fact2 * fact3)) % 100000007)
        return number_list


class Deq:

    def __init__(self):
        # constructor
        self.items = []

    def add_front(self, item):
        # this method adds the value from front
        self.items.append(item)

    def add_rear(self, item):
        # this method adds the value from the rear
        self.items.insert(0, item)

    def remove_front(self):
        # this method removes values from front
        return self.items.pop()

    def remove_rear(self):
        # this method removes value from rear
        return self.items.pop(0)

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)
