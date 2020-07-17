n,m=map(int, input().split())
a=list(map(int, input().split()))

p=list()
for i in range(1,m+1):
    for j in a:
        if 2*i>=j:
            if ((2*i/j)-1)%2==0:
                p.append((i/j)-0.5)

x=list()
for i in a:
    for j in p:
        x.append(i*(j+0.5))

print(len(set(x)))
