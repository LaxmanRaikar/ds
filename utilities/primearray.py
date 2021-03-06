"""Prime Number stored in 2D array Program
This program is used to store prime numbers in two dimensional array.
Example:
    Like here prime number within 100 range will be stored in one dimension
    and next prime number within 100 to 200 range will be stored in  second dimension
    and so on.
Author:Laxman Raikar
Since:
    16 JAN,2019
"""


def prime():
    arr = []
    for i in range(1,1001):
        for j in range(2, i - 1):
            if i % j == 0:
                break
        else:
                arr.append(i)
    return arr


def prime_number_2d_array():
    prime_list = prime()  # get prime number
    row = 10
    column = 25
    limit = 100
    # create empty 2d array
    two_d_array = [[0 for j in range(column)] for i in range(row)]
    k = 0
    for i in range(row):
        for j in range(column):
            if k < len(prime_list):
                if prime_list[k] <= limit:  # prime number check with the limit
                    two_d_array[i][j] = prime_list[k]  # add number into array
                    k += 1
        limit += 100  # increment limit by 100 for each iteration
    for i in range(row):
        for j in range(column):
            if two_d_array[i][j] != 0:
                print(two_d_array[i][j], end=" ")  # display elements in 2d array format
        print()


if __name__=="__main__":
    prime_number_2d_array()
