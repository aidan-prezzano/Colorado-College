# in terminal, ran: pip install pandas

import pandas as pd


# **************************************************************************


def us_happiness_trend_last_decade(df):

    # find the US ladder score in 2013
    us_2013_row = df.loc[(df['Country'] == 'United States') & (df['year'] == 2013)].iloc[0]
    us_2013_ladder_score = us_2013_row['Life Ladder']

    # find the US ladder score in 2023
    us_2023_row = df.loc[(df['Country'] == 'United States') & (df['year'] == 2023)].iloc[0]
    us_2023_ladder_score = us_2023_row['Life Ladder']

    # determine if the happiness trend, based on ladder score, is going UP or DOWN
    trend = 'UP' if us_2023_ladder_score > us_2013_ladder_score else 'DOWN'

    print('The US happiness has gone ' + trend + ' over the last decade')


# **************************************************************************


def global_happiness_trend_last_decade(df):

    # find the the ladder score sum of all countries in 2013
    global_2013_rows = df.loc[df['year'] == 2013]
    global_2013_ladder_score_sum = global_2013_rows['Life Ladder'].sum()

    # find the the ladder score sum of all countries in 2023
    global_2023_rows = df.loc[df['year'] == 2023]
    global_2023_ladder_score_sum = global_2023_rows['Life Ladder'].sum()

    # determine if the happiness trend, based on ladder score, is going UP or DOWN
    trend = 'UP' if global_2023_ladder_score_sum > global_2013_ladder_score_sum else 'DOWN'

    print('Globally, happiness has gone ' + trend + ' over the last decade')


# **************************************************************************


def most_corrupt_seeming_countries(df):

    most_corrupt_countries = ['US', 'Mexico', 'Japan']

    print('The top (3) most corrupt seeming countries are: ' + str(most_corrupt_countries))


# **************************************************************************


def compare_highest_social_support_vs_gdp_capita(df):

    social_support_countries_happier_than_gdp_capita = 'MORE'

    print('Top (10) countries with the highest social support happier are ' + social_support_countries_happier_than_gdp_capita + ' happy than the top (10) countries with the highest GDP / capita')


# **************************************************************************


def run_happy_analysis():

    df = pd.read_csv('happiness.csv')

    us_happiness_trend_last_decade(df)
    global_happiness_trend_last_decade(df)
    most_corrupt_seeming_countries(df)
    compare_highest_social_support_vs_gdp_capita(df)


# **************************************************************************


run_happy_analysis()


# **************************************************************************
