import pandas as pd
import numpy as np


dataset = None


def validate_vict_sex(dataset):

    if 'Vict Sex' not in dataset.columns:
        raise KeyError("'Vict Sex' column not found")
    
    for sex in dataset['Vict Sex']:
        if pd.isnull(sex) or sex not in ['M', 'F']:
            print("Sex must be 'M' or 'F': ", sex)
            return False
    return True

def validate_vict_age(dataset):
    
    if 'Vict Age' not in dataset.columns:
        raise KeyError("'Vict Age' column not found")
    
    for age in dataset['Vict Age']:
        if pd.isnull(age) or not (1 <= age <= 100):
            print("Age is not in desired bounds: ", age)
            return False
    return True

