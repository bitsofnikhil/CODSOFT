import random

options = ["rock", "paper", "scissors"]

while True:
    user = input("Enter Rock, Paper, or Scissors (or 'exit' to quit): ").lower()
    if user == "exit":
        break
    if user not in options:
        print("Invalid input. Try again.")
        continue

    computer = random.choice(options)
    print("Computer chose:", computer)

    if user == computer:
        print("It's a tie!")
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("You win!")
    else:
        print("Computer wins!")
