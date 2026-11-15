import random

score = 0
for round in range(3):
    print(f"Round {round + 1}:")
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    computer_choice = random.choice(["rock", "paper", "scissors"])
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win this round!")
        score += 1
    else:
        print("Computer wins this round!")
        score -= 1

print(f"Final score: {score}")