#!/bin/bash

for size in small large
do
    for hz in 100 50 30 10
    do
        for m in 1 2 5 10
        do
            for n in 1 2 5 10 
            do
                python3 data_process_mqtt.py $hz $n $m $size
                python3 cpu_mem_process_mqtt.py $hz $n $m $size

                python3 data_process_ros.py $hz $n $m $size
                python3 cpu_mem_process_ros.py $hz $n $m $size
            done
        done
    done
done