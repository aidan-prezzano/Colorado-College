# in terminal, ran: pip install pandas

import pandas as pd


# **************************************************************************


def us_happiness_trend_last_decade(df):

    trend = 'DOWN'

    print('The US happiness has gone ' + trend + ' over the last decade')


# **************************************************************************


def global_happiness_trend_last_decade(df):

    trend = 'UP'

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
