import numpy as np 
import matplotlib 
import matplotlib.pyplot as plt 
import pandas as pd 
import re 

stdc1 = pd.read_csv('./stdcmalloc/prmon.athena.txt',delimiter='\t') 
stdc2 = pd.read_csv('./stdcmalloc2/prmon.athena.txt',delimiter='\t') 
stdc4 = pd.read_csv('./stdcmalloc4/prmon.athena.txt',delimiter='\t') 

stdc = [] 

x1 = stdc1["Time"]
y1 = stdc1["pss"] 
time1 = x1[len(x1)-1] - x1[0] 
memory1 = np.amax(y1)
mean1 = memory1/time1
print("one thread:", "time=",time1,"memory=", memory1,"mean=", mean1)   
stdc.append(memory1)

x2 = stdc2["Time"] 
y2 = stdc2["pss"] 
time2 = x2[len(x2)-1]- x2[0]
memory2 =  np.amax(y2) 
mean2 = memory2/time2  
print("two threads:", "time=",time2,"memory=", memory2,"mean=", mean2)   
stdc.append(memory2)

x4 = stdc4["Time"] 
y4 = stdc4["pss"] 
time4 = x4[len(x4)-1]-x4[0]
memory4 =  np.amax(y4)
mean4 = memory4/time4
print("4 threads:", "time=",time4,"memory=", memory4,"mean=", mean4)   
stdc.append(memory4)

threads = np.array([1,2,4])

z = mean1/threads 


plt.plot(threads, stdc, 'm*', label = "stdcmalloc")
#plt.plot(threads,z)  


 #repeat for the 3 memory's 
 #add a simplefit straight line? one for each?  

tc1 = pd.read_csv('./tcmalloc/prmon.athena.txt',delimiter='\t') 
tc2 = pd.read_csv('./tcmalloc2/prmon.athena.txt',delimiter='\t') 
tc4 = pd.read_csv('./tcmalloc4/prmon.athena.txt',delimiter='\t') 

tc = [] 

x1 = tc1["Time"]
y1 = tc1["pss"] 
time1 = x1[len(x1)-1] - x1[0] 
memory1 =  np.amax(y1) 
mean1 = memory1/time1
print("one thread:", "time=",time1,"memory=", memory1,"mean=", mean1)   
tc.append(memory1)

x2 = tc2["Time"] 
y2 = tc2["pss"] 
time2 = x2[len(x2)-1]- x2[0]
memory2 =  np.amax(y2)
mean2 = memory2/time2  
print("two threads:", "time=",time2,"memory=", memory2,"mean=", mean2)   
tc.append(memory2)

x4 = tc4["Time"] 
y4 = tc4["pss"] 
time4 = x4[len(x4)-1]-x4[0]
memory4 =  np.amax(y4)
mean4 = memory4/time4
print("4 threads:", "time=",time4,"memory=", memory4,"mean=", mean4)   
tc.append(memory4)

z = mean1/threads 

plt.plot(threads, tc, 'b*', label = "tcmalloc")


je1 = pd.read_csv('./jemalloc/prmon.athena.txt',delimiter='\t') 
je2 = pd.read_csv('./jemalloc2/prmon.athena.txt',delimiter='\t') 
je4 = pd.read_csv('./jemalloc4/prmon.athena.txt',delimiter='\t') 

je = [] 

x1 = je1["Time"]
y1 = je1["pss"] 
time1 = x1[len(x1)-1] - x1[0] 
memory1 =  np.amax(y1)
mean1 = memory1/time1
print("one thread:", "time=",time1,"memory=", memory1,"mean=", mean1)   
je.append(memory1)

x2 = je2["Time"] 
y2 = je2["pss"] 
time2 = x2[len(x2)-1]- x2[0]
memory2 =  np.amax(y2) 
mean2 = memory2/time2  
print("two threads:", "time=",time2,"memory=", memory2,"mean=", mean2)   
je.append(memory2)

x4 = je4["Time"] 
y4 = je4["pss"] 
time4 = x4[len(x4)-1]-x4[0]
memory4 =  np.amax(y4)
mean4 = memory4/time4
print("4 threads:", "time=",time4,"memory=", memory4,"mean=", mean4)   
je.append(memory4)

z = mean1/threads 

plt.plot(threads, je, 'g*', label = "jemalloc")

mi1 = pd.read_csv('./mimalloc_folder/prmon.athena.txt',delimiter='\t') 
mi2 = pd.read_csv('./mimalloc_folder2/prmon.athena.txt',delimiter='\t') 
mi4 = pd.read_csv('./mimalloc_folder4/prmon.athena.txt',delimiter='\t') 

mi = [] 

x1 = mi1["Time"]
y1 = mi1["pss"] 
time1 = x1[len(x1)-1] - x1[0] 
memory1 =  np.amax(y1)
mean1 = memory1/time1
print("one thread:", "time=",time1,"memory=", memory1,"mean=", mean1)   
mi.append(memory1)

x2 = mi2["Time"] 
y2 = mi2["pss"] 
time2 = x2[len(x2)-1]- x2[0]
memory2 =  np.amax(y2) 
mean2 = memory2/time2  
print("two threads:", "time=",time2,"memory=", memory2,"mean=", mean2)   
mi.append(memory2)

x4 = mi4["Time"] 
y4 = mi4["pss"] 
time4 = x4[len(x4)-1]-x4[0]
memory4 =  np.amax(y4)
mean4 = memory4/time4
print("4 threads:", "time=",time4,"memory=", memory4,"mean=", mean4)   
mi.append(memory4)

z = mean1/threads 

plt.plot(threads, mi, 'r*', label = "mimalloc")
 
plt.xlabel('threads') 
plt.ylabel('peak pss') 
plt.legend()
plt.savefig("peakpss_threading")
