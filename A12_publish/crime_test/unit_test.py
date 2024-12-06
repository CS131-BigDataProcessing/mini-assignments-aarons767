import unittest
import pandas as pd
from stats_function import calculate_mean, calculate_median
from validate_functions import validate_vict_sex, validate_vict_age

class TestStatsFunctions(unittest.TestCase):
    def setUp(self):
        try:
            self.dataset = pd.read_csv("Crime_Data_from_2020_to_Present.csv")
        except FileNotFoundError:
            raise FileNotFoundError("Crime_Data_from_2020_to_Present.csv not found.")
            
        #Tester set for mean and median test
        self.mock_dataset = pd.DataFrame({
            'Vict Age': [25, 30, 35, 40, 45],
            'Vict Sex': ['M', 'F', 'M', 'F', 'M']
        })
        
    def test_calculate_mean_real_dataset(self):
        #Test calculate_mean with the real dataset.
        mean_age = calculate_mean(self.dataset)
        self.assertIsInstance(mean_age, (float, int), "Mean should be a number.")
        self.assertGreater(mean_age, 0, "Mean should be greater than 0.")

    def test_calculate_median_real_dataset(self):
        median_age = calculate_median(self.dataset)
        self.assertIsInstance(median_age, (float, int), "Median should be a number.")
        self.assertGreater(median_age, 0, "Median should be greater than 0.")
    
    #test for mean for smaller dataset
    def test_calculate_mean_mock_dataset(self):
        mean_age = calculate_mean(self.mock_dataset)
        self.assertEqual(mean_age, 35)

    #to test median for smaller data set
    def test_calculate_median_mock_dataset(self):
        median_age = calculate_median(self.mock_dataset)
        self.assertEqual(median_age, 35)

class TestValidateFunctions(unittest.TestCase):
    def setUp(self):
        try:
            self.dataset = pd.read_csv("Crime_Data_from_2020_to_Present.csv")
        except FileNotFoundError:
            raise FileNotFoundError("Crime_Data_from_2020_to_Present.csv not found.")
            
        self.invalid_sex_mock_dataset = pd.DataFrame({
            'Vict Age': [25, 30, 35],
            'Vict Sex': ['X', None, 'Z']
        })
        self.invalid_age_mock_dataset = pd.DataFrame({
            'Vict Age': [150, -5, None],
            'Vict Sex': ['M', 'F', 'M']
        })
        
    def test_validate_vict_sex_invalid_mock_dataset(self):
        #Test with an invalid mock dataset
        result = validate_vict_sex(self.invalid_sex_mock_dataset)
        self.assertFalse(result)
        
    def test_validate_vict_age_invalid_mock_dataset(self):
        #Test with an invalid mock dataset.
        result = validate_vict_age(self.invalid_age_mock_dataset)
        self.assertFalse(result)
        
    def test_validate_vict_sex_real_dataset(self):
        #Test validate_vict_sex with the real dataset.
        result = validate_vict_sex(self.dataset)
        self.assertIsInstance(result, bool, "Result should be a boolean.")
        self.assertFalse(result) #'Vict Sex' column validation must fail as expected

    def test_validate_vict_age_real_dataset(self):
        result = validate_vict_age(self.dataset)
        self.assertIsInstance(result, bool, "Result should be a boolean.")
        self.assertFalse(result) #'Vict Age' column validation must fail as expected

if __name__ == "__main__":
    unittest.main()
