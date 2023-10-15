# XORmium

def compute_T(A, V):
    return (A ^ A) + (V ^ A)

A, V = map(int, input().split())
print(compute_T(A, V))
