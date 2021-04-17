#아르키메데스를 코딩으로 구현
import math
import os

diameter=2
polygon=6
side=1

n=20 

os.remove(r"mathod1_result.txt")

f = open("mathod1_result.txt", 'a')

for i in range(n):
    polygon = polygon * 2
    side = ( 2 - ( 4 - side**2 ) **.5 ) **.5
    pi = side * polygon / diameter
    print(polygon, ":", pi, file=f)
f.close()