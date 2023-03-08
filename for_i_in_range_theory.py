num=[2,1,3,5,6,8,7,9,4,10]

for k in range(len(num)): #len-length это длина списка, например здесь 7 чисел
##    if num[k]%2==0:
##        print(num[k])
    print(k,num[k])
    print()
for k in range(len(num)):
    if k%2==0:
        print(k)
        print()
for k in range(len(num)):
    if k%2==1:
        print(k)
        print()
for k in range(0,len(num),3):
    print(k)
    print()
    #or
##for k in range(len(num)):
##    if k%3==0:
##        print(k)

sum=0
for k in range(len(num)):
    sum=sum+num[k]
print(sum)
    #or
print(sum(num))
print()

print(max(num)) #max-максимальное число
print(min(num)) #min-минимальное число
max=num[0]
for k in range(len(num)):
    if max==max<num[k]:
        max=num[k]
print(max)

min=num[0]
for k in range(len(num)):
    if min==min>num[k]:
        min=num[k]
print(min)
    



