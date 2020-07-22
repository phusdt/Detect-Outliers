
import pandas as pd
import os
from os import listdir
import datetime
import logging
from utils.constant import ErrorMessage


def find_csv_file_names(input_folder, suffix=".csv"):
    """
    Find csv name
    :param input_folder: Folder path
    :param suffix: suffix
    :return: name of csv file
    """
    filenames = listdir(input_folder)
    return [filename for filename in filenames if filename.endswith(suffix)]


def find_file_name_err(input_folder, suffix=".csv"):
    """
    Find file name error
    :param input_folder: Folder path
    :param suffix: suffix
    :return: file name is not csv
    """
    filenames = listdir(input_folder)
    arr_name_error = []
    for filename in filenames:
        if filename.endswith(suffix):
            pass
        else:
            start = datetime.datetime.now()
            arr_name_error.append(filename)
            logging.info(str(start) + "  Processing start:   " + filename)
            logging.info(str(datetime.datetime.now()) + "  Processing complete:   " + ErrorMessage.ERROR__FILE_WRONG_FORMAT.format(
                filename) + "   processing time:  " + str(datetime.datetime.now() - start) + "(Seconds)")
    return arr_name_error


def write_error_file(file_name_error, output_dir):
    """
    Write error file
    :param file_name_error: name of file is not csv
    :param output_dir: Path to the output directory
    :return: None
    """
    file_name_error.to_csv(output_dir, mode='w+', index=False)


#######################################################

# TODO: Write your common functions here

#######################################################
