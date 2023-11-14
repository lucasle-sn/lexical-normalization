# The University of Melbourne
# School of Computing and Information Systems
# COMP90049 Knowledge Technologies
# Semester 01/2019
# Project A: Lexical Normalization
# Author: QUANG TRUNG LE - 987445

import fuzzy


def file_read(file_name):
    file_lines = open(file_name, "r").readlines()

    for i in range(len(file_lines)):
        file_lines[i] = file_lines[i][:-1]
    return file_lines


if __name__ == "__main__":
    SD_setup = fuzzy.Soundex(4)

    dict_list = file_read("dict.txt")
    dict_SD_write = open("dict_SD.txt", "w+")

    dict_list_SD = []

    for i in range(len(dict_list)):
        dict_list_SD.append([SD_setup(dict_list[i])])
        dict_SD_write.write("%s\n" % ','.join(dict_list_SD[i]))
    dict_SD_write.close()

