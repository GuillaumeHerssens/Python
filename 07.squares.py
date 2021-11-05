def squares(n):
    squaresum = sumsquare = 0
    for i in range(1, n+1):
        squaresum += i
        sumsquare += (i ** 2)

    print ((squaresum **2) - sumsquare)
    
n = 10
squares(n)