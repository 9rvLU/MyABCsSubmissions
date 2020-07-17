import itertools


n, m, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))


accA = list(itertools.accumulate(a))
accB = list(itertools.accumulate(b))


cnt = 0
ans = 0
for i in range(len(accA)):
    for j in range(len(accB)):
        if k >= accA[i]+accB[j]:
            cnt = i+j
        
        ans = max(cnt, ans)


print(ans)