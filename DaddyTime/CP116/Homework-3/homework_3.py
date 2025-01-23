# ************************************************************************** Help

def help_menu():
    # Neatly prints out all valid user inputs and what they do
    print("'add': add a new student")
    print("'set': update a student's score for an assignment")
    print("'display': print out all records in the database")
    print("'dayavg': view the average score for an assignment (across students)")
    print("'nameavg': view the average score for a student (across assignments)")
    print("'quit': exit the program")


# **************************************************************************

def add_menu(name):
    student_names = []
    user_name = input("what is the new students name?")
    if user_name not in student_names:
        student_names.append(user_name)
        print(f"Successfully added a new record for {user_name}")

    else:
        print("There is a pre-existing record for Ben")
        print("Please use 'set' to update their record")


# **************************************************************************

def mainloop():
    user_action = input("What action would you like to take? ('help' for options): ")

    while user_action != "quit":
        match user_action:

            case 'help':
                help_menu()
                print('')
                user_action = input("What action would you like to take? ('help' for options): ")

            case 'add':
                add_menu()
                print('')
                user_action = input("What action would you like to take? ('help' for options): ")

    print("See ya later")


# **************************************************************************
mainloop()

# **************************************************************************