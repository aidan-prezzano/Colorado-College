from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

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
    print('There have been ' + str(
        len(female_athletes_in_sport)) + ' female athletes and who have won a medal in ' + sport)
    female_athletes_by_age = female_athletes_in_sport.groupby(['Age']).size()

    # find all male athletes for the sport
    # group the male athletes by age
    male_athletes_in_sport = df[(df['Sport'] == sport) & (df['Sex'] == 'M')]
    print('There have been ' + str(len(male_athletes_in_sport)) + ' male athletes and who have won a medal in ' + sport)
    male_athletes_by_age = male_athletes_in_sport.groupby(['Age']).size()

    # show the data found while making a title and showing different hues for M and F
    sns.lineplot(female_athletes_by_age, color='pink', label='Female')
    sns.lineplot(male_athletes_by_age, color='blue', label='Male')
    plt.title("The Medals per age in Gymnastics")
    plt.ylabel('# Medals')
    plt.show()

    # I choose lineplot because comparing age is similar to comparing something over time. I think the line plot looks smooth
    # for this type of data. I also added in title's and hues for M and F so the reader understands fully what type of data is being presented. As you can see
    # Gymnastics athletes can start very early, espically women. Women actually win most of their medals before the age of 20 as the climax
    # stands around 17 years old. As for the men, they can win in their late teens but their twilight years peak around the age of 25 and rapidly decline after. It is also important
    # to note that women have far less longevity than men. No women has won a medal past the age of 35 while there are many men who have, even reaching
    # the age of 45.



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

    # As you can see, the happiness of Canada and the United States has declined over the last 15 years. I would say that it was a more
    # steady decline for both countries during years 2009-2016. However, both countries had some hope during the year 2012. During years
    # 2016-2020, United States overall increased their happiness while Canada lost theirs at a near linear path until the year 2023. It is also
    # important to note that in 2009 the US started near 7.2 while Canada started around 7.5. Looking at 2023 the US are around 6.5 and Canada is
    # around 6.8. This means that both countries have lost around .7 happiness points over the last 15 years. I choose a Line plot again because it does
    # well evaluating values over time. I then chose different hues for the countries to make the data clear. I included a tile, and labels for the
    # axsises to make the graph easy to read.

# **************************************************************************


def relationship_between_wealth_generosity_and_happiness(df):

    # see what the life ladder score is as generosity goes up
    #generosity_sorted = df.sort_values(by='Generosity', ascending=False)

    generosity_rows_happiness = df[['Generosity', 'Life Ladder']].sort_values(by='Generosity', ascending=False).dropna(subset=['Generosity'])



    print(generosity_rows_happiness)
    #wealth_rows = df['Log GDP per capita']


    #generosity_rows_happiness = generosity_rows['Life Ladder']
    # see what the life ladder score is when wealth goes up
    # maybe see when the two of them combined goes up



    print('relationship_between_wealth_generosity_and_happiness')


# **************************************************************************


def run_viz():

    df_happiness = pd.read_csv('happiness.csv')
    df_olympic = pd.read_csv('olympic_data.csv')

    print('------------------------------------------------------------\n')


    #relationship_between_sport_and_age_in_olympics(df_olympic)

    print('\n------------------------------------------------------------\n')

    #how_has_happiness_changed_past_15_years(df_happiness)


    print('\n------------------------------------------------------------\n')

    relationship_between_wealth_generosity_and_happiness(df_happiness)

    #print('\n------------------------------------------------------------')


# **************************************************************************


run_viz()


# **************************************************************************