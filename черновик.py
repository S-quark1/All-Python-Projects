##s=['кар','мяу','гав','гав','кар']
##res={}
##prev=''
##for w in s:
##    if prev in res:
##        res[prev].append(w)
##        print('if: '+str(res))
##    else:
##        res[prev]=[w,]
##        print('else: '+str(res))
##    prev=w
#print(res)


####if int(n[0])>=1 and int(n[0])<=10**9 and int(n[1])>=2 and int(n[1])<=10:
####    if int(n[1])==2:
####        b=n[0][::-1]*2
####    else:
####        b=n[0][::-1]
####    print(b)
##n=int(input())
##a=int(input())
##if n>=1 and n<=10**6 and a>=0 and a<=10**6:
##    b=0
##    for i in range(1,n+1):
##        for j in range(i,n+1):
##            if j-i<=a:
##                b+=1
##    print(b)

#print(s[:2])
import csv

score=input("whats ya score")
username=input("whats ya name")

with open ("protleader.csv", "a", newline='') as file:
    fields=['score', 'name']
    writer=csv.DictWriter(file, fieldnames=fields)
    writer.writerow({'score' : score, 'name' : username})

with open ("protleader.csv", "r") as file:
    sortlist=[]
    reader=csv.reader(file)
    for i in reader:
        sortlist.append(i)
for i in range(len(sortlist)):
    if i != 0:
        sortlist[i][0]=int(sortlist[i][int(0)])


print("")

print("Unsorted:")
for i in range(len(sortlist)):
    print(sortlist[i])


for i in range(555):
    for i in range(len(sortlist)-1):
        if i != 0:
            if sortlist[i][0] < sortlist[i+1][0]:
                change=sortlist[i]
                sortlist[i]=sortlist[i+1]
                sortlist[i+1]=change


print("")

print("Sorted and cut:")
for i in range(len(sortlist)-1):
    print(sortlist[i])
