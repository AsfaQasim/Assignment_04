import random

def main():
    secret_number = random.randint(1, 100)
    print("I am thinking of a number between 1 and 100....")

    guess = None
    while guess != secret_number:
        guess = int(input("Enter a guess: "))

        if guess < secret_number:
            print("Your guess is too low")
        elif guess > secret_number:
            print("Your guess is too high")

    print(f"Congratulations! The number was {secret_number}")

if __name__ == "__main__":
    main()
