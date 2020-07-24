import unittest
import pandas as pd
import numpy as np
import sys 
from view_point.data_length import check_length

class MyTest(unittest.TestCase):

    def test_check_length_with_valid_value(self):
        data_col = pd.Series(['a', 'b', 'a', 'a', 'b', 'b', 'b', 'a', 'c', 'c', 'c', 'c'])

        #call function to check data_col with threshold=0.9

        self.assertEqual(result, 'OK')
        self.assertEqual(len(df_detail), 0)

    #write unittest function here


if __name__ == '__main__':
    unittest.main()
