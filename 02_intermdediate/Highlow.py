import random

rounds = 5

def main():
    print("Welcome to the high low game!")
    print("*****************************")

    your_score = 0  

    for i in range(rounds):
        print("Round", i + 1)

        computer_number = random.randint(1, 100)
        your_number = random.randint(1, 100)
        print("Your number is", your_number)
        choice = input("Do you think your number is higher or lower than the computer's number? (higher/lower): ").lower()

        higher_and_correct = choice == "higher" and your_number > computer_number
        lower_and_correct = choice == "lower" and your_number < computer_number

        if higher_and_correct or lower_and_correct:
            print("You were right! The computer's number was", computer_number)
            your_score += 1 
        else:
            print("That's incorrect! The computer's number was", computer_number)

        print("Your score is now", your_score)
        print()

    print("Thanks for playing!")

if __name__ == "__main__":
    main()
