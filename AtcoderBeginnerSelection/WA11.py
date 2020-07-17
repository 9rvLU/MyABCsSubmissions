n=int(input())
route=list([(0,0,0)])
for i in range(n):
    route.append(tuple(map(int, input().split())))

t=0
x=0
y=0

isAbleTravel=True

for i in range(len(route)-1):
    t=route[i+1][0]-route[i][0]
    x=route[i+1][1]-route[i][1]
    y=route[i+1][2]-route[i][2]

    if 0>t-abs(x)-abs(y):
        print('NO')
        isAbleTravel=False
        break
    elif 1==(t-abs(x)-abs(y))%2:
        print('NO')
        isAbleTravel=False
        break

if isAbleTravel==True:
    print('YES')