# The University of Melbourne
# School of Computing and Information Systems
# COMP90049 Knowledge Technologies
# Semester 01/2019
# Project A: Lexical Normalization
# Author: QUANG TRUNG LE


class Matching:
    def __init__(self):
        self.default_distance = 0
        self.greatest_distance = False
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
    

    def get_iv_distance(self, term):
        return 0
    

    def get_oov_distance(self, rhs, lhs):
        """
        Measure distance between 2 strings
        """
        return 0
        

    def measure_distance(self, term, dictionary_list):
        """
        Measure distance of a term
        """
        
        def is_oov(term, dictionary_list):
            return term not in dictionary_list
              
        # ==================== EDIT DISTANCE ====================
        matching_distance = self.get_default_distance
        matching_string = []

        if not is_oov(term, dictionary_list):
            matching_distance = self.get_iv_distance(term)
            matching_string = [term]
        else:
            for dict in dictionary_list:
                distance = self.get_oov_distance(term, dict)

                if (self.is_greatest_distance and (distance > matching_distance)) or (self.is_least_distance and (distance < matching_distance)):
                    matching_distance = distance
                    matching_string = [str(dict)]
                elif distance == matching_distance:
                    matching_string.append(str(dict))
        
        return [matching_distance, matching_string]
