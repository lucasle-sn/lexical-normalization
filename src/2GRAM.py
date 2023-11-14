# The University of Melbourne
# School of Computing and Information Systems
# COMP90049 Knowledge Technologies
# Semester 01/2019
# Project A: Lexical Normalization
# Author: QUANG TRUNG LE - 987445

import time
import datetime


def get_max(value_list):
    max_value = value_list[0]
    for i in value_list:
        if i > max_value:
            max_value = i
    return max_value


def file_read(file_name):
    file_lines = open(file_name, "r").readlines()

    for i in range(len(file_lines)):
        file_lines[i] = file_lines[i][:-1]
    return file_lines


def oov_category(term_list, dict_list):
    # term_list_sub = []
    term_location = []

    for i in range(len(term_list)):
        if term_list[i] not in dict_list:
            # term_list_sub.append(term_list[i])
            term_location.append(i)

    return term_location


def two_gram_create(element):
    string_sub = [element[0]]
    for i in range(len(element) - (2 - 1)):
        string_sub.append(element[i:i + 2])
    string_sub.append(element[len(element) - 1])
    return string_sub


def two_gram_distance(element1, element2):
    element1_gram = two_gram_create(element1)
    element2_gram = two_gram_create(element2)
    similarity = 0

    for i in range(len(element1_gram)):
        for j in range(len(element2_gram)):
            if element1_gram[i] == element2_gram[j]:
                similarity = similarity + 1
                element2_gram = array_remove(j, element2_gram)
                break

    return len(element1)+len(element2) + 2 - 2*similarity


def array_remove(index, array):
    array_sub = []
    for i in range(index):
        array_sub.append(array[i])
    for i in range(index, len(array) - 1):
        array_sub.append(array[i+1])
    return array_sub


if __name__ == "__main__":
    start_time = time.time()
    print("Start time: ", datetime.datetime.now())

    matching_result_write = open("2GRAM_result.txt", "w+")
    dict_list = file_read("dict.txt")
    term_list = file_read("misspell.txt")
    # print(len(term_list), "x", len(dict_list))

    # ==================== SHORTEN OOV LIST ====================
    oov_location = oov_category(term_list, dict_list)

    # ==================== TWO-GRAM DISTANCE ====================
    matching_distance = []
    matching_string = []

    for i in range(len(term_list)):
        matching_distance.append(50)
        matching_string.append([])

        if i not in oov_location:
            matching_distance[i] = 0
            matching_string[i] = [term_list[i]]
        else:
            for j in range(len(dict_list)):
                distance = two_gram_distance(term_list[i], dict_list[j])

                if distance < matching_distance[i]:
                    matching_distance[i] = distance
                    matching_string[i] = [str(dict_list[j])]
                elif distance == matching_distance[i]:
                    matching_string[i].append(str(dict_list[j]))

        print(i, ". The term: ", term_list[i])
        print("Global edit distance: ", matching_distance[i])
        print("Matching string: ", matching_string[i])
        print()

        matching_result_write.write("%s\n" % ','.join(matching_string[i]))

        # if i == 100:
        #     break

    matching_result_write.close()
    end_time = time.time()
    print("End time: ", datetime.datetime.now())
    running_time = end_time - start_time
    print("Total running time: ", running_time)

