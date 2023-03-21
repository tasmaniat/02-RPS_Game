import random


# Functions go here
def check_rounds():
    while True:
        print()
        response = input("How many rounds")

        round_error = "Please type either <enter> or an " \
                      "integer that is more then 0\n"

        # if infinite mode not chosen, check response
        # is an integer that is more than 0
        if response != "":
            try:
                response = int(response)

                # if response is too low, go back to
                # start of loop
                if response < 1:
                    print(round_error)
                    continue

            # if response is not an integer go back to
            # start of loop
            except ValueError:
                print(round_error)
                continue

        return response


def choice_checker(question, valid_list, error):
    valid = False
    while not valid:

        # ask user for choice (and put choice in lowercase)
        response = input(question).lower()

        # iterates through list and if response == item
        # in the list (or the first letter of an item), the
        # full item name is returned

        for var_item in valid_list:
            if response == var_item[0] or response == var_item:
                return var_item

        # output error if the item not in list
        print(error)
        print()


def yes_no(question):
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("please type yes / no")
            print()


def instructions():
    print()
    print("**** How to play ****")
    print()
    print("choose either a number of rounds or press <enter> for \n"
          "infinite mode")
    print()
    print("Then for each round, choose from rock \n"
          "/paper /scissors (or xxx to quit)")
    print("you can type r / p / s / x if you \n"
          "don't want to type the entire word.")
    print()
    print("The rules are...")
    print("- Rock beats scissors")
    print("- Scissors beats paper")
    print("- Paper beats rock")
    print()
    print("*** Have fun ***")
    print()
    return ""


# Main Routine goes here...
played_before = yes_no("Have you played the "
                       "game before?  ")

if played_before == "no":
    instructions()

print("program continues")

# Main routine goes here

# Lists of valid responses
yes_no_list = ["yes", "no"]
rps_list = ["rock", "paper", "scissors", "xxx"]

# ask user if they have played before.
# If 'yes', show instructions


# ask user for # of rounds then loop...
rounds_played = 0

# initialize lost / drawn counters
rounds_lost = 0
rounds_drawn = 0
choose_instruction = "Please chose rock (r), paper (p) or scissors (s)"

# ask user # of rounds, <enter> for infinite mode
rounds = check_rounds()

end_game = "no"
while end_game == "no":

    # Start of Game Play Loop

    # Rounds Heading
    print()
    if rounds == "":
        heading = "Continuous Mode: " \
                  "Round {}".format(rounds_played + 1)
    else:
        heading = "Round {} of" \
                  " {} ".format(rounds_played + 1, rounds)

    print(heading)
    choose_instruction = "please choose rock," \
                         " paper or scissors " \
                         "or 'xxx' to exit"
    choose_error = "Please choose from rock /" \
                   "paper / scissors (or xxx to quit)"

    # Ask the user for choice and check it's valid
    user_choice = choice_checker(choose_instruction, rps_list,
                                 choose_error)

    # end of game if exit code is typed
    if user_choice == "xxx":
        break

    # get computer choice
    comp_choice = random.choice(rps_list[:-1])
    print("comp_choice: ", comp_choice)

    # compare choices
    if comp_choice == user_choice:
        result = "tie"
        rounds_drawn += 1
    elif user_choice == "rock" and comp_choice == "scissors":
        result = "won"
    elif user_choice == "paper" and comp_choice == "rock":
        result = "won"
    elif user_choice == "scissors" and comp_choice == "paper":
        result = "won"
    else:
        result = "lost"
        rounds_lost += 1

    if result == "tie":
        feedback = "it's a tie"
    else:
        feedback = "{} vs {} you {}".format(user_choice,
                                            comp_choice, result)

    # output results
    print(feedback)

    rounds_played += 1

    # end game if requested # of rounds has been played
    if rounds_played == rounds:
        break

# ask user if they want to see their game history.
# If 'yes' show game history
game_summary = []

for item in range(0, 5):
    result = input("choose result: ")

    outcome = "Round {}: {}".format(item, result)

    if result == "lost":
        rounds_lost += 1
    elif result == "tie":
        rounds_drawn += 1

    game_summary.append(outcome)

rounds_won = rounds_played - rounds_lost - rounds_drawn

# ***** Calculate Game Stats *****
percent_win = rounds_won / rounds_played * 100
percent_lose = rounds_lost / rounds_played * 100
percent_tie = rounds_drawn / rounds_played * 100

print()
print("******** Game History ********")
for game in game_summary:
    print(game)

print()

# show game statistics
# displays game stats with % values to the nearest whole number
print("******** Game Statistics ********")
print("Win: {}, ({:.0f}%)\nLoss: {}, "
      "({:.0f}%)\nTie: {}, ({:.0f}%)".format(rounds_won,
                                             percent_win,
                                             rounds_lost,
                                             percent_lose,
                                             rounds_drawn,
                                             percent_tie))

# Quick Calculations (stats)
rounds_won = rounds_played - rounds_lost - rounds_drawn

# End of game Statements
print()
print('***** End Game Summary *****')
print("won: {} \t|\t Lost: {} \t|\t Draw: "
      "{}".format(rounds_won, rounds_lost, rounds_drawn))
print()
print("Thanks for playing")
