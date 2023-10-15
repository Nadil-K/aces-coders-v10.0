# Colorful Lichess

import math

n,m = map(int,input().split(' '))
x = int(input())
arr=[]

while n-2>0 and m-2>0:
    arr.append(math.ceil(n*m/2)-math.ceil(((n-2)*(m-2))/2))
    n-=2
    m-=2
if n<=0 and m<=0:
    pass
else:
    arr.append(math.ceil(n*m/2))

try:
    print(arr[x-1])
except:
    print(0)