n,m=map(int, input().split())
a=list()
for i in range(m):
    a.append(int(input()))

mod=1e9+7

inf=float('inf')

dp=[inf]*(n+1)
dp[0]=1
dp[1]=1

for i in a:
    dp[i]=0

for i in range(2,n+1):
    dp[i] = min(dp[i], dp[i-1]+dp[i-2]) % mod

print(int(dp[-1]))