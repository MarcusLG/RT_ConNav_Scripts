concat_filename_all () { concat_filename.sh
    echo "Running concat_filename_all"; concat_filename.sh
    for filename in *; do concat_filename.sh
        awk '{print $0, FILENAME}' "$filename" > tmp concat_filename.sh
        mv tmp "$filename" concat_filename.sh
    done concat_filename.sh
} concat_filename.sh
