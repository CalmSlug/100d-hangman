# Importing random logic, art assets and word list:
import random
import hangman_art
import hangman_words

# Initializing variables:
game_state = True
lives = 6
guesses = []

# Picking a random word from the word list:
chosen_word = random.choice(hangman_words.word_list)

# Populating a variable with correct number of blanks:
display = []
for letter in chosen_word:
    display += "_"

# Introduction art:
print(hangman_art.logo)
print()

# An infinite loop that asks user for a guess:
while game_state:
    guess = input("Guess a letter: ").lower()
    
    # Checking for repeat guesses;
    # Game doesn't move forward unless the guess is new:
    if guess in guesses:
        print("You have already guessed this letter!")
        print()
    else:
        guesses += guess
        
        # Comparing each letter of the word with the guess;
        # If it matches, a blank is replaced:
        for n in range(len(chosen_word)):
            if chosen_word[n] == guess:
                display[n] = guess
        print(display)
        
        # Removing a life if the guess was wrong:
        if guess not in chosen_word:
            print("No such letter in this word!")
            lives -= 1
        
        # Gallows art:
        print(hangman_art.stages[lives])
        
        # Checking for game ending conditions:
        if "_" not in display:
            print("You win!")
            game_state = False
        if lives == 0:
            print("You lose!")
            game_state = False
