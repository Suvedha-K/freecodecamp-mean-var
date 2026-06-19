import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read dataset (FIXED parsing)
    df = pd.read_csv('adult.data.csv', header=None, sep=',', skipinitialspace=True)
    # Add column names
    df.columns = [
        'age', 'workclass', 'fnlwgt', 'education', 'education-num',
        'marital-status', 'occupation', 'relationship', 'race', 'sex',
        'capital-gain', 'capital-loss', 'hours-per-week',
        'native-country', 'salary'
    ]

    # 1. Race count
    race_count = df['race'].value_counts()

    # 2. Average age of men
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. Percentage with Bachelor's degree
    percentage_bachelors = round(
        (df['education'] == 'Bachelors').mean() * 100, 1
    )

    # 4. Higher education (>50K)
    higher_edu = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    higher_education_rich = round(
        (df[higher_edu]['salary'] == '>50K').mean() * 100, 1
    )

    # 5. Lower education (>50K)
    lower_edu = ~higher_edu
    lower_education_rich = round(
        (df[lower_edu]['salary'] == '>50K').mean() * 100, 1
    )

    # 6. Min work hours
    min_work_hours = df['hours-per-week'].min()

    # 7. % rich among min workers
    min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round(
        (min_workers['salary'] == '>50K').mean() * 100, 1
    )

    # 8. Country with highest % >50K
    country_stats = df.groupby('native-country')['salary'].apply(
        lambda x: (x == '>50K').mean()
    )
    highest_earning_country = country_stats.idxmax()
    highest_earning_country_percentage = round(
        country_stats.max() * 100, 1
    )

    # 9. Top occupation in India (>50K)
    india_rich = df[
        (df['native-country'] == 'India') &
        (df['salary'] == '>50K')
    ]
    top_IN_occupation = india_rich['occupation'].value_counts().idxmax()

    if print_data:
        print("Race count:\n", race_count)
        print("Average age of men:", average_age_men)
        print("Percentage with Bachelors:", percentage_bachelors)
        print("Higher education rich:", higher_education_rich)
        print("Lower education rich:", lower_education_rich)
        print("Min work hours:", min_work_hours)
        print("Rich % among min workers:", rich_percentage)
        print("Top country:", highest_earning_country)
        print("Top country %:", highest_earning_country_percentage)
        print("Top occupation India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }