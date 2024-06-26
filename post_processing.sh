#!/bin/bash

# shellcheck disable=SC2164
cd Data
echo "Available CSV files:"
ls

echo "Enter the names of 7 CSV files to process (separated by space):"
# shellcheck disable=SC2162
read -a INPUT_FILES

# Check if exactly 5 files are entered
if [ ${#INPUT_FILES[@]} -ne 7 ]; then
    echo "You must enter exactly 7 files."
    exit 1
fi

# shellcheck disable=SC2068
python3 ../post_processing.py --input-files ${INPUT_FILES[@]}
