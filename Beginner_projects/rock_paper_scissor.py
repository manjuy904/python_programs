# Rock_paper_Scissor!

import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissor"]

while True:
    user_input = input("Type rock/paper/scissor or Q to quit: " )
    if user_input.lower() == "q":
        break
    if user_input not in options:
        continue
    
    random_number = random.randint(0, 2)
    # 0 = rock, 1 = paper, 2 = scissor
    
    computer_input = options[random_number]
    print("computer picked", computer_input)
    
    if user_input == "rock" and computer_input == "scissor":
        print("You won!")
        user_wins += 1
        
    elif user_input == "paper" and computer_input == "rock":
        print("You won!")
        user_wins += 1
        
    elif user_input == "scissor" and computer_input == "paper":
        print("You won!")
        user_wins += 1
    else:
        print ("You lost!")
        computer_wins += 1
        
print("You won", user_wins, "times.")
print("Computer won", computer_wins, "times.")
    