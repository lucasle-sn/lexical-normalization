# The University of Melbourne
# School of Computing and Information Systems
# COMP90049 Knowledge Technologies
# Semester 01/2019
# Project A: Lexical Normalization
# Author: QUANG TRUNG LE - 987445

import numpy
import time
import datetime

MATCHING = 1
DELETION = -1
INSERTION = -1
REPLACEMENT = -1


def init_matrix(row, column):
    matrix = numpy.zeros((row, column), dtype=int)

    for i in range(0, row):
        matrix[i][0] = i * INSERTION
    for j in range(0, column):
        matrix[0][j] = j * DELETION

    return matrix


def get_max(value_list):
    max_value = value_list[0]
    for i in value_list:
        if i > max_value:
            max_value = i
    return max_value


def check_equals(string01, string02):
    if string01 == string02:
        equals = MATCHING
    else:
        equals = REPLACEMENT
    return equals


def calc_matrix(matrix, term, query):
    [row, column] = numpy.shape(matrix)
    for i in range(1, row):
        for j in range(1, column):
            insert_value = matrix[i - 1][j] + INSERTION
            delete_value = matrix[i][j - 1] + DELETION
            match_value = matrix[i - 1][j - 1] + check_equals(query[i - 1], term[j - 1])

            matrix[i][j] = get_max([insert_value, delete_value, match_value])

    return matrix


def global_edit_distance(term, query):
    term_length = len(term)
    query_length = len(query)

    matrix = init_matrix(query_length + 1, term_length + 1)
    matrix = calc_matrix(matrix, term, query)

    return matrix[len(query)][len(term)]


def file_read(file_name):
    file_lines = open(file_name, "r").readlines()

    for i in range(len(file_lines)):
        file_lines[i] = file_lines[i][:-1]
    return file_lines


if __name__ == "__main__":
    start_time = time.time()
    print("Start time: ", datetime.datetime.now())

    file_write = open("GED_result.txt", "w+")

    dict_list = file_read("dict.txt")
    term_list = file_read("misspell.txt")
    # print(len(term_list), "x", len(dict_list))

    # for i in range(len(term_list)):
    for i in range(len(term_list)):
        matching_distance = -20
        matching_string = []

        if term_list[i] in dict_list:
            matching_distance = len(term_list[i]) * MATCHING
            matching_string.append(term_list[i])
        else:
            for j in range(len(dict_list)):
                distance = global_edit_distance(term_list[i], dict_list[j])

                if distance > matching_distance:
                    matching_distance = distance
                    matching_string = [str(dict_list[j])]
                elif distance == matching_distance:
                    matching_string.append(str(dict_list[j]))

        print(i, ". The term: ", term_list[i])
        # print("Global edit distance: ", matching_distance)
        # print("Matching string: ", matching_string)
        # print()

        file_write.write("%s\n" % ','.join(matching_string))

    file_write.close()
    end_time = time.time()
    print("End time: ", datetime.datetime.now())
    running_time = end_time - start_time
    print("Total running time: ", running_time)
