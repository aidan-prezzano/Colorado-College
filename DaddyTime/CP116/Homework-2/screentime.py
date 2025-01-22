# **************************************************************************

def find_all_names(min_lines):
    return ['Elsinore.', 'Ber.', 'Fran.', 'Hor.', 'Mar.', 'King.', 'Laer.', 'Pol.', 'Ham.', 'Queen.', 'Both.', 'All.', 'Oph.', 'Exeunt.', 'Ghost.', 'Rey.', 'Ros.', 'Guil.', '1.', 'Capt.', 'Clown.', 'Other.', 'Osr.']

# **************************************************************************

def find_nbr_lines_for_name(name):
    return 45

# **************************************************************************

print('I just finished reading Hamlet, and can tell you how many lines each character spoke!')
print('Please input one of the three following commands:')
print('        "names": display all character names')
print('        "exit":  terminates the program')
print('        "{name}": display how many lines were spoken by that character')
print('')

names = find_all_names(5)
names_str = str(names).replace('[', '').replace(']', '').replace('\'', '')

command = input('Enter command: ')
while command != 'exit':
    if command == 'names':
        print('Here are the valid character names (with > 5 lines): ' + names_str)
    elif command == 'exit':
        print('Okay, shutting down.')
    else:
        name = command
        if name in names:
            nbr_lines = find_nbr_lines_for_name(name)
            print('Based on my count, ' + name + ' had ' + str(nbr_lines) + ' lines.')
        else:
            print(name + ' is not a valid character name')
    print('')
    command = input('Enter command: ')

# **************************************************************************