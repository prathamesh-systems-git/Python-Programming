#Python Program to write a Rocks-Paper-Scissors Games using List & Random Function:
#Importing the Random Function since it is required for the program to Run.
import random 

print("Welcome to the Rocks - Papers - Scissors Game...!")
random_choice = ["Rocks", "Papers", "Scissors"]
players_choice = input("What Would You Choose: (Rocks / Papers / Scissors)? ")
systems_choice = random.choice(random_choice)
if players_choice == "Rocks" and systems_choice == "Rocks":
    print("System Chose: Rocks")
    print("You Choose: Rocks")
    print("Match Tied.")
elif players_choice == "Rocks" and systems_choice == "Papers":
    print("System Chose: Papers")
    print("You Choose: Rocks")
    print("System Won!!!!!.")
elif players_choice == "Rocks" and systems_choice == "Scissors":
    print("System Chose: Scissors")
    print("You Choose: Rocks")
    print("You Won!!!!!.")
elif players_choice == "Papers" and systems_choice == "Rocks":
    print("System Chose: Rocks")
    print("You Choose: Papers")
    print("You Won!!!!!.")
elif players_choice == "Papers" and systems_choice == "Papers":
    print("System Chose: Papers")
    print("You Choose: Papers")
    print("Match Tied.")
elif players_choice == "Papers" and systems_choice == "Scissors":
    print("System Chose: Scissors")
    print("You Choose: Papers")
    print("System Won!!!!!.")
elif players_choice == "Scissors" and systems_choice == "Rocks":
    print("System Chose: Rocks")
    print("You Choose: Scissors")
    print("System Won!!!!!.")
elif players_choice == "Scissors" and systems_choice == "Papers":
    print("System Chose: Papers")
    print("You Choose: Scissors")
    print("You Won.")
else:
    print("Match Tied. Both Values are Same. Play Again")
