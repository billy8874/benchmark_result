import numpy as np
import matplotlib.pyplot as plt


def main():
    xlocs = np.array([1, 2, 3, 4, 5, 6], dtype=np.int32)
    xlable = np.array(['8B', '80B', '200B', '500B', '1000B', '2000B'], dtype=str)
    # Load Data 1
    x1 = np.load('ros2/cpu_mem/1v1_x1_small_100hz.npy')

    # Load Data 2
    x2 = np.load('mqtt/cpu_mem/1v1_x1_small_100hz.npy')

    # Load Data 3
    x3 = np.load('ros/cpu_mem/1v1_x1_small_100hz.npy')

    # Load Data 4
    x4 = np.load('zmq/cpu_mem/1v1_x1_small_100hz.npy')

    # Plot CPU
    plt.plot(xlocs, x1[:, 0]*100)
    plt.plot(xlocs, x2[:, 0]*100)
    plt.plot(xlocs, x3[:, 0]*100)
    plt.plot(xlocs, x4[:, 0]*100)
    plt.xticks(xlocs, xlable)
    plt.legend(['ros2', 'mqtt', 'ros', 'zmq'], loc='upper left')
    plt.xlabel('Payload(B)')
    plt.ylabel('CPU Usage(%)')
    # plt.xlim((-100,2100))
    # plt.ylim((0,5000))
    plt.title('CPU Usage 1v1 100hz')
    plt.show() 
    

if __name__ == "__main__":
    main()