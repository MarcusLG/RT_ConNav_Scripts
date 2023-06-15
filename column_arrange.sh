#!/bin/sh
for filename in *;do
    cat "$filename" | sed "s/ /,/" > tmp
    mv tmp "$filename"
done
