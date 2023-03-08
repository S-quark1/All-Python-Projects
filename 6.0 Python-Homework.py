import random
print("Let's play")
py=['apple','banana','orange','lemon','cherry']
num=random.randint(0,len(py)-1)

word=py[num] #?letter сокрощенно от: num of letter in a word? 
print(py[num])#дз это сделать виселицу

x=10

while x>0:
    my=input("Enter your only 1 letter ")
    if my in word[0]:
        print("Yes")
    elif my not in word[0]:
        print("No")
    if my in word[1]:
        print("Yes")
    elif my not in word[1]:
        print("No")
    if my in word[2]:
        print("Yes")
    elif my not in word[2]:
        print("No")
    if word[3] in word:
        if my in word[3]:
            print("Yes")
        elif my not in word[3]:
            print("No")
        else:
            print()
    if word[4] in word:
        if my in word[4]:
            print("Yes")
        elif my not in word[4]:
            print("No")
        else:
            print()
    if word[5] in word:
        if my in word[5]:
            print("Yes")
        elif my not in word[5]:
            print("No")
        else:
            print()
    if word[6] in word:
        if my in word[6]:
            print("Yes")
        elif my not in word[6]:
            print("No")
        else:
            print()
##for i in range(0,len(letter)):
##    print(i)
##n=0
##while n<len(letter):
##    print(n)
##    n=n+1
##    print(letter[min(letter+n)])
##while True:
##    while n<len(letter):
##        if my[0]==letter[min(len(letter)+n)]: #в нашем случае letter это слово которое выбрал питон
##            print("yes")
##            n=n+1
##        elif my[0]!=letter[min(len(letter)+n)]:
##            print("no")
##            n=n+1
##        break
