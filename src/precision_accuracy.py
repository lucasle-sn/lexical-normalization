# The University of Melbourne
# School of Computing and Information Systems
# COMP90049 Knowledge Technologies
# Semester 01/2019
# Project A: Lexical Normalization
# Author: QUANG TRUNG LE - 987445

result_file = ["GED_result.txt", "2GRAM_result.txt", "SD_GED_result.txt", "SD_2GRAM_result.txt"]


def file_read(file_name):
    file_lines = open(file_name, "r").readlines()

    for i in range(len(file_lines)):
        file_lines[i] = file_lines[i][:-1]
    return file_lines


def matching_count(list):
    matching = 0
    for element in list:
        if element == True:
            matching = matching + 1
    return matching


def test_type(index):
    string = ""
    if index == 0:
        string = "Global edit distance:"
    elif index == 1:
        string = "N-gram(N=2):"
    elif index == 2:
        string = "Soundex & GED:"
    elif index == 3:
        string = "Soundex & N-gram(N=2):"
    return string


if __name__ == "__main__":
    correct_list = file_read("correct.txt")

    for count in range(len(result_file)):
        return_list = file_read(result_file[count])
        matching = []
        precision = []

        for i in range(len(return_list)):
            matching.append(False)
            precision.append(0)

            return_count = str(return_list[i]).split(",")

            for j in range(len(return_count)):
                if correct_list[i] == return_count[j]:
                    matching[i] = True
                    precision[i] = 1
                    break
            precision[i] = precision[i]*100/len(return_count)

        print(test_type(count))
        accuracy = matching_count(matching)*100/len(matching)
        print("Accuracy: ", accuracy)

        sum_precision = 0
        for i in range(len(precision)):
            sum_precision = sum_precision + precision[i]
        average_precision = sum_precision/len(precision)
        print("Precision: ", average_precision)
        print()
