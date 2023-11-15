test-2gram:
	python3 main.py -m "2gram" -i "test/misspell.txt" -o result_2gram.txt -l 20

test-ged:
	python3 main.py -m "ged" -i "test/misspell.txt" -o result_ged.txt -l 20
