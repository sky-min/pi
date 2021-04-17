import math
import os
PI = math.pi
LIMIT = .000001

f = open("mathod4_result.txt", 'a')
f.close()
os.remove(r"mathod4_result.txt")
f = open("mathod4_result.txt", 'a')
n = 1; s = 1; a = 4

while(1):
    s = -s
    n = n + 1
    a = a + ( s * 4 * ( 1 / (2*n-1) ) )
    error = abs( a - PI )
    if( error < LIMIT ):
        print(n, a, file=f)
        break
    
