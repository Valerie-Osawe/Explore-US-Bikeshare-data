import time
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
    print('O O   ^ ^   ^ ^   O O\n -     -     -     -')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    names_of_cities = ['chicago', 'new york city', 'washington']
    while True:
        city = input('Which city do you want to analyze between Chicago, New York city or Washington?\n ').lower()
        if city in names_of_cities:
            break
        else:
            print('You entered an invalid city!')
    # TO DO: get user input for month (all, january, february, ... , june)
    names_of_months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    while True: 
        month = input('Which month do you want to filter?\n Input "all" if you want to filter all.\n ').lower()
        if month  in names_of_months:  
            break
        elif month == 'all':
            print('No month will be filtered.')
            break
        else:
            print('You entered an invalid month!')
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_query = input('Will you like to filter all days or specific day? yes or no?\n ').lower()
    if day_query == 'yes':
        day ='all'
        print('No day will filtered.')
    else:
        while True:
            day = int(input('Which day will you like to filter using sunday = 0, monday = 1...saturday = 6\n '))
            days = [0, 1, 2, 3, 4, 5, 6]
            if day in days:
                print('Day filtered')
                break
            else:
                print('You entered an invalid day!')
            print('-'*40) 
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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['week day'] = df['Start Time'].dt.dayofweek
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':
        df = df.loc[df['week day'] == day]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()
    print('The most common month of travel:\n', most_common_month)
    # TO DO: display the most common day of week
    most_common_day = df['week day'].mode()
    print('The most common day of travel:\n', most_common_day)
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df['hour'].mode()
    print('The most common start hour of travel:\n', most_common_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()
    print('The most commonly used start station:\n', most_common_start_station)
    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()
    print('The most commonly used end station:\n', most_common_end_station)
    # TO DO: display most frequent combination of start station and end station trip
    comb_start_and_end_station = (df['Start Station'] + ' ' + df['End Station']).mode()
    print('The most frequent combination of start and end station:\n', comb_start_and_end_station)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    print('The tottal travel time:\n', total_time)
    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    print('The mean travel time:\n', mean_time)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts()
    print('The counts of user types are:\n', user_type)
    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender = df['Gender'].value_counts()
        print('The counts of gender:\n', gender)
    else:
        print('No available data on Gender.')
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest = df['Birth Year'].min()
        print('The earliest birth year:\n', earliest)
        recent = df['Birth Year'].max()
        print('The most recent birth year:\n', recent)
        most_common_birth_year = df['Birth Year'].mode()
        print('The most common birth year:\n', most_common_birth_year)
    else:
        print('No available data on Birth Year')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?\n ").lower()
    start_loc = 0
    while view_data == 'yes':
        print(df.iloc[start_loc:(start_loc + 5)])
        start_loc += 5
        view_display = input("Do you wish to continue?: ").lower()
        if view_display != 'yes':
            break
    print('Thank you for exploring US bikeshare with me!')
    print('O O   ^ ^   ^ ^   O O\n -     -     -     -') 
        


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
