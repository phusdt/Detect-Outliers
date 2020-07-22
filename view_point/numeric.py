
import pandas as pd
import numpy as np
from utils.constant import Constant


def check_numeric(data_col, threshold):
    """
    Check numeric
    :param data_col: one data column from file csv.
    :param threshold: the point at which you start evaluate the result is NG,NA or OK.
    :return: result (OK, NG, NA), k (numbers of numeric rows), N (total values),
    abnormal_data_details (DataFrame contains values and indexes of invalid numeric).
     """
    #create dictionnary to constains values and indexes of invalid numeric
    abnormal_data_details = {'Indexes': [], 'Values': []}

    indexes = []
    values = []
    #for loop to fill data to 2 list (indexes and values)
    for index, value in data_col.iteritems():
        row_isnumeric = value.isnumeric()
        if not row_isnumeric:
            indexes.append(index)
            values.append(value)

    #update value in dict and change into data frame
    abnormal_data_details['Indexes'] = indexes
    abnormal_data_details['Values'] = values
    abnormal_data_details = pd.DataFrame(abnormal_data_details)

    result = 'NA'
    k = len(values)  # number of numeric rows
    N = len(data_col)  # total values
    #Condition to get result by the ratio of k/N and theshold
    if k/N >= threshold and k < N:
        result = 'NG'
    elif k == N:
        result = 'OK'

    return result, k, N, abnormal_data_details









