import numpy as np
import matplotlib.pyplot as plt


def main():
    per_lat = (100 - 95) * 5
    xlocs = np.array([1, 2, 3, 4, 5, 6], dtype=np.int32)
    xlable = np.array(['8B', '80B', '200B', '500B', '1000B', '2000B'], dtype=str)
    # xlable = np.array(['1MB', '5MB', '10MB', '20MB', '30MB', '50MB'], dtype=str)
    
    # Load Data 1
    x1 = np.load('result/latency/1v1_small_30hz.npy')
    data1 = []
    for i in range(x1.shape[0]):
        data1.append(np.sort(x1[i,:])[:-per_lat]/1000)
    y1_mean = np.mean(np.array(data1), axis=1)
    x1 = xlocs

    # Load Data 2
    x2 = np.load('result/latency/1v2_small_30hz.npy')
    data2 = []
    for i in range(x2.shape[0]):
        data2.append(np.sort(x2[i,:])[:-per_lat]/1000)
    y2_mean = np.mean(np.array(data2), axis=1)
    x2 = xlocs

    # Load Data 3
    x3 = np.load('result/latency/1v5_small_30hz.npy')
    data3 = []
    for i in range(x3.shape[0]):
        data3.append(np.sort(x3[i,:])[:-per_lat]/1000)
    y3_mean = np.mean(np.array(data3), axis=1)
    x3 = xlocs

    # Load Data 4
    x4 = np.load('result/latency/1v10_small_30hz.npy')
    data4 = []
    for i in range(x4.shape[0]):
        data4.append(np.sort(x4[i,:])[:-per_lat]/1000)
    y4_mean = np.mean(np.array(data4), axis=1)
    x4 = xlocs

    # Plot
    fig, ax = plt.subplots()
    per = (0.5, 99.5)
    box_wid = 0.15

    # Plot Data 1
    c1='green'
    plt.plot(x1, y1_mean, c1)
    locs, labels = plt.xticks()
    box_pos1 = x1 - 3*np.array([box_wid/2*1.2], dtype=np.float64)
    bp1 = ax.boxplot(data1, positions=box_pos1 ,showfliers=True, widths=box_wid, whis=per, patch_artist=True,
            boxprops=dict(facecolor=(0,1,0,0.1), color=c1),
            capprops=dict(color=c1),
            whiskerprops=dict(color=c1),
            flierprops=dict(color=c1, markeredgecolor=c1),
            medianprops=dict(color='black'))
    
    # Plot Data2
    c2='blue'
    plt.plot(x2, y2_mean, c2)
    box_pos2 = x2 - np.array([box_wid/2*1.2], dtype=np.float64)
    bp2 = ax.boxplot(data2, positions=box_pos2 ,showfliers=True, widths=box_wid, whis=per, patch_artist=True,
            boxprops=dict(facecolor=(0,0,1,0.1), color=c2),
            capprops=dict(color=c2),
            whiskerprops=dict(color=c2),
            flierprops=dict(color=c2, markeredgecolor=c2),
            medianprops=dict(color='black'))
    
    # Plot Data3
    c3='orange'
    plt.plot(x3, y3_mean, c3)
    box_pos3 = x3 + np.array([box_wid/2*1.2], dtype=np.float64)
    bp3 = ax.boxplot(data3, positions=box_pos3 ,showfliers=True, widths=box_wid, whis=per, patch_artist=True,
            boxprops=dict(facecolor=(1,0.8,0,0.1), color=c3),
            capprops=dict(color=c3),
            whiskerprops=dict(color=c3),
            flierprops=dict(color=c3, markeredgecolor=c3),
            medianprops=dict(color='black'))
    
    # Plot Data3
    c4='red'
    plt.plot(x4, y4_mean, c4)
    box_pos4 = x4 + 3*np.array([box_wid/2*1.2], dtype=np.float64)
    bp4 = ax.boxplot(data4, positions=box_pos4 ,showfliers=True, widths=box_wid, whis=per, patch_artist=True,
            boxprops=dict(facecolor=(1,0,0,0.1), color=c4),
            capprops=dict(color=c4),
            whiskerprops=dict(color=c4),
            flierprops=dict(color=c4, markeredgecolor=c4),
            medianprops=dict(color='black'))
    

    plt.xticks(xlocs, xlable)
    ax.legend([bp1["boxes"][0], bp2["boxes"][0], bp3["boxes"][0], bp4["boxes"][0]], ['1v1', '1v2', '1v5', '1v10'], loc='upper left')
    plt.xlabel('Payload(B)')
    plt.ylabel('Latency(us )')
    # plt.xlim((-100,2100))
    # plt.ylim((0,3000))
    plt.title('ROS2 (30Hz)')
    plt.show()   
    

if __name__ == "__main__":
    main()