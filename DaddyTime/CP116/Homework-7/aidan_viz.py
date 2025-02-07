from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

# **************************************************************************


def relationship_between_sport_and_age_in_olympics(df):
    sport = 'Gymnastics'

    # only lines concerning gymnastics
    gymnastic_contestants = df[df["Sport"] == sport]

    # find medal winners of gymnastics
    gymnastic_age = gymnastic_contestants.groupby('Age').size()
    print(gymnastic_age)


    # plot the data by age, I choose lineplot because age is similar to comparing something over time. I think the line plot looks smooth
    # for this type of data. I also added in title's so the reader understands fully what type of data is being presented. As you can see
    # Gymnastics athletes can start very early, many having metals won at only 15 years old! The athletes reach their peak preformance around
    # the age 24- 25 and then start to decline as they get older. I was still suprised that there were even few people winning medals above
    # the age 35.
    sns.lineplot(gymnastic_age)
    plt.title("The Medals per age in Gymnastics")
    plt.ylabel('# Medals')
    plt.show()


    #print('relationship_between_sport_and_age_in_olympics')


# **************************************************************************


def how_has_happiness_changed_past_15_years(df):

    country_1 = 'United States'

    us_rows = df[df["Country"] == country_1]

    US_happiness = us_rows.groupby('Life Ladder')['year'].max()

    US_happiness_sorted = US_happiness.sort_values(ascending=True)

    US_happiness_sorted_last_15 = [US_happiness_sorted.head(15)]
    print(US_happiness_sorted_last_15)

    sns.lineplot(US_happiness_sorted_last_15, x=US_happiness_sorted_last_15['year'])
    plt.show()

    print('how_has_happiness_changed_past_15_years')


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

    #print('\n------------------------------------------------------------')


# **************************************************************************


run_viz()


# **************************************************************************