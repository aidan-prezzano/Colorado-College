# ************************************************************************** Help

# print the acceptable commands
def help():
    print('        \'add\': add a new student')
    print('        \'set\': update a student\'s score for an assignment')
    print('        \'display\': print out all records in the database')
    print('        \'dayavg\': view the average score for an assignment (across students)')
    print('        \'nameavg\': view the average score for a student (across assignments)')
    print('        \'quit\': exit the program')


# ************************************************************************** Add Student


# determine if a student exist in the records
def student_in_records(records, name):
    return False


# add a new student to the records with default scores
def add_new_student_to_records(records, name):
    records.append({'name': name, 'day0': 0, 'day1': 0, 'day2': 0})
    return records


# add a student to the records, as long as the student does not already exist
def add_student_record(records):
    name = input('What is the new student\'s name? ')
    if student_in_records(records, name):
        print('There is a pre-existing record for ' + name)
        print('Please use \'set\' to update their record')
    else:
        records = add_new_student_to_records(records, name)
    return records


# ************************************************************************** Display all Student Records


# display all student records
def display_student_records(records):
    if len(records) == 0:
        print('There are no student records')
        print('Please use \'add\' to add a student record')
    else:
        for record in records:
            print('Student record')
            print('        name: ' + record.get('name'))
            print('        day0: ' + str(record.get('day0')))
            print('        day1: ' + str(record.get('day1')))
            print('        day2: ' + str(record.get('day2')))


# **************************************************************************


student_records = []
help()
student_records = add_new_student_to_records(student_records, 'Charlie')
student_records = add_new_student_to_records(student_records, 'Aidan')
display_student_records(student_records)

# command = input('What action would you like to take? (\'help\' for options): ')
command = 'quit'
while command != 'quit':
    print('')
    match command:
        case 'add':
            student_records = add_student_record(student_records)
        case 'display':
            display_student_records(student_records)
        case 'help':
            help()
    command = input('\nWhat action would you like to take? (\'help\' for options): ')

print('\nSee ya later')


# **************************************************************************

