import random

stages = [
    '''
        ------
        |    |
        |    
        |    
        |    
        |         
    --------
    ''',
    '''
        ------
        |    |
        |    O
        |    
        |    
        |         
    --------
    ''',
    '''
        ------
        |    |
        |    O
        |    |
        |    
        |         
    --------
    ''',
    '''
        ------
        |    |
        |    O
        |   /|
        |    
        |         
    --------
    ''',
    '''
        ------
        |    |
        |    O
        |   /|\\
        |    
        |         
    --------
    ''',
    '''
        ------
        |    |
        |    O
        |   /|\\
        |   / 
        |         
    --------
    ''',
    '''
        ------
        |    |
        |    O
        |   /|\\
        |   / \\
        |         
    --------
    '''
]

words = ["orange", "banana", "grapes", "kiwi", "pineapple", "mango", "peach"]
chosen_word = random.choice(words)
word_display = ['_' for _ in chosen_word]
guess_letters = []
lives = len(stages) - 1

print("Welcome to Hangman!")
print("Guess the fruit word.")

while True:
    print("\n" + " ".join(word_display))
    guess = input("Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a valid single letter.")
        continue

    if guess in guess_letters:
        print("You already guessed that letter. Try again.\n")
        continue

    guess_letters.append(guess)

    if guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                word_display[index] = guess
        if "_" not in word_display:
            print("\n" + " ".join(word_display))
            print("Congratulations! You guessed the word correctly. 🎉")
            break
    else:
        print(f"Wrong guess. You lose a life.")
        print(stages[len(stages) - lives - 1])
        lives -= 1
        if lives < 0:
            print("Game Over! You ran out of lives.")
            print(f"The word was: {chosen_word}")
            break
