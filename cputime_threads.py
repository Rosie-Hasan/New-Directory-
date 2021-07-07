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
time1 = x1[len(x1)-1]
memory1 = y1[len(y1)-1] 
mean1 = time1/memory1  
stdc.append(mean1)

x2 = stdc2["Time"]
y2 = stdc2["pss"] 
time2 = x2[len(x2)-1]
memory2 = y2[len(y2)-1] 
mean2 = time2/memory2  
stdc.append(mean2)

x4 = stdc4["Time"]
y4 = stdc4["pss"] 
time4 = x4[len(x4)-1]
memory4 = y4[len(y4)-1] 
mean4 = time4/memory4  
stdc.append(mean4)

threads = np.array([1,2,4])

z = mean1/threads 

plt.xlabel('threads') 
plt.ylabel('mean pss') 
plt.plot(threads, stdc, 'm*')
#plt.plot(threads,z)  
plt.show()

 #repeat for the 3 memory's 
 #add a simplefit straight line? one for each?  
