# Increasing Order

n = int(input().strip())
arr = list(map(int, input().strip().split()))
moves = 0
for i in range(1, n):
    if arr[i] < arr[i - 1]:
        moves += arr[i - 1] - arr[i]
        arr[i] = arr[i - 1]
print(moves)
