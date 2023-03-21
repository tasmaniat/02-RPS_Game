# Function go here...
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
