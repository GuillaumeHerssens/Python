import string
az = string.ascii_lowercase

def transform(one,two,three,four,five,eight,ten):
    scrabble = {}
    old_scrabble = [one,two,three,four,five,eight,ten]
    for i in az:
        #scrabble.append(i)
        for j in old_scrabble:
            if i.upper() in j:
                score = old_scrabble.index(j) + 1
                if score == 6:
                    score = 7
                elif score == 7:
                    score = 10
        scrabble[i] = score
    print (scrabble)



one = ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T",]
two = ["D", "G",]
three = ["B", "C", "M", "P",]
four = ["F", "H", "V", "W", "Y",]
five = ["K",]
eight = ["J", "X",]
ten = ["Q", "Z",]
transform(one,two,three,four,five,eight,ten)