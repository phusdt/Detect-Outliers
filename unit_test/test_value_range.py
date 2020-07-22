import unittest
import pandas as pd
import numpy as np
import sys 
from view_point.value_range import check_value_range


class MyTest(unittest.TestCase):

    def test_check_value_range_with_na_value(self):
        data_col = pd.Series(['a', 'b', 'a', 'a', 'b', 'b', 'b', 'a', 'c', 'c', 'c', 'c'])


        #TODO: call your function to check data_col with threshold_range_z_score = 15, threshold_range_iqr=1.5

        self.assertEqual(result, 'NA')
        self.assertEqual(len(abnormal_data_details), 0)

    def test_check_value_range_with_empty_value(self):
        data_col = pd.Series([])
        #TODO: call your function to check data_col with threshold_range_z_score = 15, threshold_range_iqr=1.5

        self.assertEqual(result, 'OK')
        self.assertEqual(len(abnormal_data_details), 0)

    # TODO: write your other unittest functions here

if __name__ == '__main__':
    unittest.main()
