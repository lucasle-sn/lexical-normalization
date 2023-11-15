# The University of Melbourne
# School of Computing and Information Systems
# COMP90049 Knowledge Technologies
# Semester 01/2019
# Project A: Lexical Normalization
# Author: QUANG TRUNG LE


def read_lines(filename):
    lines = open(filename, "r").readlines()

    for i in range(len(lines)):
        lines[i] = lines[i][:-1]
    return lines

