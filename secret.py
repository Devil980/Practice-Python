import string
import random
code = input("Enter a code that is more then 3 letters for coding or decoding: ")

choice = int(input("1 for coding and 0 for decoding: "))
# print (True) if choice == 1 else print (False)
if choice == 1:
    if len(code)>=3:
        new_code = code[::-1]
        def hidden_code(length=14):
            character = string.ascii_letters
            code = "".join(random.choice(character) for _ in range(length))
            return code
        r1 = hidden_code()
        r2 = hidden_code()
        hide = r1 + new_code + r2
        print(hide)
    elif len(code)<3:
        print("enter code more then 3 words")
elif choice == 0:
    print("welcome to decoding")
    if len(code)>=3:
        dcode = code[::-1]
        word = dcode[14:-14]
        print (word)