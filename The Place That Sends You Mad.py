# The Place That Sends You Mad

n = int(input())
a = list(map(int, input().split()))

time = 0
if (n%2 == 1):
    a.append(0)
    
for i in range(n//2):
    if len(a) <= 2:
        time += max(a[0], a[1])
        break
    first_three = a[:3]
    differences = [(abs(first_three[i] - first_three[j]), i, j)
                   for i in range(3) for j in range(i+1, 3)]
    min_diff = min(differences, key=lambda x: x[0])
    time += max(a[min_diff[2]],a[min_diff[1]])
    # print(min_diff,min_diff[1])
    del a[min_diff[2]]
    del a[min_diff[1]]
    # print(a, time)
    
print(time)
