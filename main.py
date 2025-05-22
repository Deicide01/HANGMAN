import random

#choose a random word from word_list and assign it to variable chose_word

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)

#STEP 2
#create a placeholder with the same no. of blanks as chosen_word

placeholder=""
for i in range(len(chosen_word)):
    placeholder += "_" 
print(placeholder)

#ask the user to guess a letter and assign it to a vairable guess

guess = input("guess a letter:").lower()
#.lower() for lowercase
print(guess)

#check if the letter chosen by the user is in chosen_word. print right or wrong

for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")

#create a display that puts the guess letter in the right positions and a blank in the rest of the strings





