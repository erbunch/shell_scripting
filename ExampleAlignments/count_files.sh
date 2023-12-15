#!/bin/bash

count_files(){
    local dir="$1"
    local log_file="$2"

    file_count=$(find "$dir" -maxdepth 1 -type f | wc -l)
    echo "Files in $dir: $file_count" >> "$log_file"

    nested_dirs=($(find "$dir -maxdepth 1 -type d ! -name ".""))

    if [${#nested_dirs[@]} -gt 0 ]; then
        for nested_dir in "${nested_dirs[@]}"; do
            count_files "$nested_dir" "$log_file"
         done
    fi
}

main(){
    if [ "$#" -ne 1 ]; then
        echo "Usage: $0 <directory_path>"
        exit 1
    fi

    target_dir="$1"
    log_file="log.txt"

    > "$log_file"

    count_files "$target_dir" "$log_file"

    echo "Counting completed. Results written to "$log_file"
}

main "$@"
