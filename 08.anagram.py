def anagram(word):
    alist = ["enlists", "google", "inlets", "banana"]
    for i in word:
        for j in alist:
            if (i in j) and word.count(i) == j.count(i):
                continue
            else:
                alist.remove(j)
                print (j + " is not an anagram of " + word)
    if alist:
        print (*alist, " is an anagram of " + word)

word = "listen"
anagram(word)