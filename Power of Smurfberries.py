# Power of Smurfberries

t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    ans = [0] * n
    total_sum = sum(a)
    v = [(a[i], i) for i in range(n)]
    v.sort()

    pre = [0] * n
    pre[0] = v[0][0]
    for i in range(1, n):
        pre[i] = pre[i-1] + v[i][0]

    mp = {v[i][0]: i for i in range(n)}
    
    for i in range(n):
        k = mp[v[i][0]]
        ind = v[i][1]
        ans[ind] = (k+1)*v[i][0] - pre[k] + (k+1) + (total_sum - pre[k]) - (n-k-1)*v[i][0] + (n-k-1)

    print(" ".join(map(str, ans)))
