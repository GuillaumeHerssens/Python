import string
checklist = string.ascii_lowercase

def pangram(sentence):
    sentence2 = (sentence.replace(" ", "")).lower()
    check = True
    for i in range(len(checklist)):
        if checklist[i] in sentence2:
            continue
        else:
            print ("The sentence is not a pangram")
            check = False
            break

    if check == True:
        print ("The sentence is a pangram")



pangram("The quick brown fox jumps over the lazy dog")