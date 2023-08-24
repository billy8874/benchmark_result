#!/bin/bash

python3 data_process_mqtt.py 100 1 1 small
python3 data_process_mqtt.py 100 5 1 small
python3 data_process_mqtt.py 100 10 1 small
python3 data_process_mqtt.py 100 5 5 small
python3 data_process_mqtt.py 100 5 10 small
# python3 cpu_mem_process_mqtt.py 100 1 1 small
# python3 cpu_mem_process_mqtt.py 100 5 1 small
# python3 cpu_mem_process_mqtt.py 100 10 1 small
# python3 cpu_mem_process_mqtt.py 100 5 5 small
# python3 cpu_mem_process_mqtt.py 100 5 10 small

# python3 data_process_ros.py 100 1 1 small
# python3 data_process_ros.py 100 5 1 small
# python3 data_process_ros.py 100 10 1 small
# python3 data_process_ros.py 100 5 5 small
# python3 data_process_ros.py 100 5 10 small
# python3 cpu_mem_process_ros.py 100 1 1 small
# python3 cpu_mem_process_ros.py 100 5 1 small
# python3 cpu_mem_process_ros.py 100 10 1 small
# python3 cpu_mem_process_ros.py 100 5 5 small
# python3 cpu_mem_process_ros.py 100 5 10 small