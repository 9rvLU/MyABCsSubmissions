n,k = map(int, input().split())
a = list(map(int, input().split()))


now = 1
repeat = list()


while now not in repeat:
    repeat.append(now)
    now = a[now-1]


print(repeat)
repeat = repeat[repeat.index(now):]


now = repeat[0]
k = k % (len(repeat))


for i in range(k+1):
    now = a[now-1]


print(now)