import itertools

aLength, aMax, subscriptListLength = map(int, input().split())
subscriptList=list()
for i in range(subscriptListLength):
    subscriptList.append(tuple(map(int, input().split())))

ans=0
sum=0
tmpList = list()
for i in range(1,aMax+1):
    tmpList.append(i)
a=list(itertools.combinations_with_replacement(tmpList, aLength))
for i in a:
    print(i)
    for cndtn in subscriptList:
        if cndtn[2] == i[cndtn[1]]-i[cndtn[0]]:
            sum+=cndtn[3]
        ans=max(sum,ans)
        sum=0

print(ans)
                                        

# [WA] DP approach
# 
# aLength, aMax, subscriptListLength = map(int, input().split())
# subscriptList=list()
# for i in range(subscriptListLength):
#     subscriptList.append(tuple(map(int, input().split())))
# 
# subscriptList.sort(key=lambda tup: tup[0])
# # print(subscriptList)
# 
# a=[[0]*(aLength+1)]*2
# 
# for conditions in subscriptList:
#     a[conditions[0]][0]
#     a[][1]
# 
# print(a)