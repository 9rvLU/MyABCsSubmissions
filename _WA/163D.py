import itertools

n,k=map(int, input().split())

mod=1e9+7

l=list()
for i in range(n+1):
    l.append(i)

ans=0
tmpl=list()
for i in range(k,len(l)+1):
    for j in list(itertools.combinations(l,i)):
        tmpl.append(sum(j))
    ans+=len(set(tmpl))%mod
    tmpl.clear()

print(int(ans))