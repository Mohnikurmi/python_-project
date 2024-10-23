import random

# List of words to choose from
words = ["python", "programming", "hangman", "developer", "algorithm", "function", "variable"]


def select_random_word(word_list):
    """Selects a random word from the word list."""
    return random.choice(word_list)


def display_word(word, guessed_letters):
    """Displays the word with guessed letters and underscores for missing letters."""
    return ''.join([letter if letter in guessed_letters else '_' for letter in word])


def play_hangman():
    # Setup
    word = select_random_word(words)  # Randomly select a word
    guessed_letters = set()  # To keep track of correctly guessed letters
    incorrect_guesses = set()  # To keep track of incorrect guesses
    max_incorrect_guesses = 6  # Max allowed incorrect guesses

    print("Welcome to Hangman!")

    # Game loop
    while len(incorrect_guesses) < max_incorrect_guesses:
        # Display the current state of the word
        print(f"\nWord: {display_word(word, guessed_letters)}")
        print(f"Incorrect guesses: {', '.join(incorrect_guesses)}")
        print(f"Remaining guesses: {max_incorrect_guesses - len(incorrect_guesses)}")

        # Get the player's guess
        guess = input("Guess a letter: ").lower()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single letter.")
            continue

        # If the letter was already guessed
        if guess in guessed_letters or guess in incorrect_guesses:
            print("You've already guessed that letter.")
            continue

        # Check if the guess is in the word
        if guess in word:
            print(f"Good guess! {guess} is in the word.")
            guessed_letters.add(guess)
        else:
            print(f"Sorry, {guess} is not in the word.")
            incorrect_guesses.add(guess)

        # Check if the player has guessed all the letters
        if all(letter in guessed_letters for letter in word):
            print(f"\nCongratulations! You've guessed the word: {word}")
            break
    else:
        # Player ran out of guesses
        print(f"\nGame over! The word was: {word}")


if __name__ == "__main__":
    play_hangman()
