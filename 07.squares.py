def squares(n):
    squaresum = 0
    sumsquare = 0
    for i in range(1, n+1):
        squaresum += i
        sumsquare += (i ** 2)

    print ((squaresum **2) - sumsquare)

squares(10)