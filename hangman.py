import random

# List of car brands
words = ["tesla", "mercedes", "toyota", "chevrolet", "bmw", "audi"]

# Initialize variables
word = random.choice(words)
guessed_word = ["_"] * len(word)
attempts = 6
score = 0

print("Welcome to Hangman: Car Edition!")
print("Guess the car brand. You have 6 attempts.")
print("Word to guess:", " ".join(guessed_word))

while attempts > 0 and "_" in guessed_word:
    guess = input("\nEnter a letter: ").lower()

    if guess in word:
        score += 10
        print("Correct guess!")
        for i, letter in enumerate(word):
            if letter == guess:
                guessed_word[i] = guess
    else:
        attempts -= 1
        score -= 5
        print(f"Incorrect! Attempts left: {attempts}")

    print("Word to guess:", " ".join(guessed_word))
    print(f"Score: {score}")

if "_" not in guessed_word:
    score += 50
    print(f"\nCongratulations! You guessed the word '{word}'. Final Score: {score}")
else:
    print(f"\nGame Over! The word was '{word}'. Final Score: {score}")
def display_hangman(attempts):
    stages = [
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      
           |      
           |      
           |     
           -
        """
    ]
    return stages[5 - attempts]

def hangman():
    word = "python"
    guessed_letters = []
    attempts = 5

    print("Welcome to Hangman!")
    print(display_hangman(attempts))

    while attempts > 0:
        display_word = "".join([letter if letter in guessed_letters else "_" for letter in word])
        print(f"The word: {display_word}")

        if display_word == word:
            print("Congratulations! You won!")
            break

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            continue

        if guess in guessed_letters:
            continue

        guessed_letters.append(guess)

        if guess in word:
            print(f"Correct! The letter '{guess}' is in the word.")
        else:
            attempts -= 1
            print(f"Wrong! The letter '{guess}' is not in the word.")
            print(f"Attempts left: {attempts}")
            print(display_hangman(attempts))

    if attempts == 0:
        print(f"You lost! The word was '{word}'.")

hangman()