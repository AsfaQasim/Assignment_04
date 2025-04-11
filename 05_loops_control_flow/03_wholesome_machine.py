correct_afformation = "I am capable of doing anything I put my mind to.."

def main():
    print("Welcome to the Wholesome Machine")

    while True:
        user = input("Type the following affirmation: " + correct_afformation + "\n")

        if user == correct_afformation:
            print("That's right!")
            break
        else:
            print("That was not the correct affirmation, please try again.")

if __name__ == "__main__":
    main()
