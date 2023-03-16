# Function go here...
def yes_no(question):
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("please answer yes / no")


def instructions():
    print("**** How to play ****")
    print()
    print("The rules of the game go here")
    print()
    return ""


# Main Routine goes here...
played_before = yes_no("Have you played the "
                       "game before?  ")

if played_before == "no":
    instructions()

print("programs continues")
