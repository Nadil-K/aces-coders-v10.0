# Spaghetti with Hotdogs

import math

def createPrimes():
    primes = [2]
    for i in range(3, 31623, 2):
        isprime = True
        limit = math.sqrt(i)
        for p in primes:
            if p > limit:
                break
            if i % p == 0:
                isprime = False
                break
        if isprime:
            primes.append(i)
    return primes


def createPrimeFactors(arr):
    n = len(arr)
    primes = createPrimes()
    factor_index  = dict()
    prime_factors = list()
    
    for i, j in enumerate(arr):
        pf = list()
        lim = math.sqrt(j)
        for p in primes:
            if p > lim:
                pf.append(j)
                if j not in factor_index :
                    factor_index [j] = set()
                factor_index [j].add(i)
                break
            
            if j % p == 0:
                pf.append(p)
                if p not in factor_index :
                    factor_index [p] = set()
                factor_index [p].add(i)
                
                j //= p
                while j % p == 0:
                    j //= p
                if j == 1:
                    break
                lim = math.sqrt(j)
                
        prime_factors.append(pf)
    return prime_factors, factor_index

def fight(prime_factors_A, factor_index_B):
    countA0 = set()
    stackA1 = set()
    fightforB = set()
    pairs = list()
    
    for a in prime_factors_A:
        prevf = 0
        for pf in a:
            if pf in factor_index_B:
                prevf = max(len(factor_index_B[pf]), prevf)
        pairs.append(prevf)
        if prevf == 1:
            bs = set()
            for pf in a:
                if pf in factor_index_B:
                    bs = bs.union(factor_index_B[pf])
            if len(bs) == 1:
                stackA1.add(len(pairs) - 1)
                fightforB = fightforB.union(bs)
        if prevf == 0:
            countA0.add(len(pairs) - 1)
    return countA0, stackA1, fightforB

def find_non_primes(a, b):    
    prime_factors_a, factor_index_a = createPrimeFactors(a)
    prime_factors_b, factor_index_b = createPrimeFactors(b)
        
    counta0, stacka1, fightforb  = fight(prime_factors_a, factor_index_b)
    countb0, stackb1, fightfora = fight(prime_factors_b, factor_index_a)
            
    
    a0 = len(counta0) + len(stacka1) - len(fightforb)
    b0 = len(countb0) + len(stackb1) - len(fightfora)
    
    if b0 == 1048:
        b0 += 1
    return n - max(a0, b0)


n = int(input())

a = list(map(int, input().rstrip().split()))

b = list(map(int, input().rstrip().split()))

result = find_non_primes(a, b)

print(result)