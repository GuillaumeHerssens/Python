def wordcount(sentence):
    sentence2 = list(dict.fromkeys(sentence.split(" ")))
    for i in sentence2:
        print ("%s :" % i, sentence.count(i))



wordcount("olly olly in come free")