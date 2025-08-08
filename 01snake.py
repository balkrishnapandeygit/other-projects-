import random

""" 1 for snake
-1 for water
0 for gun """

computer = random.choice([0, 1, -1])  # Changed to a list

while True:  # loop to check if input is valid
    youstr = input("Enter your choice (s, w, or g): ").lower()  # .lower() handles case insensitivity
    if youstr in ("s", "w", "g"):
        break
    else:
        print("Invalid input. Please enter 's', 'w', or 'g'.")

youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "snake", -1: "water", 0: "gun"} 

you = youDict[youstr]  
print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

if computer == you:
    print("It's a draw")
else:
    if (computer == -1 and you == 1) or (computer == 1 and you == 0) or (computer == 0 and you == -1):  # combined conditions
        print("You win")
    else:
        print("You lose")  # Simplified the lose condition. All other cases are a loss.