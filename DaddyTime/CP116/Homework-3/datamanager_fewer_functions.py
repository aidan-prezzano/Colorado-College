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


# ************************************************************************** Set a Student Record


# update a students record
def update_student_record(student_records, name, assignment_name, assignment_score):
    for idx, student_record in enumerate(student_records):
        if student_record.get('name') == name:
            student_record.update({assignment_name: float(assignment_score)})
            student_records[idx] = student_record
    return student_records


# set a students record
def set_student_record(student_records):
    name = input('What is the new student\'s name? ')
    if not student_in_records(student_records, name):
        print('There is NOT a pre-existing record for ' + name)
        print('Please use \'add\' to add their student record')
        return student_records
    else:
        assignment_name = input('What is the assignment name? ')
        while assignment_name not in ['day0', 'day1', 'day2']:
            print('Acceptable assignment names are: \'day0\', \'day1\', \'day2\'')
            assignment_name = input('What is the assignment name? ')
        assignment_score = input('What is their score? ')
        while not assignment_score.isnumeric():
            print('The assignment score must be numeric')
            assignment_score = input('What is their score? ')
        return update_student_record(student_records, name, assignment_name, assignment_score)


# ************************************************************************** Display all Student Records


# display all student records
def display_student_records(student_records):
    if len(student_records) == 0:
        print('There are no student records')
        print('Please use \'add\' to add a student record')
    else:
        for student_record in student_records:
            print('Student record')
            print('        name: ' + student_record.get('name'))
            print('        day0: ' + str(student_record.get('day0')))
            print('        day1: ' + str(student_record.get('day1')))
            print('        day2: ' + str(student_record.get('day2')))


# ************************************************************************** Display a Students Average


# calculate a students average assignment score
def calculate_student_average(student_record):
    return (student_record.get('day0') + student_record.get('day1') + student_record.get('day2')) / 3


# display a students average assignment score
def display_student_average(student_records):
    name = input('Whose scores would you like to average?: ')
    if not student_in_records(student_records, name):
        print('There is NOT a pre-existing record for ' + name)
        print('Please use \'add\' to add their student record')
    else:
        for student_record in student_records:
            if student_record.get('name') == name:
                print('The average score for ' + name + ' is ' + str(round(calculate_student_average(student_record), 2)))


# ************************************************************************** Display a Day Average


# calculate the day average assignment score
def calculate_day_average(student_records, assignment_name):
    assignment_score = 0
    for student_record in student_records:
        assignment_score += student_record.get(assignment_name)
    return assignment_score / len(student_records)


# display the day average assignment score
def display_day_average(student_records):
    if len(student_records) == 0:
        print('There are no student records')
        print('Please use \'add\' to add a student record')
        return
    assignment_name = input('Which assignment would you like to average?: ')
    while assignment_name not in ['day0', 'day1', 'day2']:
        print('Acceptable assignment names are: \'day0\', \'day1\', \'day2\'')
        assignment_name = input('What is the assignment name? ')
    print('The average score for ' + assignment_name + ' is ' + str(round(calculate_day_average(student_records, assignment_name), 2)))


# **************************************************************************


def run_data_manager():

    student_records = []

    command = input('What action would you like to take? (\'help\' for options): ')
    while command != 'quit':
        print('')
        match command:
            case 'add':
                student_records = add_student_record(student_records)
            case 'dayavg':
                display_day_average(student_records)
            case 'display':
                display_student_records(student_records)
            case 'help':
                help()
            case 'nameavg':
                display_student_average(student_records)
            case 'set':
                student_records = set_student_record(student_records)
        command = input('\nWhat action would you like to take? (\'help\' for options): ')

    print('\nSee ya later')


# **************************************************************************


run_data_manager()


# **************************************************************************

