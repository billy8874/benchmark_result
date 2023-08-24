import numpy as np
import csv
import sys

def main():
    fre = sys.argv[1]
    sub_num = sys.argv[2]
    pub_num = sys.argv[3]
    size = sys.argv[4]

    payloads = ['8', '80', '200', '500', '1000', '2000']
    np_data = np.zeros((6,500),dtype=np.double)

    for payload, i in zip(payloads, range(6)):
        filename = 'ros/output/N='+sub_num+'_M='+pub_num+'_fre='+fre+'_small/'+'N='+sub_num+'_M='\
            +pub_num+'_fre='+fre+'_payload='+payload+'.csv'
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            data = list(reader)
        np_data[i] = np.max(np.array(data, dtype=int)[:,5:], axis=0)

    filename = 'ros/output/1v'+sub_num+'_x'+pub_num+'_'+size+'_'+fre+'hz'
    np.save(filename,np_data)
    

if __name__ == "__main__":
    main()