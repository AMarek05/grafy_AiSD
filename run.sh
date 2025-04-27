#!/bin/bash
> out.txt
for repr in Matrix List; do
    for algo in Kahn Tarjan; do
        > res.txt
        for (( i = 100; i <= 1000; i += 100 )); do
            echo "Sprawdzanie $repr $algo: $i" | tee -a out.txt
            echo `python main.py $i $repr $algo` | tee -a out.txt >> res.txt
        done
        printf "$repr $algo: "
        cat res.txt | awk -F';' '{t=$2; c++; s+=t; ss+=t*t} END {a=s/c; v=ss/c - a*a; printf "avg=%.10f stddev=%.10f\n", a, (v>=0)?sqrt(v):0}'
    done
done
exit 0
