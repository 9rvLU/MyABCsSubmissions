s=input()

multple19=list()
for i in range(int(1000/19)+1):
    multple19.append(19*i)

ansCondidate=list()
for mlt in multple19:
    if s.count(str(mlt)) > 0:
        ansCondidate.append(mlt)

for i in range(len(ansCondidate)):
    ansCondidate[i]+=int(2000*ansCondidate[i]/19)

sum=0
for cnddt in ansCondidate:
    sum+=s.count(str(cnddt))

print(sum)