#!/bin/sh
echo "Runnign concat content pareto"
for filename in *; do
    cat "$filename" | grep 'True' >> concat_content_output_pareto.csv
done