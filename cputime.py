import numpy as np 
import matplotlib 
import matplotlib.pyplot as plt 
import pandas as pd 
import re 

f = open("t1.txt")
txt = f.read() 
time = re.findall(r'[\d\.\d]+', txt)
t1 = float(time[0]) 
e1 = float(time[1]) 

f2 = open("t2.txt")
txt2 = f2.read() 
time2 = re.findall(r'[\d\.\d]+', txt2)
t2 = float(time2[0]) 
e2 = float(time2[1]) 

f3 = open("t3.txt")
txt3 = f3.read() 
time3 = re.findall(r'[\d\.\d]+', txt3)
t3 = float(time3[0]) 
e3 = float(time3[1]) 


x = np.array([1,2,3])
my_xticks = ['stdcmalloc','tcmalloc','jemalloc']
plt.xticks(x, my_xticks)
plt.ylabel('time (ms)')


plt.errorbar(1, t1, yerr = e1, fmt ='*m') 
plt.errorbar(2, t2, yerr = e2, fmt ='*m') 
plt.errorbar(3, t3, yerr = e3, fmt ='*m') 
plt.savefig('cputime_malloc.png')
