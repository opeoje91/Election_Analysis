# Incorporate the random library
import random

# Print Title
print("Let's Play Rock Paper Scissors!")

# Specify the three options
options = ["r", "p", "s"]

# Computer Selection
computer_choice = random.choice(options)

# User Selection
user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")

# Run Conditionals
if (user_choice == "r" and computer_choice == "p"): 
    print(f"The computer selected {computer_choice}. You chose {user_choice}")
    print("The user have lost.")
elif (user_choice == "p" and computer_choice == "s"):
    print(f"The computer selected {computer_choice}. You selected {user_choice}")
    print("Sorry, You lost!")
elif(user_choice == "s" and computer_choice == "r"):
    print(f"The computer selected {computer_choice}. You selected {user_choice}")
    print("Sorry, You lost!")
elif(user_choice == computer_choice):
    print("There is a draw")
else:
    print("You have won!")
