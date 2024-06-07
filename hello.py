import random
import tkinter as tk


def get_computer_choice():
    """ Returns a random choice ("rock","paper","scissor" for the computer.)"""
    possible_choice = ["rock","paper","scissor"]
    return random.choice(possible_choice)

def get_winner(user_choice,computer_choice):
    """Returns the winner of the game (user or computer) or a tie."""
    if (user_choice == computer_choice):
        return "Tie"
    elif (user_choice == "rock" and computer_choice == "scissor") or\
    (user_choice == "paper" and computer_choice == "rock") or\
    (user_choice == "scissor" and computer_choice == "paper"):
        return "user"
    else:
        return "computer"

def on_button_click(choice):
    computer_choice = get_computer_choice()
    result = get_winner(choice, computer_choice)

    if result == "Tie":
        label_result.config(text="It is a Tie")
    elif result == "user":
        label_result.config(text="Congratulations! You have won")
    elif result == "computer":
        label_result.config(text="Computer has won")

    image_computer_choice = get_image(computer_choice)
    image_computer_choice.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

def on_quit_button_click():
    root.destroy()

def get_image(choice):
    if choice == "rock":
        return tk.PhotoImage(file="rock.png")
    elif choice == "paper":
        return tk.PhotoImage(file="paper.png")
    else:
        return tk.PhotoImage(file="scissor.png")

root = tk.Tk()
root.title("Rock, Paper, Scissors")
root.geometry("500x400+300+200")
root.configure(bg="#F0F0F0")

# Create Buttons for rock, paper, and scissors
button_rock = tk.Button(root, text="rock", command=lambda: on_button_click("rock"), font=("Helvetica", 16), bg="#F0F0F0", bd=0, activebackground="#E0E0E0")
button_rock.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

button_paper = tk.Button(root, text="paper", command=lambda: on_button_click("paper"), font=("Helvetica", 16), bg="#F0F0F0", bd=0, activebackground="#E0E0E0")
button_paper.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

button_scissor = tk.Button(root, text="scissor", command=lambda: on_button_click("scissor"), font=("Helvetica", 16), bg="#F0F0F0", bd=0, activebackground="#E0E0E0")
button_scissor.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

# Create Quit Button
quit_button = tk.Button(root, text="Quit", command=on_quit_button_click, font=("Helvetica", 16), bg="#F0F0F0", bd=0, activebackground="#E0E0E0")
quit_button.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

# Create Result Label
label_result = tk.Label(root, text="", font=("Helvetica", 16))