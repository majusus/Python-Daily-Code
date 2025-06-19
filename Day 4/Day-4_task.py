import random

#Task 1 - Heads or Tails
print("Welcome to Heads or Tails!")
while True:
    user_choice = input("Choose Heads or Tails (H/T): ").strip().upper()
    if user_choice not in ['H', 'T']:
        print("Invalid choice. Please choose 'H' for Heads or 'T' for Tails.")
        continue
    
    computer_choice = random.choice(['H', 'T'])
    print(f"Computer chose: {'Heads' if computer_choice == 'H' else 'Tails'}")
    
    if user_choice == computer_choice:
        print("You win!")
    else:
        print("You lose!")
    
    play_again = input("Do you want to play again? (y for yes/n for no): ").strip().lower()
    if play_again != 'y':
        break


#Task 2 - Banker Roulette
print("\nWelcome to Banker Roulette!")
friends = ["Alice", "Bob", "Charlie", "David", "Eve"]
while True:
    if not friends:
        print("No friends left to choose from!")
        break
    
    chosen_friend = random.choice(friends)
    print(f"{chosen_friend} is going to pay the bill!")
    
    play_again = input("Do you want to play again? (y for yes/n for no): ").strip().lower()
    if play_again != 'y':
        break


#Task 3 - Rock, Paper, Scissors
print("\nWelcome to Rock, Paper, Scissors!")

# ASCII art for rock, paper, scissors
rock_art = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper_art = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors_art = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

while True:
    user_choice = input("Choose Rock, Paper, or Scissors (R/P/S): ").strip().upper()
    if user_choice not in ['R', 'P', 'S']:
        print("Invalid choice. Please choose 'R' for Rock, 'P' for Paper, or 'S' for Scissors.")
        continue
    
    # Print user's choice with ASCII art
    print("\nYour choice:")
    if user_choice == 'R':
        print(rock_art)
    elif user_choice == 'P':
        print(paper_art)
    else:
        print(scissors_art)
    
    computer_choice = random.choice(['R', 'P', 'S'])
    
    # Print computer's choice with ASCII art
    print("Computer chose:")
    if computer_choice == 'R':
        print(rock_art)
    elif computer_choice == 'P':
        print(paper_art)
    else:
        print(scissors_art)
    
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'R' and computer_choice == 'S') or \
         (user_choice == 'P' and computer_choice == 'R') or \
         (user_choice == 'S' and computer_choice == 'P'):
        print("You win!")
    else:
        print("You lose!")
    
    play_again = input("Do you want to play again? (y for yes/n for no): ").strip().lower()
    if play_again != 'y':
        break