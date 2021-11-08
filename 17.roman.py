def to_roman(n):
    power = ["I","X","C","M"]
    intermediate = ["V","L","D"]
    roman = ""

    if int(n) > 3999:
        print("Sorry, roman numerals don't go that far")
    else:
        for i in range(len(n)):
            if int(n[-i-1]) < 4:
                roman = power[i]*int(n[-i-1]) + roman
            elif int(n[-i-1]) < 5:
                roman = (power[i]*1)+(intermediate[i]) + roman
            elif int(n[-i-1]) == 5:
                roman = intermediate[i] + roman
            elif int(n[-i-1]) > 5 and int(n[-i-1]) < 9:
                roman = (intermediate[i])+(power[i]*(int(n[-i-1])-5)) + roman
            elif int(n[-i-1]) > 8:
                roman = (power[i]*1)+(power[i+1]) + roman
        print (roman)
n = 3999
to_roman(str(n))
