import string
checklist = string.ascii_lowercase

def cipher(sentence):
    result = ""
    for i in sentence:
        if i == " ":
            continue
        n = len(checklist) - checklist.index(i) - 1
        result += checklist[n]
    print (result)

encode = "the quick brown fox jumps over the lazy dog"
decode = "gsvjf rxpyi ldmul cqfnk hlevi gsvoz abwlt"
cipher(encode)
cipher(decode)
