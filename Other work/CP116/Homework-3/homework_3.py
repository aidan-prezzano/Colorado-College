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
def student_in_records(student_records, name):
    for student_record in student_records:
        if student_record.get('name') == name:
            return True
    return False
# **************************************************************************
def add_student_record(student_records):
    name = input('What is the new student\'s name? ')
    if student_in_records(student_records, name):
        print('There is a pre-existing record for ' + name)
        print('Please use \'set\' to update their record')
    else:
        student_records.append({'name': name, 'day0': 0, 'day1': 0, 'day2': 0})
        print('Successfully added a new record for ' + name)
    return student_records




def add_menu(student_records):
    student_name = input("what is the new students name?")
    if student_name not in student_names:
        student_names.append(student_name)
        print(f"Successfully added a new record for {student_name}")

    else:
        print("There is a pre-existing record for Ben")
        print("Please use 'set' to update their record")

# **************************************************************************



def mainloop():
    student_records = []

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