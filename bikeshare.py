import time
import pandas as pd
import numpy as np
import datetime as dt
import calendar as cl

CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv'
}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze(str) month - name of the month to filter by, or "all"
    to apply no month filter
        (str) day - name of the day of week to filter by, or "all"
    to apply no day filter
    """
    validCities = ["chicago", "new york city", "washington"]
    validMonths = {
        "january": 1,
        "february": 2,
        "march": 3,
        "april": 4,
        "may": 5,
        "june": 6,
        "july": 7,
        "august": 8,
        "september": 9,
        "october": 10,
        "november": 11,
        "december": 12,
        "all": 0
    }
    validDays = {
        "monday": 0,
        "tuesday": 1,
        "wednesday": 2,
        "thursday": 3,
        "friday": 4,
        "saturday": 5,
        "sunday": 6,
        "all": 7
    }

    print('Hello! Let\'s explore some US bikeshare data!')
    while True: #TO DO: get user input for city(chicago, new york city, washington).HINT: Use a while loop to handle invalid inputs
        print('Enter the name of the city that you would like to analyse data for : ')
        city = input()
        city = city.lower()
        if city in validCities: break
    while True: #TO DO: get user input for month(all, january, february, ..., june)
        print('Enter the month that you would like to analyse data for : ')
        month = input()
        month = month.lower()
        if month in validMonths.keys(): break
    month = validMonths[month]
    while True: #TO DO: get user input for day of week(all, monday, tuesday, ...sunday)
        print('Enter the day of the week you would like to analyse data for : ')
        day = input()
        day = day.lower()
        if day in validDays.keys(): break
    day = validDays[day]
    print('-' * 40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze(str) month - name of the month to filter by, or "all"
    to apply no month filter
        (str) day - name of the day of week to filter by, or "all"
    to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day """

    df = pd.read_csv(CITY_DATA[city])
    df["Start Time"] = pd.to_datetime(df['Start Time'])
    if (month != 0): #0 is mapped to all months
        df = df[df["Start Time"].dt.month == month]
    if (day != 7): #7 is mapped to all days
        df = df[df["Start Time"].dt.dayofweek == day]
    print("Do you want to view the first 5 lines of data?")
    view = 0
    while True:
        answer = input()
        answer = answer.lower()
        if (answer == "yes"):
            print(df.iloc[view:view+5])
            view = view + 5
        else: break
        print("Do you want to view the next 5 lines of data?")

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # TO DO: display the most common month
    df["month"] = df["Start Time"].dt.month
    popularMonth = cl.month_name[df["month"].mode()[0]]
    # TO DO: display the most common day of week
    df["day"] = df["Start Time"].dt.dayofweek
    popularDay = cl.day_name[df["day"].mode()[0]]
    # TO DO: display the most common start hour
    df["hour"] = df["Start Time"].dt.hour
    popularHour = df["hour"].mode()[0]
    print("The most common month is :", popularMonth)
    print("The most common day is :", popularDay)
    print("The most common hour is :", popularHour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def station_stats(df):
    """ Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    # TO DO: display most commonly used start station
    print("The most commonly used start station is : ", df["Start Station"].mode()[0])
    # TO DO: display most commonly used end station
    print("The most commonly used End station is : ", df["End Station"].mode()[0])
    # TO DO: display most frequent combination of start station and end station trip
    df["Start and End"] = "From " + df['Start Station'] + " to " + df['End Station']
    print("The most frequent combination of start and end station trip is : ", df["Start and End"].value_counts().idxmax())
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    # TO DO: display total travel time
    print("The total travel time: ", df["Trip Duration"].sum())
    # TO DO: display mean travel time
    print("The mean travel time: ", df["Trip Duration"].mean())
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # TO DO: Display counts of user types
    print("Count of user types : ", df["User Type"].value_counts())
    # TO DO: Display counts of gender
    if ("Gender") in df.columns:
        print("Count of gender types : ", df["Gender"].value_counts())
    else:
        print("There is no gender column in this dataframe")
    # TO DO: Display earliest, most recent, and most common year of birth
    if ("Birth Year") in df.columns:
        print("The earliest birth year is : ", df["Birth Year"].min())
        df["Relative Year"] = dt.datetime.now().year - df["Birth Year"]
        print("The most recent birth year is : ", dt.datetime.now().year - df["Relative Year"].min())
        print("The most common birth year is : ", df["Birth Year"].mode()[0])
    else:
        print("There is no birth year column in this panda dataframe")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

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
