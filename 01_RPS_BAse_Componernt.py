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


# Main routine goes here

# Lists of valid responses
yes_no_list = ["yes", "no"]
rps_list = ["rock", "paper", "scissors", "xxx"]

# ask user if they have played before.
# If 'yes', show instrucyions


# ask user for # of rounds then loop


# ask user if they want to see their game history.
# If 'yes' show game history

# show game statistics
