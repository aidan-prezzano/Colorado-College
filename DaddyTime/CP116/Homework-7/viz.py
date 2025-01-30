import matplotlib.pyplot as plt
import pandas as pd


# **************************************************************************


def relationship_between_sport_and_age_in_olympics(df):

    sport = 'Gymnastics'
    print('Studying how age impacts an athletes ability to medal in ' + sport + '\n')

    # find all athletes for the sport
    athletes_in_sport = df[(df['Sport'] == sport)]
    print('There have been ' + str(len(athletes_in_sport)) + ' athletes and who have won a medal in ' + sport)

    # group the athletes by age
    nbr_athletes_by_age = athletes_in_sport.groupby(['Age']).size()
    print(nbr_athletes_by_age)

    for xyz in enumerate(nbr_athletes_by_age):
        print(xyz)



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

    #how_has_happiness_changed_past_15_years(df_happiness)

    print('\n------------------------------------------------------------\n')

    #relationship_between_wealth_generosity_and_happiness(df_happiness)

    print('\n------------------------------------------------------------')


# **************************************************************************


run_viz()


# **************************************************************************