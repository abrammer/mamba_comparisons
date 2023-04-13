#!/bin/bash

input="./all_services"
while read -r line
    do
    if [ -f ${line}.txt ]; then
        continue
    fi
    docker compose build --no-cache ${line} | tee ${line}.txt
    docker system prune -a -f
done < "$input"

for f in *.txt; do grep DONE $f >> artifacts/artifact/$f; done
