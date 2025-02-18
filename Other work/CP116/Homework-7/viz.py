import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# **************************************************************************


def relationship_between_sport_and_age_in_olympics(df):

    sport = 'Gymnastics'
    print('Studying how age impacts an athletes ability to medal in ' + sport + '\n')

    # find all athletes for the sport
    # group the athletes by age
    athletes_in_sport = df[(df['Sport'] == sport)]
    print('There have been ' + str(len(athletes_in_sport)) + ' athletes and who have won a medal in ' + sport)
    athletes_by_age = athletes_in_sport.groupby(['Age']).size()

    # find all female athletes for the sport
    # group the female athletes by age
    female_athletes_in_sport = df[(df['Sport'] == sport) & (df['Sex'] == 'F')]
    print('There have been ' + str(len(female_athletes_in_sport)) + ' female athletes and who have won a medal in ' + sport)
    female_athletes_by_age = female_athletes_in_sport.groupby(['Age']).size()

    # find all male athletes for the sport
    # group the male athletes by age
    male_athletes_in_sport = df[(df['Sport'] == sport) & (df['Sex'] == 'M')]
    print('There have been ' + str(len(male_athletes_in_sport)) + ' male athletes and who have won a medal in ' + sport)
    male_athletes_by_age = male_athletes_in_sport.groupby(['Age']).size()

    #sns.lineplot(athletes_by_age)
    sns.lineplot(female_athletes_by_age, color='pink', label='Female')
    sns.lineplot(male_athletes_by_age, color='blue', label='Male')
    plt.title('Medals by Age for ' + sport)
    plt.ylabel('# Medals')
    plt.show()


# **************************************************************************


def how_has_happiness_changed_past_15_years(df):

    canada_rows = df[(df['Country'] == 'Canada')].tail(15)
    us_rows = df[(df['Country'] == 'United States')].tail(15)

    sns.lineplot(canada_rows, x=canada_rows['year'], y=canada_rows['Life Ladder'], color='green', label='Canada')
    sns.lineplot(us_rows, x=us_rows['year'], y=us_rows['Life Ladder'], color='red', label='United States')
    plt.title('Happiness by Country - Past 15 Years')
    plt.xlabel('Year')
    plt.ylabel('Happiness (Life Ladder)')
    plt.show()

# **************************************************************************


def relationship_between_wealth_generosity_and_happiness(df):

    print('relationship_between_wealth_generosity_and_happiness')


# **************************************************************************


def run_viz():

    df_happiness = pd.read_csv('happiness.csv')
    df_olympic = pd.read_csv('olympic_data.csv')

    print('------------------------------------------------------------\n')

    #relationship_between_sport_and_age_in_olympics(df_olympic)

    print('\n------------------------------------------------------------\n')

    how_has_happiness_changed_past_15_years(df_happiness)

    print('\n------------------------------------------------------------\n')

    #relationship_between_wealth_generosity_and_happiness(df_happiness)

    print('\n------------------------------------------------------------')


# **************************************************************************


run_viz()


# **************************************************************************