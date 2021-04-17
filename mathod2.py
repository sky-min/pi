#난수를 이용해 점을 찍어 원의 면적을 계산하여 원주율을 구한다
import random
import os

n=1000000 #n값이 높을 수 록 더 자세한 근사값이 나오지만 cpu를 많이 먹는다
f = open("mathod2_result.txt", 'a')
f.close()
os.remove(r"mathod2_result.txt")
f = open("mathod2_result.txt", 'a')
count=0
for i in range(n):
  x=random.random()
  y=random.random()
  if(x*x+y*y<1):
    count=count+1
a=4*count/n
print(a,file=f)