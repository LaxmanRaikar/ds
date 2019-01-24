from utilities.utility import dequeue
def pal_check(string):
    '''Palindrome checker using Deque'''
    pal_dq = dequeue()
    for character in string:
        pal_dq.add_front(character)
    match = True
    while (pal_dq.size() > 1 and match):
        front = pal_dq.remove_front()
        rear = pal_dq.remove_rear()
        if front != rear:
            match = False
    return match


print(pal_check('radar'))
print(pal_check('abcd'))