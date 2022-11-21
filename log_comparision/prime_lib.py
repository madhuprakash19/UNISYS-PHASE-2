from logCalculation import log_usingMath as lm
import os, psutil
process = psutil.Process(os.getpid())
m1=process.memory_info().rss
print("Memory usage: ",m1," bytes")

primeNoList=[] 
def isPrime(num):
    for i in range(2,num//2+1):
        if(num%i)==0:
            return 0
    return 1
for num in range(2,800):
    if(isPrime(num)):
        primeNoList.append(num)

for ele in primeNoList:
    lm.log(ele)

m2=process.memory_info().rss
print("Memory usage: ",m2," bytes")
print(m2-m1)








