import queue


bookNum, algNum, understanding = map(int, input().split())
expList=queue.Queue()
for i in range(bookNum):
    expList.set(tuple(map(int, input().split())))


print(expList)