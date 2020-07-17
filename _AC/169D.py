n = int(input())


# 素因数分解する関数(https://qiita.com/snow67675476/items/e87ddb9285e27ea555f8)
def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr


fct=factorization(n)


cnt = 0
tmp = 0
ma = 0
for t in fct:
    if t[0] == 1:
        break

    tmp = t[1]
    ma = 1
    while tmp >= ma:
        tmp -= ma
        ma += 1
        cnt += 1


print(cnt)
