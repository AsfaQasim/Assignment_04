import random

print("Welcome to the number guessing game...")

low = 1
high = 10

print("Think of a number between 1 to 10 and the computer will try to guess it!")

while low <= high:
    guess = random.randint(low, high)
    print(f"Computer's guess is: {guess}")

    feedback = input("Is the guess too High (H), too Low (L), or Correct (C)?:  ").upper()

    if feedback == "C":
        print("Yay! The computer guessed your number correctly!")
        break
    elif feedback == "H":
        high = guess - 1
    elif feedback == "L":
        low = guess + 1
    else:
        print("Invalid input. Please enter H, L, or C.")

if low > high:
    print("Hmm, something went wrong. Are you sure you gave correct hints?")
