# Middleware Benchmark Result
This is a repo storing benchmark and performance (Latency, CPU Usage, Memory Usage) between different middlewares(ROS2, MQTT, ZeroMQ, ROS).

You can find detail benchmark code in following repos:

* [**ROS2 Benchmark**](https://github.com/billy8874/benchmark_ros2)
* [**MQTT Benchmark**](https://github.com/Fuhoward0513/MQTT-benchmark)
* [**ZeroMQ Benchmark**](https://github.com/billy8874/benchmark_zmq)
* [**ROS Benchmark**](https://github.com/Fuhoward0513/ROS-Benchmark)

## Result Folder and Naming

```
.
    ├── ...
    ├── mqtt                    # MQTT
    │   ├── latency             # Latency
    │   └── cpu_mem             # CPU and Memory Usage
    ├── ros2
    │   ├── latency             # Latency
    │   └── cpu_mem             # CPU and Memory Usage
    ├── ros
    │   ├── latency             # Latency (Queue=10)
    │   ├── latency_q=1000      # Latency (Queue=1000)
    │   └── cpu_mem             # CPU and Memory Usage (Queue=10)
    ├── zmq
    │   ├── latency             # Latency
    │   └── cpu_mem             # CPU and Memory Usage
    └── ...
```
Naming: 1vN_xM_Payload_Frequency.npy --> Numpy array of shape: (6, 500): 6 for payload size (ascendant): small: 8B, 80B, 200B, 500B, 1000B, 2000B, large: 1MB, 5MB, 10MB, 20MB, 30MB, 50MB; 500 for max latency of 500 messages among all subscribers.



## Visualization
Visualize comparison between two or four different middleware, frequency, numbers of subscribers... by using following command.
```
python3 box_plot_2.py
python3 box_plot_4.py
```
Also, run following command to visualize histogram of latency.
```
python3 distribution.py
```
Note that you can modify filenames in python scripts to visualize specific combination of benchmark result.
