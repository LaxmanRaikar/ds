for i in range(1001):
    for j in range(2,i-1):
        if i%j==0: break
    else:
        print (i)
