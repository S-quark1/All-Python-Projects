import random
print("Let's play")
py=['apple','banana','orange','lemon','cherry','mandarin','blueberry']
num=random.randint(0,len(py)-1)

word=py[num]
#print(py[num])

x=10

while x>0 and word!="":
    my=input("Enter your only 1 letter ")
    if my in word:
        print("Yes")
        i=word.index(my)
        #print(i)
        word=word[:i]+word[i+1:]
        #print(word)
    else:
        print("No")
        x=x-1
if x==0:
    print("You lose")
    print("My word was", py[num])
if word=="":
    print("You win!")
    print("My word", py[num])
