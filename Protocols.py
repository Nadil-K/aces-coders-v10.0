# Protocols

def num_protocols(n):
    side_length = int(n ** 0.5)
    if side_length < 4:
        return 0
    elif side_length % 2 == 0:
        return 2
    else:
        return 1

n = int(input())
protocols = num_protocols(n)
print(protocols)
