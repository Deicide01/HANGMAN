import random

#update the wordlist to use the 'worldlist' from hangman_words.py
import hangman_words
from hangman_art import stages, logo

lives = 6

#import the logos from hangman_art.py and print it at the start of the game
print(logo)
chosen_word = random.choice(hangman_words.word_list)
print(chosen_word)

placeholder=""
for i in range(len(chosen_word)):
    placeholder += "_" 
print(placeholder)

game_over = False

correct_letters = []

while not game_over:
    print(f"*********************{lives}/6 LIVES LEFT**********************")
    guess = input("guess a letter:").lower()

#if the user entered the letter they already guessed print and let them know
    if guess in correct_letters:
       print(f"you've already guessed {guess}") 

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("word to guess:" + display)

    #if the letter is not in chosen_word, print the letter and let them know they lost a life
    #eg - you guessed d, thats's not in the word. you lose a life.
    
    if guess not in chosen_word:
        lives -= 1
        print(f"you guessed {guess}, thats's not in the word. you lose a life.")
        if lives == 0:
            game_over = True
            print(f"It was:{chosen_word} YOU LOSE!!!!!")

    if "_" not in display:
        game_over = True
        print("*********************YOU WIN!!!!!********************")

    print(stages[lives])