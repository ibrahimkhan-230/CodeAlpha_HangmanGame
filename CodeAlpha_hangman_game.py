import random

def hangman():
    words = ["python", "hangman", "program", "computer", "keyboard"]
    
    secret_word = random.choice(words)
    
    guessed_letters = []
    max_attempts = 6
    attempts_left = max_attempts
    word_progress = ["_"] * len(secret_word)
    
    print("Welcome to Hangman!")
    print(" ".join(word_progress))
    
    while attempts_left > 0 and "_" in word_progress:
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        # Check if letter was already guessed
        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try another letter.")
            continue
        
        guessed_letters.append(guess)
        
        # Check if guess is in the word
        if guess in secret_word:
            print(f"Correct! '{guess}' is in the word.")
            # Update word progress
            for i in range(len(secret_word)):
                if secret_word[i] == guess:
                    word_progress[i] = guess
        else:
            attempts_left -= 1
            print(f"Wrong! '{guess}' is not in the word. {attempts_left} attempts left.")
        
        # Display current progress
        print(" ".join(word_progress))
        print(f"Guessed letters: {', '.join(guessed_letters)}")
    
    if "_" not in word_progress:
        print(f"Congratulations! You guessed the word: {secret_word}")
    else:
        print(f"Game over! The word was: {secret_word}")

# Start the game
hangman()
