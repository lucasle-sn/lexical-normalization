# lexical-normalization

* 3 given datasets: `dictionary/dict.txt` (dictionary), `test/misspell.txt` (misspelling list), `test/correct.txt` (the list of correct result).
* `tools/generate_soundex_dictionary.py`: create the Soundex dictionary, which is used for normalization techniques using Soundex + N-gram/GED.
* `src/Matching.py`: Define the base class `Matching` for all approximate matching methods.
* `src/Ged.py`: Define `Ged` class, which contains approximate matching algorithm of Global Edit Distance(GED).
* `src/TwoGram.py`: Define `TwoGram` class, which contains approximate matching algorithm of N-Gram (N=2).
* `main.py`: Main program
* `tool/precision_accuracy.py`: Read data from result files and compare with `test/correct.txt`, print out precision and accuracy.
* `tools/generate_soundex_dictionary.py`: Tool to generate soundex version of queries in dictionary `dictionary/dict.txt`.

NOTE:
- The execution time is printed on command window after the running process finishes.
- The dataset source is: Timothy Baldwin, Marie-Catherine de Marneffe, Bo Han, Young-Bum Kim, Alan Ritter, and Wei Xu. 2015. 
Shared tasks of the 2015 workshop on noisy user-generated text: Twitter lexical normalization and named entity recognition. 
In Proceedings of the Workshop on Noisy User-generated Text, pages 126-135.
