
import pandas as pd
import numpy as np
from utils.constant import Constant
from utils.utility import find_summary_file


def check_numeric(data_col, threshold):
    """
    Check numeric
    :param data_col: one data column from file csv.
    :param threshold: the point at which you start evaluate the result is NG,NA or OK.
    :return: result (OK, NG, NA), k (numbers of numeric rows), N (total values),
    abnormal_data_details (DataFrame contains values and indexes of invalid numeric).
     """
    # create dictionnary to constains values and indexes of invalid numeric
    abnormal_data_details = {'Indexes': [], 'Values': []}

    indexes = []  # indexes of invalid numeric
    values = []  # values of invalid numeric

    # for loop to fill data to 2 list (indexes and values)
    for index, value in data_col.iteritems():
        value = str(value)
        row_isnumeric = value.isnumeric()
        if not row_isnumeric:
            indexes.append(index)
            values.append(value)

    # update value in dict and change into data frame
    abnormal_data_details['Indexes'] = indexes
    abnormal_data_details['Values'] = values
    abnormal_data_details = pd.DataFrame(abnormal_data_details)


    result = 'NA'
    k = len(data_col) - len(values)  # number of numeric rows: total_row - abnormal_row
    N = len(data_col)  # total values

    # Condition to get result by the ratio of k/N and threshold
    if k / N >= threshold and k < N:
        result = 'NG'
    elif k == N:
        result = 'OK'

    return result, k, N, abnormal_data_details




