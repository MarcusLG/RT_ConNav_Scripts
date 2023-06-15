#!/bin/sh
echo "Running pareto merging"
for filename in *; do
    cat ../pareto/concat_content_output_pareto.csv | grep `echo $filename | sed -e 's/\.csv$//'` >> "$filename"
done