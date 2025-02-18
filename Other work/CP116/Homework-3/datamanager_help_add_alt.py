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


# add a student to the records
# if the student exists in the list of records, return a dictionary with success as False
# else, add the student to the list of records with default assignment scores of 0,
# and return a dictionary with success as False and the the updated list of student records
def add_student_record(student_records, name):
    for student_record in student_records:
        if student_record.get('name') == name:
            return False
    new_student_record = {'name': name, 'day0': 0, 'day1': 0, 'day2': 0}
    student_records.append(new_student_record)
    return True


# **************************************************************************


def run_data_manager():
    student_records = []

    command = input('What action would you like to take? (\'help\' for options): ')
    while command != 'quit':
        print('')
        match command:
            case 'add':
                name = input('What is the new student\'s name? ')
                if add_student_record(student_records, name):
                    print('Successfully added a new record for ' + name)
                else:
                    print('There is a pre-existing record for ' + name)
                    print('Please use \'set\' to update their record')
            case 'help':
                help()
        command = input('\nWhat action would you like to take? (\'help\' for options): ')

    print('\nSee ya later')


# **************************************************************************


run_data_manager()


# **************************************************************************
