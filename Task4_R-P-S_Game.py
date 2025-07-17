import random  # Import random module for computer's choice

# Valid full choices
choices = ['rock', 'paper', 'scissors']

# Initialize score counters
user_score = 0
computer_score = 0

print("Welcome to Rock-Paper-Scissors Game!")
print("Instructions: Enter R for Rock, P for Paper, S for Scissors, or Q to Quit.\n")

while True:
    # Get user input and convert to lowercase
    user_input = input("Choose (R/P/S or Q to quit): ").lower()

    # Map short input to full choice
    if user_input == 'q':
        break
    elif user_input == 'r':
        user = 'rock'
    elif user_input == 'p':
        user = 'paper'
    elif user_input == 's':
        user = 'scissors'
    else:
        print("Invalid input. Please enter R, P, S, or Q.\n")
        continue

    # Show what user chose
    print("You chose:", user)

    # Computer randomly chooses
    computer = random.choice(choices)
    print("Computer chose:", computer)

    # Determine result and update scores
    if user == computer:
        print("It's a tie!")
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'paper' and computer == 'rock') or \
         (user == 'scissors' and computer == 'paper'):
        print("You win!")
        user_score += 1
    else:
        print("You lose.")
        computer_score += 1

    # Show current score
    print(f"Score => You: {user_score}, Computer: {computer_score}\n")

# Final message after quitting
print("\nThanks for playing!")
print(f"Final Score => You: {user_score}, Computer: {computer_score}")
# End of the game
print("See You Next Time!")
