import math

# sum of all the multiple until n
def multiplesum(n):
 for i in range(1,n):
    result = 0
    x = 1
    while (i * x) < n:
        result += (i * x)
        x += 1
    if result == 0:
        break
    else:
        print ("sum of all multiple of %d up to %d : %d" % (i, (n - 1), result))

# sum of the multiple of given m until n
def multiplesum_of_m(n,m):
    result = 0
    for i in range (1,n):
        if (i * m) < n:
            result += (i * m)
    print ("sum of all multiple of %d up to %d : %d" % (m, (n - 1), result))

n = 10
m = 2
multiplesum(n)
multiplesum_of_m(n,m)