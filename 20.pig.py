def latin(sentence):
    piglatin = ""
    vowels = ["a","e","i","o","u"]
    for i in sentence.split():
        for j in i:
            if j in vowels:
                piglatin += i + "ay "
                break
            else:                
                i = i[1:] + i[0]
    print (piglatin)

sentence = "the quick brown fox jumps over the lazy dog"
latin(sentence)
