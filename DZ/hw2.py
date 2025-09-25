a = list(map(int,input().split()))
p1 = 0
p2 = len(a) - 1
ans = 0

while p1 < p2:
    S = min(a[p1], a[p2]) * (p2 - p1)
    ans = max(ans, S)
    if a[p1] < a[p2]:
        p1 += 1
    else:
        p2 -= 1


print(ans)