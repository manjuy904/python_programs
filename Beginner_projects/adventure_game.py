#choose you own adventure game

name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go (left/right)? ").lower()

if answer == "left":
    answer1 = input("You come to a river, you can walk around it or swim accross? Type walk to walk around and swim to swim accross (swim/walk): ")
    if answer1 == "swim":
        print("You swam acrross and were eaten by an alligator.")
    elif answer1 == "walk":
        print("You walked for many miles, ran out of water and you lost the game.")
    else:
        print("Not a valid option. You lose.")
    
elif answer == "right":
    answer2 = input("You come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ")
    if answer2 == "back":
        print("You go back and lose.")
    elif answer2 == "cross":
        answer3 =input("You cross the bridge and meet a stranger. Do you talk to them (yes/no)? ")
        if answer3 == "yes":
            print("You talk to the stanger and they give you gold. You WIN!")
        elif answer3 == "no":
            print("You ignore the stranger and they are offended and you lose.")
        else:
            print("Not a valid option. You lose.")
                
    else:
        print("Not a valid option. You lose.")
    
else:
    print("Not a valid option. You lose") 
    
print("Thank you", name, "for trying")