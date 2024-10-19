import matplotlib.pyplot as plt
import numpy as np
import sys

#python AAAGraphGenerator.py 3 data_1.csv data_2.csv data_3.csv Merge_Sort_Experiment

file = sys.argv[1]
title = sys.argv[2]
n = range(int(sys.argv[1]))
title = sys.argv[int(sys.argv[1])+2]
labels = ['Best','Worst','Average',]
first = False
for i in n:
    datapath = sys.argv[i+2]
    data = np.loadtxt(datapath, delimiter=',', skiprows=1)
    X = data[:,0]
    Y = data[:,1]
    if first:
        plt.plot(X,Y,label = labels[i])      
    else:
        first = True
        plt.plot(X,Y,label = labels[i])

plt.xlabel('input size (n)')
plt.ylabel('time (ms)')
plt.title(title)
# plt.xscale('log') 
# plt.yscale('log')
plt.ylim(ymin=0)
plt.xlim(xmin=0)
plt.legend(shadow = False, fancybox = True)
plt.savefig(title +'.pdf')
plt.close()