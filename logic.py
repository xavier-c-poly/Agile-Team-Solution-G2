import pandas as pd

def calculate_stats(df):
    mean = float(df["Grades"].mean())
    max = int(df["Grades"].max())
    min = int(df["Grades"].min())
    return mean, max, min
    

def get_grade_distribution(df):
    grade_distribution = {'A': 0, 'B': 0,'C': 0, 'D': 0, 'F': 0}
    grades = df["Grades"].to_list()

    for grade in grades:
        if grade >= 90:
            grade_distribution['A'] = grade_distribution['A'] + 1
        elif grade >= 80:
            grade_distribution['B'] = grade_distribution['B'] + 1
        elif grade >= 70:
            grade_distribution['C'] = grade_distribution['C'] + 1
        elif grade >= 60:
            grade_distribution['D'] = grade_distribution['D'] + 1
        else:
            grade_distribution['F'] = grade_distribution['F'] + 1

    return grade_distribution