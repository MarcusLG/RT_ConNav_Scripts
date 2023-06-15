#!/bin/sh
echo "Running concat_content"
for filename in *; do
    cat "$filename" >> concat_content_output.csv
done