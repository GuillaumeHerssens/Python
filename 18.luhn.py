def luhn(n):
    l = str(n).replace(" ", "")
    sum = 0
    for i in range(len(l)):
        if ((i % 2) == 0):
            m = (int(l[i]) * 2)
            if m > 9:
                m -= 9
            l = l[:i] + (str(m)) + l[i+1:]

    for i in range(len(l)):
        sum += int(l[i])
    
    if (sum % 10) == 0:
        print ("Your number %s is valid." % (n))
    else:
        correction = 10 - (sum % 10)
        if (len(n) % 2) == 0:
            if (correction % 2) == 1:
                correction = int((correction + 9) / 2)
            else:
                correction = int(correction / 2)
        corrected = n + str(correction)

        print ("Your number %s is invalid." % (n))
        print ("Number : %s should be valid." % (corrected))

n = "2323 2005 7766 3554"
luhn(n)