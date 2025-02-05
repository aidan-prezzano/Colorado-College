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

    # get each row of generosity and wealth and compare and sort the data from highest to lowest
    generosity_rows = df[['Generosity', 'Life Ladder']].sort_values(by='Generosity', ascending=False).dropna(subset=['Generosity'])
    wealth_rows = df[['Log GDP per capita', 'Life Ladder']].sort_values(by='Log GDP per capita', ascending=False).dropna(subset=['Log GDP per capita'])

    #plotting data
    # line_kws=dict shows colored line of reg
    sns.regplot(generosity_rows, x=generosity_rows['Generosity'], y=generosity_rows['Life Ladder'], color='green', label="Generosity's Impact on Happiness",line_kws=dict(color="b"),)
    plt.show()
    sns.regplot(wealth_rows, x=wealth_rows['Log GDP per capita'], y=wealth_rows['Life Ladder'], color='red', label="Log GDP per capita, Impact on Happiness",line_kws=dict(color="b"))
    plt.show()

    # I choose a regplot because I thought it would more accuratly show the data rather than a line plot because of its ability to show a line of regressioin. I made the color different as well
    # so the line of best fit could be easily identified. I choose accurate labels and titles to make sure the user knows what is going on in the graph. At first when I used a line graph it didn't
    # seem like Generosity had any impact on the Country's state of happiness. However when I plugged in the line of best fit it made it clear that although not much, there was some positive
    # correlation of generosity and happiness. I think this was due to the fact that some countries only had a little bit of generosity, like around .1 - .4 but also yeilded a ton of happiness,
    # showing that somtimes only a little bit of generosity is needed to produce high scores of happiness. on the other hand, wealth had a greater impact on overall happiness of a country.
    # The larger the Wealth in a country had a pretty strong correlation to the happiness as the line of best fit shows. When a country had a wealth of 11 there were few insances of a happiness
    # score below 5 which I thought was interesting.

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