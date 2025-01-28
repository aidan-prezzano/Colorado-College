# in terminal, ran: pip install pandas

import pandas


# **************************************************************************

def youngest_olympian_to__receive_medal(data_frame):

    athelete = 'Aidan Prezzano'
    sport = 'Soccer'
    year = 2020

    print('Youngest olympian to receive a medal was ' + athelete + '. The medal was in ' + sport + ', in the year ' + str(year) + '.')


# **************************************************************************


def city_with_lowest_nbr_medals_awarded(data_frame):

    city = 'Rhinebeck'

    print('The lowest number of awarded medals took place in ' + city + '.')


# **************************************************************************


def who_won_most_silver_medals(data_frame):

    athelete = 'Aidan Prezzano'

    print(athelete + ' has won the most silver medals.')


# **************************************************************************


def unique_athletes_to_win_a_medal_after_40(data_frame):

    nbr_athletes = 99

    print('The number of (unique) athletes who have won a medal after the age of 40 is: ' + str(nbr_athletes))


# **************************************************************************


def run_olympic_analysis():

    data_frame = pandas.read_csv('olympic_data.csv')

    youngest_olympian_to__receive_medal(data_frame)
    city_with_lowest_nbr_medals_awarded(data_frame)
    who_won_most_silver_medals(data_frame)
    unique_athletes_to_win_a_medal_after_40(data_frame)


# **************************************************************************


run_olympic_analysis()


# **************************************************************************

