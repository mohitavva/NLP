#! /bin/bash
python3 ./scripts/cleaner.py
echo "Cleaning Done"
python3 ./scripts/splitter.py
echo "Splitting Done"
python3 ./scripts/tokenizer.py
echo "Tokenizer Done"