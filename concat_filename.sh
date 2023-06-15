#!/bin/sh
echo "Running concat_filename_all";
for filename in *; do
    awk '{print $0, FILENAME}' "$filename" > tmp
    cat tmp | sed "s/ /,/" > tmp2
    mv tmp2 "$filename"
    rm tmp
done