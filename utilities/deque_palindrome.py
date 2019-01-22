from utilities.utility import dequeue
def palindrome_checker():
    """
    This method is used to check for palindrome .
    return this will return True if string is palindrome else return False
    """
    deque = dequeue()
    try:
        string = input("Enter String to Check for Palindrome: ")
    except Exception as e:
        print(e)
    lower_string = string.lower()
    string = lower_string

    remove_space = ''
    for i in range(0, len(string)):
        if string[i] == ' ':
            continue

        remove_space += string[i]

    string = remove_space

    for i in string:
        deque.add_rear(i)
    reverse_string = ''
    for i in range(0, deque.size()):
        reverse_string += str(deque.remove_rear())

    if string == reverse_string:
        return True
    else:
        return False


if __name__ == "__main__":
    print(palindrome_checker())