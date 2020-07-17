n,Y=map(int, input().split())

x=int(Y/10000)
y=int((Y-10000*x)/5000)
z=int((Y-10000*x-5000*y)/1000)

isAnable=False

while(n>=x+y+z):
    if n==x+y+z:
        print(x,y,z)
        isAnable=True
    
    if 0==(n-x-y-z)%4:
        y-=1
        z+=5
        if y<0:
            break
    else:
        x-=1
        y+=2
        if x<0:
            break

if isAnable==False:
    print(-1,-1,-1)