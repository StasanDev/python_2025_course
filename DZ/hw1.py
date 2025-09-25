a = list(map(int,input().split()))
a.sort()
p1 = 0
p2 = len(a) - 1
ans = list(range(len(a)))
n = p2

if n >= 0:
    while p1 < p2:
        #print(ans)
        if abs(a[p1]) > abs(a[p2]):
            ans[n] = abs(a[p1])
            p1 += 1
        else:
            ans[n] = abs(a[p2])
            p2 += 1
        n -= 1
    ans[n] = a[p2]


print(ans)