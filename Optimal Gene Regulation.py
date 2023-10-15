# Optimal Gene Regulation

def minTranscriptionFactors(values):
    n = len(values)
    left_pass = [1] * n
    right_pass = [1] * n

    for i in range(1, n):
        if values[i] > values[i-1]:
            left_pass[i] = left_pass[i-1] + 1

    for i in range(n-2, -1, -1):
        if values[i] > values[i+1]:
            right_pass[i] = right_pass[i+1] + 1

    result = 0
    for i in range(n):
        result += max(left_pass[i], right_pass[i])

    return result

values = list(map(int, input().split()))
result = minTranscriptionFactors(values)
print(result)