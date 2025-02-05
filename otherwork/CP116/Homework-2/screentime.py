# **************************************************************************


# determine if the line is a spoken line
# this is true if the first word ends in a '.'
def is_spoken_line(line):
    return line.strip().partition(' ')[0].endswith('.')


# find the name who spoke the line,
# which is the first word
def spoken_line_name(line):
    return line.strip().partition(' ')[0]


# determine if the name exists in the list
def does_name_exist_in_list(names_with_nbr_lines, line_name):
    for name_with_nbr_lines in names_with_nbr_lines:
        if line_name == name_with_nbr_lines[0]:
            return True
    return False


# add a line to a name
# if the name does not exist in the list, add the name with having one line
# if the name does exist in the list, increment the number of lines spoken by the name
def add_line_to_name(names_with_nbr_lines, line_name):
    if does_name_exist_in_list(names_with_nbr_lines, line_name):
        for idx, name_with_nbr_lines in enumerate(names_with_nbr_lines):
            if line_name == name_with_nbr_lines[0]:
                names_with_nbr_lines[idx] = [line_name, (name_with_nbr_lines[1] + 1)]
    else:
        names_with_nbr_lines.append([line_name, 1])
    return names_with_nbr_lines


# find all names with any number of lines
def find_all_names_with_any_nbr_lines():
    names_with_nbr_lines = []
    hamlet_file = open('hamlet.txt', 'r')
    for line in hamlet_file:
        if is_spoken_line(line):
            line_name = spoken_line_name(line)
            names_with_nbr_lines = add_line_to_name(names_with_nbr_lines, line_name)
    hamlet_file.close()
    return names_with_nbr_lines


# find all names that have a minimum number of lines
def find_all_names_with_min_nbr_lines(names_with_nbr_lines, min_nbr_lines):
    names_with_min_nbr_lines = []
    for name_with_nbr_lines in names_with_nbr_lines:
        if name_with_nbr_lines[1] >= min_nbr_lines:
            names_with_min_nbr_lines.append(name_with_nbr_lines[0])
    return names_with_min_nbr_lines


# **************************************************************************


# find the number if lines, for a name
def find_nbr_lines_for_name(names_with_nbr_lines, name_to_find):
    for name_with_nbr_lines in names_with_nbr_lines:
        if name_to_find == name_with_nbr_lines[0]:
            return name_with_nbr_lines[1]
    return -1


# **************************************************************************


print('I just finished reading Hamlet, and can tell you how many lines each character spoke!')
print('Please input one of the three following commands:')
print('        "names": display all character names')
print('        "exit":  terminates the program')
print('        "{name}": display how many lines were spoken by that character')
print('')

# find all names with any number of lines
names_with_any_nbr_lines = find_all_names_with_any_nbr_lines()

# from the list of all names with any number of lines, find those with the minimum number of lines
# then make it look pretty
names = find_all_names_with_min_nbr_lines(names_with_any_nbr_lines, 5)
names_str = str(names).replace('[', '').replace(']', '').replace('\'', '')

command = input('Enter command: ')
while command != 'exit':
    if command == 'names':
        print('Here are the valid character names (with > 5 lines): ' + names_str)
    else:
        name = command
        if name in names:
            nbr_lines = find_nbr_lines_for_name(names_with_any_nbr_lines, name)
            print('Based on my count, ' + name + ' had ' + str(nbr_lines) + ' lines.')
        else:
            print(name + ' is not a valid character name')
    print('')
    command = input('Enter command: ')

print('Okay, shutting down.')

# **************************************************************************

