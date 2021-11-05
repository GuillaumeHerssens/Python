import math
# sum of all the multiple of any number until n (for fun)
def multiplesum(n):
 for i in range(1,n):
    result = 0
    for j in range(math.ceil(n / i)):
        result += (j * i)
    print ("sum of all multiple of %d up to %d : %d" % (i, (n - 1), result))
# sum of the all the multiple of given m until n
def multiplesum_of_m(n,m):
    result = 0
    for i in range(math.ceil(n / m)):
        result += (i * m)
    print ("sum of all multiple of %d up to %d : %d" % (m, (n - 1), result))

n = 10
m = 2
multiplesum(n)
multiplesum_of_m(n,m)