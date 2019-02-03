"""Balanced Parentheses Program
This program is used to check whether user given arithmetic expression is balanced or not
Example:
    Balanced Expression :: {{a+b}*[a-b]}
    Unbalanced Expression:: {{a+b}*[a-b]
Author:Laxman Raikar
Since:
    16 JAN,2019
"""


from utilities.utility import Stack


def balance_parentheses():
    """
    This method is used as runner balanced_parentheses(string) method
    """
    stack = Stack()
    try:
        string = input("Enter Expression to check for balanced Parentheses: ")
    except ValueError:
        print("Enter String")

    stack.balanced_parentheses(string)


if __name__ == "__main__":
    balance_parentheses()