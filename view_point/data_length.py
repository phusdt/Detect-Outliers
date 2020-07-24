import numpy as np
import pandas as pd
from utils.constant import Constant


def check_length(data_col, threshold_length):
    """
    The function checks the length of the data column.
    :param data_col: data column.
    :param threshold_length: threshold of the length function.
    :return: result 'OK', 'NA', 'NG'.
    """

    # set default result as 'NA'
    result = 'NA'
    # get len of data_col as N
    N = len(data_col)
    # Setting up a new value chain is the length of each value in the original string
    Li = []
    for li in data_col:
        Li.append(len(li))  # add length of each value in data_col
    list_value = {str(i): Li.count(i) for i in Li}
    max_ki = max(list_value.values())
    if max_ki / N >= threshold_length and max_ki / N < 1:
        result = 'NG'
    elif max_ki / N == threshold_length:
        result = 'OK'

    return result

