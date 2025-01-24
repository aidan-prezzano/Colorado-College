# ************************************************************************** Help


# print the acceptable commands
def help():
    print('        \'add\': add a new student')
    print('        \'set\': update a student\'s score for an assignment')
    print('        \'display\': print out all records in the database')
    print('        \'dayavg\': view the average score for an assignment (across students)')
    print('        \'nameavg\': view the average score for a student (across assignments)')
    print('        \'quit\': exit the program')


# ************************************************************************** Add a Student


# determine if a student exist in the records
def student_in_records(student_records, name):
    for student_record in student_records:
        if student_record.get('name') == name:
            return True
    return False


# add a student to the records, as long as the student does not already exist
def add_student_record(student_records):
    name = input('What is the new student\'s name? ')
    if student_in_records(student_records, name):
        print('There is a pre-existing record for ' + name)
        print('Please use \'set\' to update their record')
    else:
        student_records.append({'name': name, 'day0': 0, 'day1': 0, 'day2': 0})
        print('Successfully added a new record for ' + name)
    return student_records


# **************************************************************************


def run_data_manager():

    student_records = []

    command = input('What action would you like to take? (\'help\' for options): ')
    while command != 'quit':
        print('')
        match command:
            case 'add':
                student_records = add_student_record(student_records)
            case 'help':
                help()
        command = input('\nWhat action would you like to take? (\'help\' for options): ')

    print('\nSee ya later')


# **************************************************************************


run_data_manager()


# **************************************************************************

