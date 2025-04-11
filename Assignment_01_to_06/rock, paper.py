import random

print("Welcome to the Rock, Paper, Scissors game!")

choices = ["rock", "paper", "scissor"]

user_score = 0
computer_score = 0

print("Let's Play!")

while True:
    user_input = input("Type Rock, Paper or Scissor or Q to quit: ").lower()

    if user_input == "q":
        print(f"\nFinal Score - You: {user_score}, Computer: {computer_score}")
        print("Thanks for playing!")
        break

    if user_input not in choices:
        print("Invalid input. Please try again.")
        continue

    computer_chose = random.choice(choices)
    print(f"Computer chose {computer_chose}.")

    if user_input == computer_chose:
        print("It's a tie!")
    elif (user_input == "rock" and computer_chose == "scissor") or \
         (user_input == "paper" and computer_chose == "rock") or \
         (user_input == "scissor" and computer_chose == "paper"):
        print("You win!")
        user_score += 1
    else:
        print("Computer wins!")
        computer_score += 1
