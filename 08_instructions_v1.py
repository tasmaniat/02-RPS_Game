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
    print("**** How to play ****")
    print()
    print("choose either a number of rounds or press <enter> for infinite mode")
    print()
    print("Then for each round, choose from rock "
          "/paper /scissors (or xxx to quit)")
    print()
    print("The rules of the game go here")
    print()
    return ""


# Main Routine goes here...
played_before = yes_no("Have you played the "
                       "game before?  ")

if played_before == "no":
    instructions()

print("program continues")
