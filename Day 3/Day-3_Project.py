#Task 5 - Treasure Island Project
## ASCII Art for the game
print(""" _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
                                                                 """)

print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
choice1 = input("You're at a crossroad. Do you want to go 'left' or 'right'? ").strip().lower()
if choice1 == "left":
    choice2 = input("You've come to a lake. Do you want to swim across or wait for a boat? ").strip().lower()
    if choice2 == "wait":
        choice3 = input("You arrive at a house with three doors. One red, one yellow, and one blue. Which color do you choose? ").strip().lower()
        if choice3 == "yellow":
            print("You found the treasure! You win!")
        elif choice3 == "red":
            print("It's a room full of fire. Game over.")
        elif choice3 == "blue":
            print("You enter a room of beasts. Game over.")
        else:
            print("You chose a door that doesn't exist. Game over.")
    else:
        print("You were attacked by an alligator. Game over.")
else:
    print("You fell into a hole. Game over.")