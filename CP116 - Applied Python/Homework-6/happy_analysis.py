# in terminal, ran: pip install pandas
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns


# **************************************************************************


def us_happiness_trend_last_decade(df):

    sns.lineplot(data=df, x='year', y='Life Ladder')
    #plt.show()

    #year_2013_US = df[df['year'] == '2013'] & df[df['Country'] == 'United States']
    #print(year_2013_US['Life Ladder'])

    us_2013_row = df.loc[(df['Country'] == 'United States') & (df['year'] == 2013)].iloc[0]
    us_2013_ladder_score = us_2013_row['Life Ladder']

    us_2023_row = df.loc[(df['Country'] == 'United States') & (df['year'] == 2023)].iloc[0]
    us_2023_ladder_score = us_2023_row['Life Ladder']

    if us_2013_ladder_score > us_2023_ladder_score:
        trend = 'Down'
    else:
        trend = 'Up'

    print('The US happiness has gone ' + trend + ' over the last decade')


# **************************************************************************


def global_happiness_trend_last_decade(df):

    global_2013_row = df.loc[df['year'] == 2013]
    global_2013_ladder_score = global_2013_row['Life Ladder'].mean()

    global_2023_row = df.loc[df['year'] == 2023]
    global_2023_ladder_score = global_2023_row['Life Ladder'].mean()

    if global_2013_ladder_score > global_2023_ladder_score:
        trend = 'Down'
    else:
        trend = 'Up'

    print('Globally, happiness has gone ' + trend + ' over the last decade')


# **************************************************************************


def most_corrupt_seeming_countries(df):
    # Filter for the latest year available
    corrupt_countries = df[df["year"] == 2023]

    # Group by country and take the average corruption perception score
    avg_corruption = corrupt_countries.groupby("Country")["Perceptions of corruption"].mean()

    # Sort in descending order to get the most corrupt-seeming countries
    most_corrupt = avg_corruption.sort_values(ascending=False)

    # Display the top 3 most corrupt-seeming countries
    most_corrupt_countries = [most_corrupt.head(3)]

    print('The top (3) most corrupt seeming countries in 2023 are: ' + str(most_corrupt_countries))


# **************************************************************************


def compare_highest_social_support_vs_gdp_capita(df):

    # # Filter for the latest year available
    year_of_study = df[df['year'] == 2023]

    # find top 10 countries based on social support
    # then find the the ladder score sum of these 10 countries
    top_10_social_support = year_of_study.nlargest(10, 'Social support')
    top_10_social_support_ladder_score_sum = top_10_social_support['Life Ladder'].sum()

    # find top 10 countries based on gdp per capita
    # then find the the ladder score sum of these 10 countries
    top_10_gdp_per_capita = year_of_study.nlargest(10, 'Log GDP per capita')
    top_10_gdp_per_capita_ladder_score_sum = top_10_gdp_per_capita['Life Ladder'].sum()

    # determine if top 10 social support countries are happier than the top 10 gdp per capita
    social_support_countries_happier_than_gdp_capita = 'MORE' if top_10_social_support_ladder_score_sum > top_10_gdp_per_capita_ladder_score_sum else 'LESS'

    print('Top (10) countries with the highest social support happier are ' + social_support_countries_happier_than_gdp_capita + ' happy than the top (10) countries with the highest GDP / capita')


# **************************************************************************


def run_happy_analysis():

    df = pd.read_csv('happiness.csv')

    us_happiness_trend_last_decade(df)
    print('***********************************')
    global_happiness_trend_last_decade(df)
    print('***********************************')
    most_corrupt_seeming_countries(df)
    print('***********************************')
    compare_highest_social_support_vs_gdp_capita(df)


# **************************************************************************


run_happy_analysis()


# **************************************************************************
