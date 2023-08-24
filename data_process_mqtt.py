import numpy as np
import csv
import sys

def main():
    fre = str(1000//int(sys.argv[1]))
    sub_num = sys.argv[2]
    pub_num = sys.argv[3]
    size = sys.argv[4]

    payloads = ['8', '80', '200', '500', '1000', '2000']
    np_data = np.zeros((6,500),dtype=np.double)

    for payload, i in zip(payloads, range(6)):
        filename = 'mqtt/output/N='+sub_num+'_M='+pub_num+'_st='+fre+'_small/'+'N='+sub_num+'_M='\
            +pub_num+'_st='+fre+'_payload='+payload+'.csv'
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            data = list(reader)
        np_data[i] = np.max(np.array(np.array(data)[1:], dtype=int), axis=1)

    filename = 'mqtt/output/1v'+sub_num+'_x'+pub_num+'_'+size+'_'+sys.argv[1]+'hz'
    np.save(filename,np_data)
    

if __name__ == "__main__":
    main()