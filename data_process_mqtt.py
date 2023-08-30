import numpy as np
import csv
import sys

def main():
    fre = str(1000//int(sys.argv[1]))
    sub_num = sys.argv[2]
    pub_num = sys.argv[3]
    size = sys.argv[4]

    if size == 'small':
        payloads = ['8', '80', '200', '500', '1000', '2000']
    else:
        payloads = ['1000000', '5000000', '10000000', '20000000', '30000000', '50000000']
    
    np_data = np.zeros((len(payloads),500),dtype=np.double)

    for payload, i in zip(payloads, range(len(payloads))):
        filename = 'mqtt/latency/tmp/N='+sub_num+'_M='+pub_num+'_st='+fre+'_payload='+payload+'.csv'
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            data = list(reader)
        try:
            np_data[i] = np.max(np.array(np.array(data)[1:], dtype=int), axis=1)
        except:
            np_data[i] = 0

    filename = 'mqtt/latency/1v'+sub_num+'_x'+pub_num+'_'+size+'_'+sys.argv[1]+'hz'
    np.save(filename,np_data)
    

if __name__ == "__main__":
    main()