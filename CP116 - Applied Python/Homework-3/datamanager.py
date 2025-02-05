from pandas.core.computation.ops import isnumeric


def help_menu():

    # Neatly prints out all valid user inputs and what they do
    print("'add': add a new student")
    print("'set': update a student's score for an assignment")
    print("'display': print out all records in the database")
    print("'dayavg': view the average score for an assignment (across students)")
    print("'nameavg': view the average score for a student (across assignments)")
    print("'quit': exit the program")


# *********************************************************************************************

def student_in_records(student_records, name):
    for student_record in student_records:
        if student_record.get('name') == name:
            return True
    return False

# *********************************************************************************************

def add_student_record(student_records):
    name = input('What is the new student\'s name? ')
    if student_in_records(student_records, name):
        print('There is a pre-existing record for ' + name)
        print('Please use \'set\' to update their record')
    else:
        student_records.append({'name': name, 'day0': 0, 'day1': 0, 'day2': 0})
        print('Successfully added a new record for ' + name)
    return student_records

# *********************************************************************************************
# update a students record
def update_student_record(student_records, name, assignment_name, assignment_score):
    for idx, student_record in enumerate(student_records):
        if student_record.get('name') == name:
            student_record.update({assignment_name: float(assignment_score)})
            student_records[idx] = student_record
    return student_records
# *********************************************************************************************
# set a students record
def set_student_records(student_records):
    name = input("What is the new students name? ")
    if student_in_records(student_records, name):
        print('There is NOT a pre-existing record for ' + name)
        print('Please use the add command to add a new student')
    else:
        assignment_name = input("What is the new assignment's name? ")
        while assignment_name not in ['day0', 'day1', 'day2']:
            print("Assignment name must be 'day0', 'day1', or 'day2' ")
        assignment_score = input('What is the students score for ' + assignment_name + '? ')
        while assignment_score.isnumeric():
            print("Assignment score must be numeric")
        return update_student_record(student_records, name, assignment_name, assignment_score)

# *********************************************************************************************
def display_student_records(student_records):
    if len(student_records) == 0:
        print("There are no records available")
        print('Please use the add command to add a new student')
    else:
        for student_record in student_records:
            print('Student record')
            print('        name: ' + student_record.get('name'))
            print('        day0: ' + str(student_record.get('day0')))
            print('        day1: ' + str(student_record.get('day1')))
            print('        day2: ' + str(student_record.get('day2')))


def run_data_manager():

    student_records = []

    command = input('What action would you like to take? (\'help\' for options): ')
    while command != 'quit':
        print('')
        match command:
            case 'help':
                help_menu()
            case 'add':
                add_student_record(student_records)
            case 'set':
                set_student_records(student_records)
            case 'display':
                display_student_records(student_records)

        command = input('\nWhat action would you like to take? (\'help\' for options): ')


run_data_manager()


