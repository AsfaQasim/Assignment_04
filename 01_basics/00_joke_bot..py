PROMPT: str = "What do you want!"
JOKE :str = """Why did the scarecrow win an award?
Because he was outstanding in his field!"""
SORRY : str = "Sorry I only tell joke"
def main():
    user_input = input("Do you want to hear a joke? ")
    user_input = user_input.strip().lower()

    if user_input == "yes":
        print(JOKE)
    else:
        print(SORRY)
if __name__ == "__main__":
    main()