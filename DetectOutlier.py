# -*- coding: utf-8 -*-
# TRAN DUY PHU -- phutdFX06737
#
###################################################

import sys
import argparse
import os
import pandas as pd
import yaml
import logging
import datetime

from view_point.numeric import check_numeric
from view_point.category import check_category
from view_point.data_length import check_length
from view_point.value_range import check_value_range

from utils.constant import Constant, ErrorMessage, ListThreshold, Config
from utils.utility import  find_csv_file_names, find_file_name_err, write_error_file

FLAGS = None

DetectOutlier_check_path = os.path.dirname(os.path.realpath(__file__))

config_path = DetectOutlier_check_path + Config.CONFIG_FOLDER + Config.CONFIG_FILENAME


def read_config_file(config_file):
    """
    'Type' for argument parse - check file format.
    :param config_file: File's path.
    :return: None.
    """

    if not os.path.exists(config_file):
        # Argument parse uses the ArgumentTypeError to give a rejection message like:
        # Error: argument input: x does not exist.
        logging.info(ErrorMessage.ERROR_NOT_EXIST.format(config_file))
        raise argparse.ArgumentTypeError(ErrorMessage.ERROR_NOT_EXIST.format(config_file))

    with open(config_file, 'r') as stream:
        try:
            config = yaml.load(stream)
            return config
        except yaml.YAMLError:
            logging.info(ErrorMessage.ERROR_WRONG_FORMAT.format(config_file))
            raise argparse.ArgumentTypeError(ErrorMessage.ERROR_WRONG_FORMAT.format(config_file))
    return None


def check_folder_exist(folder_path):
    """
    check exists of folder path.
    :param folder_path: Folder path.
    :return: Folder path if it exists.
    """
    if not os.path.isdir(folder_path):
        # Argument parse uses the ArgumentTypeError to give a rejection message like:
        # Error: argument input: x does not exist.
        logging.info(ErrorMessage.ERROR_NOT_EXIST.format(folder_path))
        raise argparse.ArgumentTypeError(ErrorMessage.ERROR_NOT_EXIST.format(folder_path))
    return folder_path


def check_view_points(config, input_folder, output_folder, encoding):
    """
    Main function that calls other functions to:
        1. Read input data
        2. Check view point
        3. Save result
    :param config:  threshold configuration.
    :param input_folder: input path.
    :param output_folder: output path.
    :param encoding: utf-8, shift-jis.
    :return: result.
    """

    start_time = datetime.datetime.now()
    logging.info(str(start_time) + "Begin check files:   ")

    ###########################################################################
    #Read all files in input_folder
    #filled in filenames variable
    filenames = find_csv_file_names(input_folder)

    data = [] #use to add data from input_folder
    columns = [] #use to add columns's name

    if filenames: #if in input_folder exist csv file
        for filename in filenames:
            df = pd.read_csv(input_folder + '/' + filename)
            data.append(df)
            columns.append(df.columns)
    else: #if in input_folder doestn't exist any csv file
        find_file_name_err(input_folder)

    #Check all columns in all files
    for col in columns:
        pd.to_csv(check_numeric(col, ListThreshold.CHECK_NUMERIC))
        check_value_range(col, ListThreshold.THRESHOLD_ZSCORE, ListThreshold.THRESHOLD_IQR)
        check_length(col, ListThreshold.CHECK_LENGTH)
        check_category(col, ListThreshold.CHECK_CATEGORY)
    #TODO: Call function to save the output
    ###########################################################################

def init():
    if not os.path.isdir(DetectOutlier_check_path + "/logs"):
        os.makedirs(DetectOutlier_check_path + "/logs")

    current_time = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    logging.basicConfig(
        handlers=[logging.FileHandler(DetectOutlier_check_path + '/logs/log_' + str(current_time) + '.log', 'w', 'utf-8')],
        level=logging.INFO,
        format='%(message)s')


if __name__ == '__main__':
    # call init function
    init()

    parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS)
    """
    Command line options
    """
    parser._actions[0].help = 'Display the guidelines.'

    parser.add_argument(
        '-i',
        type=check_folder_exist,
        required=True,
        dest="directory",
        help='Path to the directory that contains the CSV file to check'
    )

    parser.add_argument(
        '-o',
        type=check_folder_exist,
        required=True,
        dest="output_folder",
        help=' Path to summary report'
    )

    parser.add_argument(
        '-c',
        type=read_config_file,
        default=config_path,  # Path of the config file.
        dest="config",
        help=' Path to configuration file'
    )

    parser.add_argument(
        '-e',
        type=str,  # Encoding format.
        default='shift-jis',
        dest="encoding",
        help=' Encoding used for all CSV files of folder '
    )

    logging.info('Parsing arguments ...')

    FLAGS = parser.parse_args()

    # call main function
    check_view_points(FLAGS.config, FLAGS.directory, FLAGS.output_folder, FLAGS.encoding)
    print(' Done.')