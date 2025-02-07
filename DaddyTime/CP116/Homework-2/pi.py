# **************************************************************************

TEST_MODE = False

TEST_NBR_TERMS = 1_000_000

# **************************************************************************

def calculate_pi_approximation(nbr_terms):
    one_fourth_pi = 0
    add_or_subtract = 'ADD'
    for idx in range(1, (nbr_terms + 1)):
        if add_or_subtract == 'ADD':
            one_fourth_pi = one_fourth_pi + (1 / ((idx * 2) - 1))
            add_or_subtract = 'SUBTRACT'
        else:
            one_fourth_pi = one_fourth_pi - (1 / ((idx * 2) - 1))
            add_or_subtract = 'ADD'
    return one_fourth_pi * 4

# **************************************************************************

print('Let\'s calculate pi! We can use the Leibniz formula, which sums up a bunch of smaller and smaller terms. This sum will eventually converge to the true value of pi... as long as you never stop calculating ;)')

nbr_terms = TEST_NBR_TERMS if TEST_MODE else int(input('How many terms would you like? '))

pi_approximation = calculate_pi_approximation(nbr_terms)

print('After summing the first ' + str(nbr_terms) + ' terms, your pi approximation is: ' + str(round(pi_approximation,16)))

# **************************************************************************