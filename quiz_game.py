print("Welcome to my Quiz Game!")

playing = input("Do you want to play? ")

if playing.lower() != "yes": 
    quit()
    
print("Okay! let's play the game :)")
score = 0

answer = input("What constant is referred to as \"The Universe\'s Clock\"? ")
if answer.lower() == "speed of light":
    print("Correct!")
    score += 1   
else:
     print("Incorrect!")
    
answer = input("What tool uses a magnetic needle that points north? ")
if answer.lower() == "compass":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
answer = input("What is the distance between two peaks of a wave called? ")
if answer.lower() == "wavelength":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
answer = input("Which insect can indicate the air temperature? ")
if answer.lower() == "cricket":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
answer = input("Newton's Second Law says that force equals mass times______ ")
if answer.lower() == "acceleration":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
print("You got", score, "questions correct")
print ("You got", (score/5)*100, "%")    
