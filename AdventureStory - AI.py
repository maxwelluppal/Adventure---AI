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
    print("2. Continue deeper into the forest.")
    print("3. Cast a protective charm and proceed cautiously.")
    print("4. Retreat back to Hogwarts.")
    print("5. Climb a tree to get a better view.")
    choice = input("Enter your choice (1-5): ")
    if choice == "1":
        print("You discover a wounded unicorn, but before you can help, you are ambushed by a group of centaurs!")
        print("You narrowly escape, but you're injured.")
    elif choice == "2":
        print("You venture deeper into the forest and encounter a colony of Acromantulas!")
        print("You manage to flee, but it was a harrowing experience.")
    elif choice == "3":
        print("With your protective charm, you navigate through the forest safely, avoiding any danger.")
        print("You emerge unscathed from the Forbidden Forest.")
    elif choice == "4":
        print("You wisely decide to return to Hogwarts, avoiding potential danger in the forest.")
    elif choice == "5":
        print("You climb a tree and spot a glimmering object in the distance.")
        print("Curious, you investigate and find a hidden treasure chest!")
        print("Congratulations! You've found a valuable treasure!")

def hogwarts_castle():
    print("You decide to explore the secret passages of Hogwarts castle.")
    print("The castle is full of hidden nooks and crannies.")
    print("You come across a staircase that seems to lead to a forbidden area.")
    print("What will you do?")
    print("1. Ascend the staircase.")
    print("2. Explore a different part of the castle.")
    print("3. Use the Marauder's Map to find hidden passageways.")
    print("4. Seek guidance from a portrait.")
    print("5. Search for the Room of Requirement.")
    choice = input("Enter your choice (1-5): ")
    if choice == "1":
        print("You climb the staircase and find yourself in the restricted section of the library.")
        print("You stumble upon a rare book of dark magic, but you're caught by Filch!")
        print("You receive a detention but manage to avoid more serious consequences.")
    elif choice == "2":
        print("You explore a different part of the castle and find a secret room filled with enchanted objects.")
        print("You spend hours discovering their mysteries before returning to your common room.")
    elif choice == "3":
        print("Using the Marauder's Map, you uncover a hidden passageway behind a tapestry.")
        print("You navigate through it and find yourself in Hogsmeade!")
        print("You enjoy a Butterbeer before sneaking back into Hogwarts.")
    elif choice == "4":
        print("You seek guidance from a portrait of a former headmaster.")
        print("The portrait advises you to be cautious and avoid certain areas of the castle.")
        print("You heed the advice and continue exploring more safely.")
    elif choice == "5":
        print("After much searching, you finally stumble upon the Room of Requirement.")
        print("Inside, you find a trove of forgotten treasures, including a valuable magical artifact!")
        print("Congratulations! You've discovered a priceless treasure!")

def main():
    intro()
    choice = input("Enter your choice (1, 2): ")
    if choice == "1":
        forbidden_forest()
    elif choice == "2":
        hogwarts_castle()
    else:
        print("Invalid choice. Please enter 1 or 2.")
        main()

if __name__ == "__main__":
    main()


