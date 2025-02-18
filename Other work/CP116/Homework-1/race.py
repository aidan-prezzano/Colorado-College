# **************************************************************************

TEST_MODE = True

TEST_SNACK_COORDINATES = '20,20'
TEST_YOUR_COORDINATES = '15,30'
TEST_FRIEND_COORDINATES = '25,25'

# **************************************************************************

def distance_between_coordinates(coordinate_1, coordinate_2):
    return pow(pow(float(coordinate_1[0]) - float(coordinate_2[0]), 2) + pow(float(coordinate_1[1]) - float(coordinate_2[1]), 2), 0.5)

# **************************************************************************

print('Enter location of')
print('        (1) the snacks,')
print('        (2) yourself, and')
print('        (3) your friend')
print('The format should be: x,y (no parenthesis, no spaces please!)')

snack_coordinates = TEST_SNACK_COORDINATES.split(',') if TEST_MODE else input('1st coordinates: ').split(',')
your_coordinates = TEST_YOUR_COORDINATES.split(',') if TEST_MODE else input('2nd coordinates: ').split(',')
friend_coordinates = TEST_FRIEND_COORDINATES.split(',') if TEST_MODE else input('3rd coordinates: ').split(',')

your_distance_to_snack = distance_between_coordinates(snack_coordinates, your_coordinates)
friend_distance_to_snack = distance_between_coordinates(snack_coordinates, friend_coordinates)
your_distance_to_snack_vs_friend = your_distance_to_snack / friend_distance_to_snack

print('You are at (' + str(float(your_coordinates[0])) + ',' + str(float(your_coordinates[1])) + '), your friend is at (' + str(float(friend_coordinates[0])) + ',' + str(float(friend_coordinates[1])) + '),')
print('and you are racing to the food at (' + str(float(snack_coordinates[0])) + ',' + str(float(snack_coordinates[1])) + ')!')

print('Your current distance to the food is ' + str(round(your_distance_to_snack, 2)) + '.')
print('Your friends distance to the food is ' + str(round(friend_distance_to_snack, 2)) + '.')
print('You are ' + str(round(your_distance_to_snack_vs_friend, 2)) + 'x as close as your friend. Run!')

# **************************************************************************