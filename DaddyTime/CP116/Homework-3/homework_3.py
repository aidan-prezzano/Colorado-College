# ************************************************************************** Help

def help_menu():
    # Neatly prints out all valid user inputs and what they do
    print("'add': add a new student")
    print("'set': update a student's score for an assignment")
    print("'display': print out all records in the database")
    print("'dayavg': view the average score for an assignment (across students)")
    print("'nameavg': view the average score for a student (across assignments)")
    print("'quit': exit the program")

    # Parameters:
    # ... # TODO
    # Returns:
    # None


# **************************************************************************


def mainloop():

    user_action = input("What action would you like to take? ('help' for options): ")

    while user_action != "quit":
        if user_action == "help":
            print(help_menu())
            user_action = input("What action would you like to take? ('help' for options): ")

    print("See ya later")


# **************************************************************************


mainloop()

# **************************************************************************
