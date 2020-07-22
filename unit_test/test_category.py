import unittest
import pandas as pd
import numpy as np
import sys
from view_point.category import check_category


class MyTest(unittest.TestCase):
    """
    Test category
    """

    def test_check_category_with_valid_value(self):
        data_col = pd.Series(['a', 'b', 'a', 'a', 'b', 'b', 'b', 'a', 'c', 'c', 'c', 'c'])
        #TODO: call your function to check data_col with threshold=0.9

        self.assertEqual(result, 'OK')
        self.assertEqual(len(df_detail), 0)

    def test_check_category_with_empty_value(self):
        data_col = pd.Series([])
        #TODO: call your function to check data_col with threshold=0.9
        self.assertEqual(result, 'OK')
        self.assertEqual(k, 0)
        self.assertEqual(N, 0)
        self.assertEqual(len(df_detail), 0)

    #TODO: write your other unittest function here


if __name__ == '__main__':
    unittest.main()
