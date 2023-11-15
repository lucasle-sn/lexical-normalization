test-2gram:
	python3 main.py -m "2gram" -i "test/misspell.txt" -o result_2gram.txt -l 20

test-ged:
	python3 main.py -m "ged" -i "test/misspell.txt" -o result_ged.txt -l 20

test-sd2gram:
	python3 main.py -m "sd2gram" -i "test/misspell.txt" -o result_sd2gram.txt -l 20

test-sdged:
	python3 main.py -m "sdged" -i "test/misspell.txt" -o result_sdged.txt -l 20

gen-soundex-dict:
	python3 tools/generate_soundex_dictionary.py