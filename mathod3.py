#구분구적법
import os

f = open("mathod3_result.txt", 'a')
f.close()
os.remove(r"mathod3_result.txt")
f = open("mathod3_result.txt", 'a')

n=10000000 #n값이 높을수록 근사값이 더 가까워짐
s=0
for k in range(n):
  s = s + (1/n) * ( (1-(k/n)**2)**.5 ) 
print(s*4, file=f)