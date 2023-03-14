import random


# Functions go here
def check_rounds():
    while True:
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

        for item in valid_list:
            if response == item[0] or response == item:
                return response

        # output error if the item not in list
        print(error)
        print()


# Main routine goes here

# Lists of valid responses
yes_no_list = ["yes", "no"]
rps_list = ["rock", "paper", "scissors", "xxx"]

# ask user if they have played before.
# If 'yes', show instructions


# ask user for # of rounds then loop...
rounds_played = 0
choose_instruction = "please choose a rock (r), paper " \
                     "(p) or scissors (s)"

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
                         "paper or scissors " \
                         "or 'xxx' to exit"
    choose_error = "Please choose from rock /" \
                   "paper / scissors (or xxx to quit)"

    # Ask the user for choice and check it's valid
    choose = choice_checker(choose_instruction, rps_list,
                            choose_error)

    # get computer choice
    comp_choice = random.choice(rps_list[:-1])
    print("Computer chose:", comp_choice)

    # compare choices

    # End game if exit code is typed
    if choose == "xxx":
        break

    # **** rest of loop / game *****
    print("You chose: {}".format(choose))

    rounds_played += 1

    # end game if requested # of rounds has been played
    if rounds_played == rounds:
        break

# ask user if they want to see their game history.
# If 'yes' show game history

# show game statistics
