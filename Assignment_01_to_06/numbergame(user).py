import random

print("Welcome to the number guessing game!")

secret_number = random.randint(1, 10)
print("I have secret a number between 1 and 10. Can you guess it?")

while True:
    try:
        guess = int(input("Enter your guess: "))
        if guess > secret_number:
            print("Too high! Try again")

        elif guess < secret_number:
            print("Too low! Try again")
        else:
            print("Congratulation! You guessed the number!")
            break
    except ValueError:
        print("Inavalid input please enter a number between 1 and 10")

           
