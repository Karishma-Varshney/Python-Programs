import random
from hangman_art import logo,stages,words_list

# importing logo of hangman from hangman_art module
print(logo)

# imported list of words from handman_art module
choosen_word = random.choice(words_list)
print(f"Lets play hangman game.\nThe word is {choosen_word}")

end_of_game = False
while not end_of_game:

    guess = input("guess a letter :\n")

    display = []
    for _ in range(len(choosen_word)):
        display += "_"
        

    if display == guess:
        print(f"you've already guessed {guess} ") 

    # checking the guessed letter
    for pos in range(len(choosen_word)):
        letter = choosen_word[pos]
        if guess == letter:
            display[pos] = letter
    print(display)

    if '_' not in display:
        end_of_game = True
        print("You win.")
        print(f"your word is {display}")    

    lives = 6
    if guess not in choosen_word:
        print(f" {guess} is not in the word . You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(stages[lives])   
        


