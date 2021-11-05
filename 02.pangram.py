import string
checklist = string.ascii_lowercase
punctuation = string.punctuation + string.whitespace

def pangram(sentence):
    
    for x in punctuation:
        sentence = (sentence.replace(x, "").lower())

    for i in checklist:
        if i in sentence:
            if i == "z":
                print ("The sentence is a pangram")
            continue
        else:
            print ("The sentence is not a pangram")
            break

        



pangram("The ,quick; brown,fox jumps ,over the %%%%lazy (dog).")