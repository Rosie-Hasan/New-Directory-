import numpy as np 
import matplotlib 
import matplotlib.pyplot as plt 
import pandas as pd 


thread1 = pd.read_csv('./tcmalloc/prmon.athena.txt',delimiter='\t') 
thread2 = pd.read_csv('./stdcmalloc/prmon.athena.txt', delimiter='\t')
thread3 = pd.read_csv('./jemalloc/prmon.athena.txt', delimiter='\t')


x = thread1["Time"] - thread1.iat[0,0] 
x2 = thread2["Time"] -thread2.iat[0,0]
x3 = thread3["Time"] -thread3.iat[0,0]


y = thread1["pss"] * 1e-6
y2 = thread2["pss"] * 1e-6
y3 = thread3["pss"] * 1e-6


z = thread1["rss"] * 1e-6
z2 = thread2["rss"] * 1e-6
z3 = thread3["rss"] * 1e-6


#plt.subplot(2,1,1)
plt.figure(1)
plt.plot(x,y,label='tcmalloc', color='b')
plt.plot(x2,y2,label='stdcmalloc', color='m')
plt.plot(x3,y3,label='jemalloc', color='g')
plt.legend() 
plt.ylabel('pss (GB)') 
plt.xlabel('time (s)')
plt.savefig('stdc_vs_tc_vs_je_pssgraph.png')

#plt.subplot(2,1,2)
plt.figure(2)
plt.plot(x,z,label='tcmalloc', color='b')
plt.plot(x2,z2,label='stdcmalloc', color='m')
plt.plot(x3,z3,label='jemalloc', color='g')
plt.legend() 
plt.xlabel('time (s)')
plt.ylabel('rss (GB)')
plt.savefig('stdc_vs_tc_vs_je_rssgraph.png')
