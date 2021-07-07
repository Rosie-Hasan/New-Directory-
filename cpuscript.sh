
grep 'PerfMonSvc.*evt' ./stdcmalloc/athena.log -A 1 | grep 'PerfMon.*<cpu.*ms' > t1.txt 
grep 'PerfMonSvc.*evt' ./tcmalloc/athena.log -A 1 | grep 'PerfMon.*<cpu.*ms' >t2.txt 
grep 'PerfMonSvc.*evt' ./jemalloc/athena.log -A 1 | grep 'PerfMon.*<cpu.*ms' >t3.txt 




python3 cputime.py 
