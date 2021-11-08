def to_letters(n):
    power = ["S", "D", "SH","ST","D","SH","SM","D","SH","SB","D","SH"]
    transform = { "1D0S" : " ten", "1D1S" : " eleven", "1D2S" : " twelve", "1D3S" : " thirteen", "1D4S" : " fourteen", "1D5S" : " fifteen", "1D6S" : " sixteen", "1D7S" : " seventeen", "1D8S" : " eighteen", "1D9S" : " nineteen", "1S" : " one", "2S" : " two", "3S" : " three", "4S" : " four", "5S" : " five", "6S" : " six", "7S" : " seven", "8S" : " eight", "9S" : " nine","2D" : " twenty-","3D" : " thirty-","4D" : " forty-","5D" : " fifty-","6D" : " sixty-","7D" : " seventy-","8D" : " eighty-","9D" : " ninety-", "H" : "-hundred","T" : "-thousand","M" : "-million","B" : "-billion",}
    letters = ""
    
    for j in range(len(n)):
        if n[(-j-1)] == "0":
            continue
        letters = n[(-j-1)] + power[j] + letters
    for o, r in transform.items():
        letters = letters.replace(o, r).replace("- ", "-").replace("--", "-")
    print(letters)

n = 2519
to_letters(str(n))
