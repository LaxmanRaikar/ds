from utilities import abc


def anagram2darray():
    prime_list = abc.prime()                               #calling method to get the prime numbers
    anagram_list = abc.prime_anagram(prime_list)           #calling method to get anagram prime numbers
    not_anagram = []                                       #empty list to store the values
    row = 10
    column = 25                                     #initialization
    two_d_array = [[0 for j in range(column)] for i in range(row)]         #create 2d array
    k = 0
    index = 0
    print("result:")
    for i in prime_list:
        if anagram_list.__contains__(i) is not True:        #comparing elements in prime and anagram list
            not_anagram.append(i)

    for i in range(row):
        for j in range(column):
            if k<len(anagram_list):
                two_d_array[i][j]=anagram_list[k]           #add values to the array
                k+=1                                        #incrementing

            if k>=len(anagram_list) and index<len(not_anagram):
                two_d_array[i][j]=not_anagram[index]
                k+=1
                index+=1
    for i in range(row):                                    #to print in 2d array format
        for j in range(column):
            if two_d_array[i][j]!=0:
                print(two_d_array[i][j],end=" ")
        print()





anagram2darray()
