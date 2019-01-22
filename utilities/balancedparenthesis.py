from utilities.utility import Stack

def balance_parentheses():
    """
    This method is used as runner balanced_parentheses(string) method
    :return:  nothing
    """
    stack = Stack()
    try:
        string = input("Enter Expression to check for balanced Parentheses: ")
    except Exception as e:
        print(e)
        print("Enter String")

    stack.balanced_parentheses(string)


if __name__ == "__main__":
    balance_parentheses()