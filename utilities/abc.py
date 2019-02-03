def prime_anagram(res):
    arr2 = []  # empty list to store the anagram elements
    for i in range(len(res)):  # outer loop
        for j in range(i + 1, len(res), 1):  # innerloop
            if sorted(res[i]) == sorted(res[j]):
                arr2.append(res[i])  # adding the anagram element to list
                arr2.append(res[j])  # adding the anagram element to list
            else:
                pass
    return arr2


# -----------------------------------------------------------------------------------------
def prime():
    arr = []
    prime_string = []
    for i in range(2,1001):
        for j in range(2, i - 1):
            if i % j == 0:
               break
        else:

            arr.append(i)
    prime_string= [str(i) for i in arr]
    return prime_string
