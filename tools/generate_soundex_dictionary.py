# The University of Melbourne
# School of Computing and Information Systems
# COMP90049 Knowledge Technologies
# Semester 01/2019
# Project A: Lexical Normalization
# Author: QUANG TRUNG LE

#!/usr/bin/env python

import jellyfish
from helper import read_lines


if __name__ == "__main__":
    dictionary_list = read_lines("dictionary/dict.txt")
    dictionary_sd = open("dict_soundex.txt", "w+")

    for term in dictionary_list:
        term_sd = jellyfish.soundex(term)
        dictionary_sd.write("%s\n" % ''.join(term_sd))
    dictionary_sd.close()
