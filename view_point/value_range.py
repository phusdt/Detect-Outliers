
import pandas as pd
from utils.constant import Constant


def check_value_range(data_col, threshold_range_z_score, threshold_range_iqr):
    """
    The function checks value range of the data column
    :param data_col: one data column from file csv.
    :param threshold_range_z_score: threshold_z_score of the length function
    :param threshold_range_iqr: threshold_z_iqr of the length function
    :return: result 'OK', 'NA', 'NG'
    """

    # TODO: write your code here

