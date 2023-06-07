concat_filename_all () {
    echo "Running concat_filename_all";
    for filename in *; do
        awk '{print $0, FILENAME}' "$filename" > tmp
        mv tmp "$filename"
    done
}
