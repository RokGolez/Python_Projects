# Dice game for 1-4 player. The first one to get 51 wins.
# Still allows the other players to have their turn after the first one has reached max score


import random

# Function to roll a dice between 1 and 6
def roll():
    min_value = 1
    max_value = 6
    return random.randint(min_value, max_value)

# Prompt user to enter the number of players
while True:
    players_input = input("Enter the number of players (2 - 4): ")
    if players_input.isdigit():
        num_players = int(players_input) # Converting str to int
        if 2 <= num_players <= 4:
            break
        else:
            print("Must be between 2 - 4 players.")
    else:
        print("Invalid, try again.")

max_score = 50
player_scores = [0 for _ in range(num_players)]

# Main game loop
while max(player_scores) < max_score:
    for player_idx in range(num_players):
        print("\nPlayer number", player_idx + 1, "turn has just started!")
        print("Your total score is:", player_scores[player_idx], "\n")
        current_score = 0

        while True:
            should_roll = input("Would you like to roll (y)? ")
            if should_roll.lower() != "y":
                break

            value = roll()
            if value == 1:
                print("You rolled a 1! Turn done!")
                break
            else:
                current_score += value
                print("You rolled a:", value)
                print("Your score is:", current_score)

        player_scores[player_idx] += current_score
        print("Your total score is:", player_scores[player_idx])

# Announce the winner
max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print("\nPlayer number", winning_idx + 1, "is the winner with a score of:", max_score)
