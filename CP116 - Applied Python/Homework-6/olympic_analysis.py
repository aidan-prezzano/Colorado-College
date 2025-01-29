
import pandas as pd


# **************************************************************************

def youngest_olympian_to__receive_medal(df):

    youngest = df.loc[df['Age'].idxmin(), ['Name', 'Age', 'Sport', 'Year']]

    athlete = youngest['Name']
    sport = youngest['Sport']
    year = youngest['Year']
    age = youngest['Age']

    print('Youngest olympian to receive a medal was ' + athlete + '. The medal was in ' + sport + ', in the year ' + str(year) + ' at '+ str(age))


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

    silver_medals = df[df['Medals'] == 'Silver']

    silver_counts = silver_medals['Name'].value_counts()

    most_silver_medals = silver_counts.idxmax()

    top_count = silver_counts.max()

    print(most_silver_medals + ' has won the most silver medals with ' + str(top_count) + ' medals.')



# **************************************************************************


def unique_athletes_to_win_a_medal_after_40(df):

    athletes_above_40 = df[df['Age'] > 40]

    unique_values = athletes_above_40["Name"].unique()
    nbr_athletes = len(unique_values)

    print('The number of (unique) athletes who have won a medal after the age of 40 is: ' + str(nbr_athletes))

# **************************************************************************


def run_olympic_analysis():

    df = pd.read_csv('olympic_data.csv')

    youngest_olympian_to__receive_medal(df)
    city_with_lowest_nbr_medals_awarded(df)
    who_won_most_silver_medals(df)
    unique_athletes_to_win_a_medal_after_40(df)



# **************************************************************************


run_olympic_analysis()


# **************************************************************************

