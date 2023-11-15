# lexical-normalization

1) 3 datasets: dictionary/dict.txt (the dictionary), test/misspell.txt (misspelled list), test/correct.txt (the list of relevant result)
2) src/SD_dictionary.py: create the Soundex dictionary, used in SD_2GRAM.py and SD_GED.py
3) src/GED.py: create approximate matching result using Global Edit Distance(GED) techniques, stored in "GED_result.txt"
4) src/2GRAM.py: create approximate matching result using N-gram techniques (N=2), stored in "2GRAM_result.txt"
5) src/SD_GED.py: create approximate matching result using Soundex and GED techniques, stored in "SD_GED_result.txt"
6) src/SD_2GRAM.py: create approximate matching result using Soundex and N-gram (N=2) techniques, stored in "SD_2GRAM_result.txt"
7) src/precision_accuracy.py: read data from result files and compare with "correct.txt"

NOTE:
- The execution time is printed on command window after the running process finishes.
- The dataset source is: Timothy Baldwin, Marie-Catherine de Marneffe, Bo Han, Young-Bum Kim, Alan Ritter, and Wei Xu. 2015. 
Shared tasks of the 2015 workshop on noisy user-generated text: Twitter lexical normalization and named entity recognition. 
In Proceedings of the Workshop on Noisy User-generated Text, pages 126-135.
