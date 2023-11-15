# The University of Melbourne
# School of Computing and Information Systems
# COMP90049 Knowledge Technologies
# Semester 01/2019
# Project A: Lexical Normalization
# Author: QUANG TRUNG LE


import numpy
from .Matching import Matching


MATCHING = 1
DELETION = -1
INSERTION = -1
REPLACEMENT = -1

class Ged(Matching):
    def __init__(self):
        Matching.__init__(self)
        self.default_distance = -100
        self.greatest_distance = True
        self.least_distance = False
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
    

    def update_distance_matrix(self, matrix, term, query):
        """ 
        Update distence matrix in GED method
        """
        
        def get_char_distance(rhs, lhs):
            """ 
            Get distance between 2 characters.
            Return MATCHING if equal, or else REPLACEMENT 
            """
            return MATCHING if rhs == lhs else REPLACEMENT    
        
        [row, column] = numpy.shape(matrix)
        for i in range(1, row):
            for j in range(1, column):
                insert_value = matrix[i - 1][j] + INSERTION
                delete_value = matrix[i][j - 1] + DELETION
                match_value = matrix[i - 1][j - 1] + get_char_distance(query[i - 1], term[j - 1])

                matrix[i][j] = max(insert_value, delete_value, match_value)

        return matrix


    def get_iv_distance(self, term):
        return len(term) * MATCHING


    def get_oov_distance(self, term, query):
        """
        Measure distance between 2 strings
        """
        
        def init_matrix(row, column):
            """ 
            Initialize distance matrix with Insrtion for rows and Deletion for column
            """
            matrix = numpy.zeros((row, column), dtype=int)

            for i in range(0, row):
                matrix[i][0] = i * INSERTION
            for j in range(0, column):
                matrix[0][j] = j * DELETION

            return matrix
        
        term_length = len(term)
        query_length = len(query)

        matrix = init_matrix(query_length + 1, term_length + 1)
        matrix = self.update_distance_matrix(matrix, term, query)

        return matrix[query_length][term_length]

