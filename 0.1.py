def fizzBuzz(n):
    # Write your code here
    for i in range(1,n):
        if i%3==0 and i%5==0:
            print("FizzBuzz")
        elif i%5==0:
            print("Buzz")
        elif i%3==0:
            print("Fizz")
        else:
            print(i)
n=int(input())
n=n+1
fizzBuzz(n)
if a1>b1 and b1>c1:
        h=a1-c1
    if b1>a1 and a1>c1:
        h=b1-c1
    if b1==a1 and a1>c1:
        h=a1-c1
    if a1>c1 and c1>b1:
        h=a1-b1
    if a1==c1 and c1>b1:
        h=a1-b1
    if c1>a1 and a1>b1:
        h=c1-b1
    if c1>b1 and b1>a1:
        h=c1-a1
    if c1==b1 and b1>a1:
        h=c1-a1
    if b1>c1 and c1>a1:
        h=b1-a1
    if a1>b1 and b1==c1:
        h=a1-c1
    if b1>a1 and a1==c1:
        h=b1-c1
    if c1>b1 and b1==a1:
        h=c1-a1
    if a1==b1 and b1==c1:
        h=a1
