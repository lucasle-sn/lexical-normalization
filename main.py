#!/usr/bin/env python

import argparse
import re
import datetime
import time
import jellyfish

from src import TwoGram
from src import Ged

METHOD_2GRAM = "2gram"
METHOD_GED = "ged"
METHOD_SD2GRAM = "sd2gram"
METHOD_SDGED = "sdged"

DICTIONARY_DIR = "dictionary/dict.txt"
DICTIONARY_SD_DIR = "dictionary/dict_soundex.txt"

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


def get_soundex_match(term, dict_list, dict_list_sd):
    def is_oov(term, dictionary_list):
        return term not in dictionary_list
    
    # ==================== SOUNDEX MATCHING ====================
    matching_list = []
    term_sd = jellyfish.soundex(term)
    if not is_oov(term, dict_list):
        matching_list.append(term)
    else:
        for j in range(len(dict_list)):
            if term_sd == dict_list_sd[j]:
                matching_list.append(dict_list[j])
    
    return matching_list


def implement(input_dir, output_dir, measure, soundex_preprocess = False, execution_length = 10):
    """
    Open files and start to implement algorithm
    """
    output_fd = open(output_dir, "w+")
    dict_list = read_lines(DICTIONARY_DIR)
    term_list = read_lines(input_dir)

    if (soundex_preprocess):
        dict_list_sd = read_lines(DICTIONARY_SD_DIR)

    for i in range(len(term_list)):
        
        if (soundex_preprocess):
            # If preprocess with soundex, create a new filtered list as dictionary
            dict_list_sd_filtered = get_soundex_match(term_list[i], dict_list, dict_list_sd)
            [matching_distance, matching_string] = measure.measure_distance(term_list[i], dict_list_sd_filtered)
        else:
            [matching_distance, matching_string] = measure.measure_distance(term_list[i], dict_list)

        print(i, ". The term: ", term_list[i])
        print("Distance: ", matching_distance)
        print("Matching string: ", matching_string, "\n")

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

    if method in [METHOD_2GRAM, METHOD_GED]:
        if method == METHOD_2GRAM:
            # implement 2GRAM method
            print ("implement TWO GRAM method")
            measure = TwoGram()
        elif method == METHOD_GED:
            # implement GED method
            print ("implement GED method")
            measure = Ged()
            
        implement(input_dir, output_dir, measure, False, execution_length)

    if method in [METHOD_SD2GRAM, METHOD_SDGED]:
        if method == METHOD_SD2GRAM:
            # implement Soundex + 2GRAM method
            print ("implement Soundex + 2GRAM method")
            measure = TwoGram()
        elif method == METHOD_SDGED:
            # implement Soundex + GED method
            print ("implement Soundex + GED method")
            measure = Ged()
            
        implement(input_dir, output_dir, measure, True, execution_length)


    end_time = time.time()
    print("End time: ", datetime.datetime.now())
    running_time = end_time - start_time
    print("Total running time: ", running_time)
