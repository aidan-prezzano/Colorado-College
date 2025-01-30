import pandas as pd


# **************************************************************************


def relationship_between_sport_and_age_in_olympics(df):

    print('relationship_between_sport_and_age_in_olympics')


# **************************************************************************


def how_has_happiness_changed_past_15_years(df):

    print('how_has_happiness_changed_past_15_years')


# **************************************************************************


def relationship_between_wealth_generosity_and_happiness(df):

    print('relationship_between_wealth_generosity_and_happiness')


# **************************************************************************


def run_viz():

    df_happiness = pd.read_csv('happiness.csv')
    df_olympic = pd.read_csv('olympic_data.csv')

    print('------------------------------------------------------------\n')

    relationship_between_sport_and_age_in_olympics(df_olympic)

    print('\n------------------------------------------------------------\n')

    how_has_happiness_changed_past_15_years(df_happiness)

    print('\n------------------------------------------------------------\n')

    relationship_between_wealth_generosity_and_happiness(df_happiness)

    print('\n------------------------------------------------------------')


# **************************************************************************


run_viz()


# **************************************************************************