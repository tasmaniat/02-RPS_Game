# Functions used to check input is valid


def check_rounds():
    while True:
        response = input("How many rounds")

        round_error = "Please type either <enter> " \
                      "or an integer that is more then 0"
        if response != "":
            try:
                response = int(response)

                if response < 1:
                    print(round_error)
                    continue

            except ValueError:
                print(round_error)
                continue

        return response


# MAin routine foes here...

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
        choose = input("{} or 'xxx' to"
                       " end: ".format(choose_instruction))

        # End game if exit code is typed
        if choose == "xxx":
            break

        if rounds_played == rounds - 1:
            end_game = "yes"

        # rest of loop / game
        print("you chose {]".format(choose))

        rounds_played += 1

    print("Thank you fro playing")
