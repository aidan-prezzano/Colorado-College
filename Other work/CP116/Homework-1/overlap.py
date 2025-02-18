# **************************************************************************

TEST_MODE = False

TEST_FIRST_LIST_OF_CLASSES = 'cp115,cp116,cp122,cp222'
TEST_SECOND_LIST_OF_CLASSES = 'cp116,cp222,cp274'

# **************************************************************************

print('This calculator will ask for two lists of classes.')
print('Please enter them separated with commas but no extra spaces!\n')

first_list_of_classes = TEST_FIRST_LIST_OF_CLASSES.split(',') if TEST_MODE else input('Enter the 1st list of classes: ').split(',')
second_list_of_classes = TEST_SECOND_LIST_OF_CLASSES.split(',') if TEST_MODE else input('Enter the 2nd list of classes: ').split(',')

common_classes = list(set(first_list_of_classes).intersection(second_list_of_classes))

print('The two lists have ' + str(len(common_classes)) + ' entries in common.')
print('They are: ', end='')
for idx, class_name in enumerate(common_classes):
    print(class_name, end='')
    print(', ', end='') if idx < (len(common_classes) - 1) else print('')

# **************************************************************************