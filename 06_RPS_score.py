# RPS Component 6 - scoring system

# Rounds won will be calculated (total- draw - lost)
rounds_played = 0
rounds_lost = 0
rounds_drawn = 0

# Results for testing purposes
test_results =["won", "won", "loss", "loss", "tie"]

# Play game
for item in test_results:
    rounds_played +=1

    # Generate computer choice

    result = item

    if result == "tie":
        result = "It's a tie"
        rounds_drawn += 1
    elif result == "loss":
        rounds_lost += 1

    
