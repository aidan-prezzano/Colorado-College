# in terminal, ran: pip install pandas

import pandas as pd


# **************************************************************************


def youngest_olympian_to_receive_medal(df):

    # find the minimum age within the dataset
    # then find the row, at this age
    min_age = df['Age'].min()
    row = df.loc[df['Age'] == min_age].iloc[0]

    # from this row get the athletes name, sport, and year that won the medal
    athlete = row['Name']
    sport = row['Sport']
    year = row['Year']

    print('Youngest olympian to receive a medal was ' + athlete + '. The medal was in ' + sport + ', in the year ' + str(year) + '.')


# **************************************************************************


def city_with_lowest_nbr_medals_awarded(df):

    # group the dataset by event (year and season)
    # then find the row with the fewest entries - with the least amount of medals
    year_season_rows = df.groupby(['Year', 'Season']).size()
    row = year_season_rows.sort_values(ascending=True).index[0]

    # from the row get the event year and season
    event_year = row[0]
    event_season = row[1]

    print('The lowest number of awarded medals took place in the ' + event_season + ' of ' + str(event_year) + '.')


# **************************************************************************


def who_won_most_silver_medals(df):

    # find all rows that have a silver medal
    # then with these rows, order the athletes by count and get the athlete who has the most
    silver_medal_rows = df[df['Medals'] == 'Silver']
    athlete = silver_medal_rows['Name'].value_counts().index[0]

    print(athlete + ' has won the most silver medals.')


# **************************************************************************


def unique_athletes_to_win_a_medal_after_40(df):

    # find all rows that have an age greater than 40
    # then with these rows, find the unique athletes
    after_40_rows = df[df['Age'] > 40]
    unique_athletes_after_40 = after_40_rows['Name'].unique()

    print('The number of (unique) athletes who have won a medal after the age of 40 is: ' + str(len(unique_athletes_after_40)))


# **************************************************************************


def run_olympic_analysis():

    df = pd.read_csv('olympic_data.csv')

    youngest_olympian_to_receive_medal(df)
    city_with_lowest_nbr_medals_awarded(df)
    who_won_most_silver_medals(df)
    unique_athletes_to_win_a_medal_after_40(df)


# **************************************************************************


run_olympic_analysis()


# **************************************************************************

