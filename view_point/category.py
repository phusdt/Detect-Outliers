import numpy as np
import pandas as pd
import math
from utils.constant import Constant


def mean(data_col):
    return (sum(data_col) / len(data_col))


def stdev(data):
    mu = mean(data)
    return math.sqrt(sum([(point - mu) ** 2 for point in data]) / len(data))


def check_category(data_col, threshold_category):
    """
    The function checks category of the data column
    :param data_col:  one data column from file csv.
    :param threshold_category: threshold of the length function.
    :return: result 'OK', 'NA', 'NG'.
    """

    Pi = []
    result = 'NA'
    outliers = []
    set_data_col = set(data_col)
    # for loop uses to count the frequence of each unique value
    for i in set_data_col:
        count = 0  # reset count varialbe for each value
        for j in data_col:
            if j == i:
                count += 1
        Pi.append(count)  # add number of each unique value to Pi

    Pmean = mean(Pi)
    Pstdev = stdev(Pi)

    for pi in Pi:
        Li_zscore = (pi - Pmean) / Pstdev
        # if Li_zscore < thresholdLength then it is outlier,
        if Li_zscore < threshold_category:
            outliers.append(Li_zscore)  # append Li_zscore to outliers[]

    if len(outliers) == 0:
        result = 'OK'
    else:
        result = 'NG'

    return result