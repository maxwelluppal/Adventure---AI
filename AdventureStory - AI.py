# Programmer: Maxwell Uppal
# Date: 3.18.24
# Program: Harry  Potter choose your own adventure game

def intro():
    print("Welcome to the Harry Potter Choose Your Own Adventure game!")
    print("You find yourself standing at a crossroads near Hogwarts School of Witchcraft and Wizardry.")
    print("Which path will you choose?")
    print("1. Enter the Forbidden Forest.")
    print("2. Explore the secret passages of Hogwarts castle.")

def forbidden_forest():
    print("You venture into the Forbidden Forest.")
    print("The trees loom ominously overhead as you tread carefully.")
    print("You hear rustling in the bushes nearby.")
    print("What will you do?")
    print("1. Investigate the source of the rustling.")
    print("2. Turn back and return to Hogwarts.")
    choice = input("Enter your choice (1 or 2): ")
    if choice == "1":
        print("You discover a wounded unicorn, but before you can help, you are ambushed by a group of centaurs!")
        print("You narrowly escape, but you're injured.")
    elif choice == "2":
        print("You wisely decide to return to Hogwarts, avoiding potential danger in the forest.")

def hogwarts_castle():
    print("You decide to explore the secret passages of Hogwarts castle.")
    print("The castle is full of hidden nooks and crannies.")
    print("You come across a staircase that seems to lead to a forbidden area.")
    print("What will you do?")
    print("1. Ascend the staircase.")
    print("2. Explore a different part of the castle.")
    choice = input("Enter your choice (1 or 2): ")
    if choice == "1":
        print("You climb the staircase and find yourself in the restricted section of the library.")
        print("You stumble upon a rare book of dark magic, but you're caught by Filch!")
        print("You receive a detention but manage to avoid more serious consequences.")
    elif choice == "2":
        print("You explore a different part of the castle and find a secret room filled with enchanted objects.")
        print("You spend hours discovering their mysteries before returning to your common room.")

def main():
    intro()
    choice = input("Enter your choice (1 or 2): ")
    if choice == "1":
        forbidden_forest()
    elif choice == "2":
        hogwarts_castle()
    else:
        print("Invalid choice. Please enter 1 or 2.")
        main()

if __name__ == "__main__":
    main()

