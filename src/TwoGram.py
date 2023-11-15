# The University of Melbourne
# School of Computing and Information Systems
# COMP90049 Knowledge Technologies
# Semester 01/2019
# Project A: Lexical Normalization
# Author: QUANG TRUNG LE


class TwoGram:
    def __init__(self):
        pass


    def get_distance(self, rhs, lhs):
        """
        Measure distance between 2 strings
        """
        
        def create_twogram_array(string):
            """
            Create an array of two-character sequences of string
            """
            gram = [string[0]]
            for i in range(len(string) - 1):
                gram.append(string[i:i + 2])
            gram.append(string[len(string) - 1])
            return gram

        rhs_gram = create_twogram_array(rhs)
        lhs_gram = create_twogram_array(lhs)
        similarity = 0

        for i in range(len(rhs_gram)):
            for j in range(len(lhs_gram)):
                if rhs_gram[i] == lhs_gram[j]:
                    similarity = similarity + 1
                    del lhs_gram[j] # Remove element at index j
                    break

        return len(rhs)+len(lhs) + 2 - 2*similarity
