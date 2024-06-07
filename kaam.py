import turtle
import random
import string
def game():
    screen = turtle.Screen()
    screen.bgcolor("Black")
    screen.title("Welcome to coding or decoding")
    
    code = turtle.textinput("Input box","Enter a code that is more then 3 letters for coding or decoding: ")
    if len(code)<3:
        print("Enter valid number of code")
    choice = int(turtle.textinput("Input box","1 for coding and 0 for decoding:"))
    if choice==1:
        new_code = code[::-1]
        def hidden_code(length=14):
            characters = string.ascii_letters
            code = "".join(random.choice(characters) for _ in range(length))
            return code
        r1 = hidden_code()
        r2 = hidden_code()
        hide = r1 + new_code + r2
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(-100,0)
        t.color("White")
        t.write("Encoded Message:", align="left", font=("Arial", 16, "normal"))
        t.goto(-100, -30)
        t.write(hide, align="left", font=("Arial", 16, "normal"))
        print(hide)
    elif choice==0:
        dcode = code[::-1]
        word = dcode[14:-14]
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(-100,0)
        t.color("White")
        t.write("Decoded Message:", align="left", font=("Arial", 16, "normal"))
        t.goto(-100, -30)
        t.write(word, font=("Arial", 16, "normal"))
        print(word)
    turtle.done()
game()