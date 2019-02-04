"""
This program is used to generate number of possible binary search tree in
given number of test cases.
Author:Laxman Raikar
Since:16 JAN,2019
"""


from utilities.utility import bintree


def searching():
    try:
        bin = bintree()  # creating object of the class
        nodes_list = []  # empty list to store the input values
        nodes = int(input("enter number of nodes to insert :"))
        print("now enter all the test cases")
        for i in range(nodes):
            nodes_list.append(int(input("Enter :")))  # adding input values to list
        result = bin.search_tree(nodes_list)  # calling the method and executing it and storing the values in result
        for j in result:
            print(j)
    except ValueError:
        print("enter the decimals")


if __name__=="__main__":
    searching()



