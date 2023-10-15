# Scammer Shamal

from math import comb 

T = int(input())

for i in range(T):
    K, S, a, b = map(int, input().split())

    print(int(comb(K-S, a)*comb(K-S-a, b)))
