import random
options = ["r","p","s"]
print("Lets Play Rock Paper Scissers!")
computer_choice = random.choice(options)
user_choice = input("Make your choice r p s ")

if (computer_choice == "r" and user_choice =="p"):
    print("you win")
else:
    print("you loose")
