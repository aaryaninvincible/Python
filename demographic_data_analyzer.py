import pandas as pd

# Load the dataset
df = pd.read_csv('census_data.csv')  # Make sure to adjust the file path if necessary

def race_count():
    return df['race'].value_counts()

def average_age_men():
    return round(df[df['sex'] == 'Male']['age'].mean(), 1)

def percentage_bachelors():
    total_people = len(df)
    bachelors_count = len(df[df['education'] == 'Bachelors'])
    return round((bachelors_count / total_people) * 100, 1)

def percentage_high_edu_rich():
    advanced_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    rich = df[advanced_education]['salary'] == '>50K'
    return round((rich.sum() / advanced_education.sum()) * 100, 1)

def percentage_no_high_edu_rich():
    no_advanced_education = ~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    rich = df[no_advanced_education]['salary'] == '>50K'
    return round((rich.sum() / no_advanced_education.sum()) * 100, 1)

def minimum_hours():
    return df['hours-per-week'].min()

def percentage_min_hours_rich():
    min_hours = minimum_hours()
    min_hours_workers = df[df['hours-per-week'] == min_hours]
    rich = min_hours_workers['salary'] == '>50K'
    return round((rich.sum() / len(min_hours_workers)) * 100, 1)

def highest_earning_country():
    country_salary_stats = df.groupby('native-country')['salary'].value_counts(normalize=True).unstack()
    percent_earning_more_than_50k = country_salary_stats['>50K'] * 100
    highest_percentage_country = percent_earning_more_than_50k.idxmax()
    highest_percentage = percent_earning_more_than_50k.max()
    return highest_percentage_country, round(highest_percentage, 1)

def most_popular_occupation_in_india():
    india_occupation_stats = df[df['native-country'] == 'India']
    rich_occupation_stats = india_occupation_stats[india_occupation_stats['salary'] == '>50K']['occupation'].value_counts()
    return rich_occupation_stats.idxmax()

# You can use these functions to get the desired results
if __name__ == "__main__":
    print("Race Count:\n", race_count())
    print("Average Age of Men:", average_age_men())
    print("Percentage of People with Bachelor's Degree:", percentage_bachelors(), "%")
    print("Percentage of People with Advanced Education making >50K:", percentage_high_edu_rich(), "%")
    print("Percentage of People without Advanced Education making >50K:", percentage_no_high_edu_rich(), "%")
    print("Minimum Hours Worked per Week:", minimum_hours())
    print("Percentage of People with Minimum Hours Working making >50K:", percentage_min_hours_rich(), "%")
    print("Country with Highest Percentage of People Earning >50K:", highest_earning_country())
    print("Most Popular Occupation in India for People Earning >50K:", most_popular_occupation_in_india())
