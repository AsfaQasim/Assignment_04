Min_Height: int = 50

def main():
    user: int = int(input("How tall are you? "))

    if user >= Min_Height:
        print("You are tall enough to ride! 🎢")
    else:
        print("You are not tall enough to ride. Maybe next year! 😊")

if __name__ == "__main__":
    main()
