#Task 1 - Hangman Project
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

word_list = ["ardvark", "baboon", "camel", "elephant", "giraffe", "kangaroo", "dolphin", "tiger", "zebra", "penguin"]
chosen_word = random.choice(word_list)
#print(f'Pssst, the solution is {chosen_word}.')  # For testing
lives = 0
letter_count = len(chosen_word)
placeholder = ""
correct_guesses = []
game_over = False
for i in range(letter_count):
    placeholder += "_"
    #display.append("_")
print(placeholder)


while not game_over:
    user_choice = input("Guess a letter: ").lower().strip()
    display = ""    

    for letter in chosen_word:
        if letter == user_choice:
            display += letter
            correct_guesses.append(letter)
            #print("Right!")
        elif letter in correct_guesses:
            display += letter
        else:
            display += "_"            
            #print("Wrong!")        
        
    print(f"The word is -------------------------------  {display} \n")
    
    if user_choice not in chosen_word:
        lives += 1        
        if lives == 0:
            print("You lose!\n")
            game_over = True
    
    if "_" not in display:
        print("You win!\n")
        game_over = True

    print(stages[lives])
