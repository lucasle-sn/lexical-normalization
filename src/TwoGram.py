# The University of Melbourne
# School of Computing and Information Systems
# COMP90049 Knowledge Technologies
# Semester 01/2019
# Project A: Lexical Normalization
# Author: QUANG TRUNG LE


class TwoGram:
    def __init__(self):
        self.default_distance = 100
        self.greatest_distance = False
        self.least_distance = True
        pass


    @property
    def get_default_distance(self):
        return self.default_distance


    @property
    def is_greatest_distance(self):
        return self.greatest_distance


    @property
    def is_least_distance(self):
        return self.least_distance
    

    def get_iv_distance(self, term):
        return 0
    

    def get_oov_distance(self, rhs, lhs):
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
