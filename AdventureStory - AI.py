# Programmer: Maxwell Uppal
# Date: 3.18.24
# Program: Harry  Potter choose your own adventure game

def intro():
    print("Welcome to the Choose Your Own Adventure game!")
    print("You find yourself standing at a crossroads. Which path will you choose?")
    print("1. Take the path through the forest.")
    print("2. Follow the path up the mountain.")

def forest_path():
    print("You venture into the forest.")
    print("You hear strange noises around you, but you push forward.")
    print("Suddenly, you encounter a bear!")
    print("What will you do?")
    print("1. Try to scare the bear away.")
    print("2. Slowly back away.")
    choice = input("Enter your choice (1 or 2): ")
    if choice == "1":
        print("The bear seems unimpressed and charges at you. You have been mauled.")
    elif choice == "2":
        print("You slowly back away, and the bear loses interest. You survive!")

def mountain_path():
    print("You start your ascent up the mountain.")
    print("The path is steep, but the view is breathtaking.")
    print("You reach a fork in the road.")
    print("1. Take the narrow path to the left.")
    print("2. Continue on the wider path to the right.")
    choice = input("Enter your choice (1 or 2): ")
    if choice == "1":
        print("The narrow path leads to a dead end. You must backtrack.")
    elif choice == "2":
        print("You continue on the wider path and reach the summit. You have a sense of accomplishment!")

def main():
    intro()
    choice = input("Enter your choice (1 or 2): ")
    if choice == "1":
        forest_path()
    elif choice == "2":
        mountain_path()
    else:
        print("Invalid choice. Please enter 1 or 2.")
        main()

if __name__ == "__main__":
    main()
