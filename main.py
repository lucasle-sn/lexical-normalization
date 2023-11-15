#!/usr/bin/env python

import argparse
import re
import datetime
import time

from src import TwoGram
from src import Ged

METHOD_2GRAM = "2gram"
METHOD_GED = "ged"
METHOD_SD2GRAM = "sd2gram"
METHOD_SDGED = "sdged"

DICTIONARY_DIR = "dictionary/dict.txt"

SUPPORTED_METHODS = [
    METHOD_2GRAM,
    METHOD_GED,
    METHOD_SD2GRAM,
    METHOD_SDGED,
]


def read_lines(file_name):
    """
    Load a file and load data into an array
    """
    
    lines = open(file_name, "r").readlines()

    for i in range(len(lines)):
        lines[i] = lines[i][:-1]
    return lines


def implement(input_dir, output_dir, measure, execution_length = 10):
    """
    Open files and start to implement algorithm
    """
    output_fd = open(output_dir, "w+")
    dict_list = read_lines(DICTIONARY_DIR)
    term_list = read_lines(input_dir)

    # ==================== MEASURE DISTANCE ====================

    def measure_distance(term, dictionary_list, measure):
        """
        Measure distance of a term
        """
        
        def is_oov(term, dictionary_list):
            return term not in dictionary_list
        
        matching_distance = measure.get_default_distance
        matching_string = []

        if not is_oov(term, dictionary_list):
            matching_distance = measure.get_iv_distance(term)
            matching_string = [term]
        else:
            for dict in dictionary_list:
                distance = measure.get_oov_distance(term, dict)

                if (measure.is_greatest_distance and (distance > matching_distance)) or (measure.is_least_distance and (distance < matching_distance)):
                    matching_distance = distance
                    matching_string = [str(dict)]
                elif distance == matching_distance:
                    matching_string.append(str(dict))
        
        return [matching_distance, matching_string]

    for i in range(len(term_list)):
        [matching_distance, matching_string] = measure_distance(term_list[i], dict_list, measure)

        print(i, ". The term: ", term_list[i])
        print("Global edit distance: ", matching_distance)
        print("Matching string: ", matching_string)
        print()

        output_fd.write("%s\n" % ','.join(matching_string))

        if (execution_length > 0 and i == execution_length):
            break

    output_fd.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--method", type=ascii, help="Method")
    parser.add_argument("-i", "--input", type=ascii, help="Input path")
    parser.add_argument("-o", "--output", type=ascii, help="Output path")
    parser.add_argument("-l", "--length", type=int, help="Execution length")
    parser.add_argument("-c", "--clean", action='store_true', help="Delete all generated output")
    args = parser.parse_args()
    
    method = re.sub("[']", "", args.method)       
    input_dir = re.sub("[']", "", args.input)
    output_dir = re.sub("[']", "", args.output)
    execution_length = int(args.length)
    
    if method not in SUPPORTED_METHODS:
        raise AssertionError("Unsupported method")

   
    start_time = time.time()
    print("Start time: ", datetime.datetime.now())
    
    if method == METHOD_2GRAM:
        # implement 2GRAM method
        print ("implement TWO GRAM method")
        measure = TwoGram()
    elif method == METHOD_GED:
        # implement GED method
        print ("implement GED method")
        measure = Ged()
    elif method == METHOD_SD2GRAM:
        # implement Soundex + 2GRAM method
        print ("implement Soundex + 2GRAM method")
    elif method == METHOD_SDGED:
        # implement Soundex + GED method
        print ("implement Soundex + GED method")
        
    implement(input_dir, output_dir, measure, execution_length)
        
    end_time = time.time()
    print("End time: ", datetime.datetime.now())
    running_time = end_time - start_time
    print("Total running time: ", running_time)
