
import pandas as pd


# **************************************************************************

def youngest_olympian_to__receive_medal(df):

    youngest = df.loc[df['Age'].idxmin(), ['Name', 'Age', 'Sport', 'Year']]
    print(youngest)

    athelete = youngest['Name']
    sport = youngest['Sport']
    year = youngest['Year']
    age = youngest['Age']

    print('Youngest olympian to receive a medal was ' + athelete + '. The medal was in ' + sport + ', in the year ' + str(year) + ' at '+ str(age))


# **************************************************************************


def city_with_lowest_nbr_medals_awarded(df):

    city = 'Rhinebeck'

    print('The lowest number of awarded medals took place in ' + city + '.')


# **************************************************************************


def who_won_most_silver_medals(df):

    athelete = 'Aidan Prezzano'

    print(athelete + ' has won the most silver medals.')


# **************************************************************************


def unique_athletes_to_win_a_medal_after_40(df):

    nbr_athletes = 99

    print('The number of (unique) athletes who have won a medal after the age of 40 is: ' + str(nbr_athletes))


# **************************************************************************


def run_olympic_analysis():

    df = pd.read_csv('olympic_data.csv')

    youngest_olympian_to__receive_medal(df)
    #city_with_lowest_nbr_medals_awarded(df)
    #who_won_most_silver_medals(df)
    #unique_athletes_to_win_a_medal_after_40(df)


# **************************************************************************


run_olympic_analysis()


# **************************************************************************

