# WA

import queue

k=int(input())

q=queue.Queue()
for i in range(1,10):
    q.put(i)
cnt=0
ans=0

while cnt<k:
    ans=q.get()
    for i in range(-1,2):
        if 0<ans+i<10:
            q.put(ans*10+ans+i)
        else:
            continue
    cnt+=1

print(ans)