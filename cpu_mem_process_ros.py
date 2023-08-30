import numpy as np
import csv
import sys

def main():
    fre = sys.argv[1]
    sub_num = sys.argv[2]
    pub_num = sys.argv[3]
    size = sys.argv[4]

    usage = np.zeros((6, 2),dtype=np.double)
    payloads = []

    if size=='large': 
        payloads = ['1MB', '5MB', '10MB', '20MB', '30MB', '50MB']
    elif size=='small':
        payloads = ['8', '80', '200', '500', '1000', '2000']
    
    for payload, i in zip(payloads, range(len(payloads))):
        filename = 'ros/cpu_mem/tmp/N='+sub_num+'_M='+pub_num+'_fre='+fre+'_payload='+payload+'.csv'
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            data = list(reader)
        usage[i] = np.mean(np.array(data, dtype=float), axis=0)
        # data[0].pop()
        # np_data[i] = np.array(data, dtype=np.double)

    # print("CPU and Memory Usage: ", usage)
    # Save to .npy file
    filename = 'ros/cpu_mem/1v'+sub_num+'_x'+pub_num+'_'+size+'_'+sys.argv[1]+'hz'
    np.save(filename,usage)
    
if __name__ == "__main__":
    main()