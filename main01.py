import random
stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

word_list = ["aardvark", "baboon", "camel"]

#create a variable called lives to keep track of the no. of chances
#set 'lives' to equal 6

lives = 6

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder=""
for i in range(len(chosen_word)):
    placeholder += "_" 
print(placeholder)

game_over = False

correct_letters = []

while not game_over:
    guess = input("guess a letter:").lower()

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(display)

#if guess is not a letter in the chosen_word, reduce 'lives' by 1
#if lives goes down to 0 then the game shoud stop and it should print 'you lose'

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("you lose!!!")

    if "_" not in display:
        game_over = True
        print("you win!!!")

#print ascii art from stages
#that corresponds to the no. of lives remaining

    print(stages[lives])