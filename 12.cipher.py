import string
checklist = string.ascii_lowercase


def cipher(sentence, mode):
    result = ""
    for i in sentence:
        if i == " ":
#            result += " "
            continue
        if mode == "encode":
            n = len(checklist) - checklist.index(i) - 1
            result += checklist[n]
        elif mode == "decode":
            n = len(checklist) - checklist.index(i) - 1
            result += checklist[n]
    print (result)

mode = "decode"
#cipher("gsvjf rxpyi ldmul cqfnk hlevi gsvoz abwlt", mode)
cipher("the quick brown fox jumps over the lazy dog", mode)