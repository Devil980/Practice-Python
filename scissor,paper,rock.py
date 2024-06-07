import random

def get_computer_choice():
    """ Returns a random choice ("rock","paper","scissor" for the computer.)"""
    possible_choice = ["rock","paper","scissor"]
    return random.choice(possible_choice)
# print(get_computer_choice())

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
    
def main():
    """Plays a game of rock,paper and scissor with the user."""
    print("Welcome to the game of rock,paper and scissor")
    while True:
        # name = input("Enter Your Name: ")
        user_choice = input("Write [rock,paper,scissor] or quit to exit the game: ").lower()
        if user_choice == "quit":
            print(f"Thanks for Playing! ")
            break
        if user_choice not in ["rock","paper","scissor"]:
            print("Invalid Input Try Again")
            continue 
        else:
            computer_choice = get_computer_choice()
            print("Computer Choice is: ",computer_choice)

            winner = get_winner(user_choice,computer_choice)
            if winner == "Tie":
                print("It is a Tie")
            elif winner == "user":
                print(f"Congratulation You have won")
            elif winner == "computer":
                print("Computer has won")  

if __name__ == "__main__":
    main()
   
    
       