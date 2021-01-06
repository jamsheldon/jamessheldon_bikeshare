import time
import calendar
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Which city (Chicago, New York City, Washington) would you like to view data for: ')
    city = city.lower()

    if city == 'new york' or city == 'nyc' or city == 'ny':
       city = 'new york city'

    while (city != 'washington') and (city != 'chicago') and (city != 'new york city'):
        print("Oops, sorry I cannot find that city. I only have any data for Chicago, New York City or Washington")
        city = input('Which city (Chicago, New York City, Washington) you would like to view data for: ')
        city = city.lower()
        if city == 'new york' or city == 'nyc' or city == 'ny':
            city = 'new york city'

    f = input('What filters would you like to apply to the data? You can choose to filter by Month, Day, Both or None: ')
    f = f.lower()
    if f == 'none':
        month = 'all'
        day = 'all'
    if f == 'month':
        month = input('Which month? January, Feburary, March, April, May or June? ')
        month = month.lower()
        day = 'all'
    if f == 'both':
        month = input('Which month would you like to view? January, Feburary, March, April, May or June? ')
        month = month.lower()
        day = input('Which day of the week would you like to filter? ')
        day = day.lower()
    elif f == 'day':
        day = input('Which day of the week would you like to filter? ')
        day = day.lower()
        month = 'all'


#     if f == 'month':
#             day = 'all'
#         elif:
#             day = input('Which day of the week would you like to filter? ')
#             day = day.lower()
# #         day = day.lower()
#     elif f == 'both':

# #         month = input('Which month? January, Feburary, March, April, May or June? ')
# #         month = month.lower()
# #         day = 'all'
#     elif f == 'day':
#         day = input('Which day of the week would you like to filter? ')
#         day = day.lower()
#         month = 'all'
#     elif f == 'none':
#         month = 'all'
#         day = 'all'

    while (f != 'month') and (f != 'day') and (f != 'both') and (f != 'none'):
        print("Sorry, I don't recognise that filter...please choose Month, Day, Both or None")
        f = input('What filters would you like to apply? ')
        f = f.lower()
        if f == 'none':
            month = 'all'
            day = 'all'
        if f == 'month':
            month = input('Which month? January, Feburary, March, April, May or June? ')
            month = month.lower()
            day = 'all'
        if f == 'both':
            month = input('Which month? January, Feburary, March, April, May or June? ')
            month = month.lower()
            day = input('Which day of the week would you like to filter? ')
            day = day.lower()
        elif f == 'day':
            day = input('Which day of the week would you like to filter? ')
            day = day.lower()
            month = 'all'




    # TO DO: get user input for month (all, january, february, ... , june)
#     months = ['January', 'February', 'March', 'April', 'May', 'June', 'All']

#     month = input('Which month? January, Feburary, March, April, May or June?')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

#     day = input('Which day would you like to filter? (For all select all): ')

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    "load data file into a dataframe"
    df = pd.read_csv(CITY_DATA[city])

    "convert the Start Time column to datetime"
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    "extract month and day of week from Start Time to create new columns"
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    df.fillna(0)



    "filter by month if applicable"
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[ df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[ df['day_of_week'] == day.title()]
        print('Hello')

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].value_counts().idxmax()
    m = calendar.month_name[popular_month]
    print('The most frequent month of travel was -> {}'.format(m))

    # TO DO: display the most common day of week
    day = df['day_of_week'].value_counts().idxmax()
    print('The most frequent day of travel was -> {}'.format(day))

    # TO DO: display the most common start hour
    hour = df['hour'].value_counts().idxmax()
    if hour >=12:
        t='pm'
    else:
        t='am'
    print('The most frequent hour of travel was -> {}:00{}'.format(hour,t))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_mode = df['Start Station'].mode()
    print("The most popular starting station was: {}.".format(start_mode.to_string()))

    # TO DO: display most commonly used end station
    end_mode = df['End Station'].mode()
    print("The most popular ending station was: {}.".format(end_mode.to_string()))

    # TO DO: display most frequent combination of start station and end station trip
    counts = df.groupby(['Start Station','End Station']).size().sort_values(ascending=False).head(1)
    print('The most popular combination of start station and end station was: {} '.format(counts))
#     print(counts.('Start Station')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    travel_time = df['Trip Duration'].sum()
    tt_min = travel_time / 60
    tt_hours = tt_min/60
    tt_days = tt_hours/24
    tt_min = "{:.2f}".format(tt_min)
    tt_hours = "{:.2f}".format(tt_hours)
    tt_days = "{:.2f}".format(tt_days)

    print('The total travel time was: ')
    print('{} minutes'.format(str(tt_min)))
    print('{} hours'.format(str(tt_hours)))
    print('{} days'.format(str(tt_days)))

    # TO DO: display mean travel time
    travel_time = df['Trip Duration'].mean()
    mt_min = travel_time / 60
    mt_hours = mt_min / 60
    mt_days = mt_hours / 24
    mt_min = "{:.2f}".format(mt_min)
    mt_hours = "{:.2f}".format(mt_hours)
    mt_days = "{:.2f}".format(mt_days)

    print('The mean travel time was: ')
    print('{} minutes'.format(str(mt_min)))
    print('{} hours'.format(str(mt_hours)))
    print('{} days'.format(str(mt_days)))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays basic statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('The breakdown of users type is:')
    print(user_types.to_string())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats2(df, ):

    if 'Gender' in df:
        print('\nCalculating User Stats...\n')
        start_time = time.time()

    # TO DO: Display counts of gender
        genders = df['Gender'].value_counts()
        print('The breakdown of users based on gender is: ')
        print(genders.to_string())

        # TO DO: Display earliest, most recent, and most common year of birth
        oldest = df['Birth Year'].min()
        print('The oldest customer was born in: ')
        print(oldest)

        youngest = df['Birth Year'].max()
        print('The youngest customer was born in: ')
        print(youngest)

        popular = df['Birth Year'].mode().head(1)
        print('The most popular birth year was: ')
        print(popular)

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
