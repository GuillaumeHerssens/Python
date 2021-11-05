def serie(m, n):
    if n > len(m):
        print ("Invalid length")
    else:               
        for i in range(len(m)):
            if len(m[i:i+n]) == n:
                print (m[i:i+n])
m = 49142
n = 3
serie(str(m), n)