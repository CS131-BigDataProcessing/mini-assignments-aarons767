import pandas as pd
import numpy as np



def calculate_mean(dataset):
    if 'Vict Age' not in dataset.columns:
        raise KeyError("'Vict Age' column not found")
    if dataset['Vict Age'].isnull().all():
        raise ValueError("The 'Vict Age' column empty.")
    return dataset['Vict Age'].mean()

def calculate_median(dataset):
    if 'Vict Age' not in dataset.columns:
        raise KeyError("'Vict Age' not found")
    
    ages = [age for age in dataset['Vict Age'] if pd.notnull(age)]
    if not ages:
        return 0
    
    ages.sort()
    n = len(ages)
    mid = n // 2
    
    if n % 2 == 0:
        return (ages[mid - 1] + ages[mid]) / 2
    else:
        return ages[mid]

