from utilities import abc


def anagram2darray():
    prime_list = abc.prime()
    anagram_list = abc.prime_anagram(prime_list)
    not_anagram = []
    row = 10
    column = 25
    two_d_array = [[0 for j in range(column)] for i in range(row)]
    k = 0
    index = 0
    print("result:")
    for i in prime_list:
        if anagram_list.__contains__(i) is not True:
            not_anagram.append(i)

    for i in range(row):
        for j in range(column):
            if k<len(anagram_list):
                two_d_array[i][j]=anagram_list[k]
                k+=1

            if k>=len(anagram_list) and index<len(not_anagram):
                two_d_array[i][j]=not_anagram[index]
                k+=1
                index+=1
    for i in range(row):
        for j in range(column):
            if two_d_array[i][j]!=0:
                print(two_d_array[i][j],end=" ")
        print()





anagram2darray()
