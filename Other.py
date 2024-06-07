def encode_decode(words, coding):
    nwords = []
    for word in words:
        if len(word) >= 3:
            if coding:
                r1 = "dchsducsuid"
                r2 = "djcbsdbcuss"
                stnew = r1 + word[1:] + word[0] + r2
                nwords.append(stnew)
            else:
                stnew = word[3:-3]
                stnew = stnew[-1] + stnew[:-1]
                nwords.append(stnew)
        else:
            nwords.append(word)
    return " ".join(nwords)

while True:
    code = input("Enter a Code: ")
    words = code.split(" ")
    coding = input("1 for Coding or 2 for Decoding: ")
    if coding == "1":
        coding = True
    elif coding == "2":
        coding = False
    else:
        print("Invalid input. Please enter either 1 for Coding or 2 for Decoding.")
        continue
    print(encode_decode(words, coding))