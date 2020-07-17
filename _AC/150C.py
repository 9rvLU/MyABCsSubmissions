import itertools

n=int(input())
p=tuple(map(int, input().split()))
q=tuple(map(int, input().split()))

tmp=list()
for i in range(n):
    tmp.append(i+1)
perm=list(itertools.permutations(tmp))

print(abs(perm.index(p)-perm.index(q)))