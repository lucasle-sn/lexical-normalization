# The University of Melbourne
# School of Computing and Information Systems
# COMP90049 Knowledge Technologies
# Semester 01/2019
# Project A: Lexical Normalization
# Author: QUANG TRUNG LE

#!/usr/bin/env python

import argparse
import re
from helper import read_lines


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--correct", type=ascii, help="Correct data path")
    parser.add_argument("-r", "--result", type=ascii, help="Result path")
    args = parser.parse_args()
    
    correct_path = re.sub("[']", "", args.correct)       
    result_path = re.sub("[']", "", args.result)
    
    correct_list = read_lines(correct_path)
    predict_list = read_lines(result_path)
    matching = []
    precision = []

    for i in range(len(predict_list)):
        matching.append(False)
        precision.append(0)

        predict_count = str(predict_list[i]).split(",")

        for j in range(len(predict_count)):
            if correct_list[i] == predict_count[j]:
                matching[i] = True
                precision[i] = 1
                break
        precision[i] = precision[i]*100/len(predict_count)

    # Accuracy
    accuracy = matching.count(True)*100/len(matching)
    print("Accuracy: ", accuracy)

    # Precision
    sum_precision = 0
    for i in range(len(precision)):
        sum_precision = sum_precision + precision[i]
    average_precision = sum_precision/len(precision)
    print("Precision: ", average_precision)
