
import pandas as pd
import numpy as np
import math
from utils.constant import Constant

##############################################################################
# build mean and stdev function
# in numpy, we already had build-in function for mean and standard deviation - np.mean() and np.std()
# I checked those 2 func, it running well and just similar to numpy build-in func
def mean(data_col):
    return (sum(data_col) / len(data_col))
def stdev(data):
    mu = mean(data)
    return math.sqrt(sum([(point - mu) ** 2 for point in data]) / len(data))
##############################################################################


def check_value_range(data_col, threshold_range_z_score, threshold_range_iqr):
    """
    The function checks value range of the data column
    :param data_col: one data column from file csv.
    :param threshold_range_z_score: threshold_z_score of the length function
    :param threshold_range_iqr: threshold_z_iqr of the length function
    :return: result 'OK', 'NA', 'NG'
    """

    Vmean = 0
    Vstdev = 0
    # set result's default as 'NA'
    result = 'NA'
    # numbers of outliers in data_col
    outliers = []

    # check numeric in data_col
    for row in data_col:
        # If the column has a value isn't numeric, return 'NA'
        row = str(row)
        if not row.isnumeric():
            return result, Vmean, Vstdev

    # If the column has 100% value is numeric
    # convert into integer
    for i in range(len(data_col)):
        data_col[i] = int(data_col[i])
    # sort data_col
    data_col_sorted = np.sort(data_col)

    # get the middle value's index
    median_index = len(data_col_sorted) // 2 if len(data_col_sorted) % 2 == 0 else len(data_col_sorted) // 2 + 1

    # If length of data_col is even number
    # First quartile Q1 is value calculate from index 0 to median_index
    # Third quartile Q3 is value calculate from median_index+1 to index -1
    if len(data_col_sorted) % 2 == 0:
        Q1 = np.median(data_col_sorted[:median_index])
        Q3 = np.median(data_col_sorted[median_index:])

        # If length of data_col is odd number
    # First quartile Q1 is value calculate from index 0 to median_index-1
    # Third quartile Q3 is value calculate from median_index+1 to index -1
    else:
        Q1 = np.median(data_col_sorted[:median_index - 1])
        Q3 = np.median(data_col_sorted[median_index:])

    # Calculate IQR
    IQR = Q3 - Q1

    # Calculate [Low, Up] value based on threshold_iqr:
    Low = Q1 - threshold_range_iqr * IQR
    Up = Q3 + threshold_range_iqr * IQR
    # If x value is greater than Up or smaller than Lower, x is outlier.
    for x in data_col:
        if x > Up or x < Low:
            outliers.append(x)  # if x is outlier, append x to outliers[]

    # Initialization
    # Calculate mean of all values in column:
    Vmean = mean(data_col)

    # Calculate the standard deviation:
    Vstdev = stdev(data_col)

    # Calculate z-score of each value Vi: Vi_zscore = (Vi - Vmean) / Vstdev
    # If abs(Vi_zscore)> threshold_z_score, x is outlier.
    for Vi in data_col:
        Vi_zscore = (Vi - Vmean) / Vstdev
        if abs(Vi_zscore) > threshold_range_z_score:
            outliers.append(Vi)  # if Vi is outlier, append Vi to outliers[]

    if len(outliers) > 0:
        result = 'NG'
    elif len(outliers) == 0:
        result = 'OK'

    return result, Vmean, Vstdev
