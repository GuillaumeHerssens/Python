def encoding(string):
    temp = string[0]
    count = 1
    code = ""
    for j, i in enumerate(string):
        if (i == temp) and ((j+1) != len(string)):
            count += 1
            continue
        else:
            if count == 1:
                count = ""
            code += str(count) + temp
            temp = i
            count = 1
    print (code)


text = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"
encoding(text)