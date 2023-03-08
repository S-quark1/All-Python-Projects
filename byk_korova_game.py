import random
print("Let's play!")
while True:
    a=random.randint(1,9)
    b=random.randint(1,9)
    c=random.randint(1,9)
    
    if a!=b!=c:
        break
py=(str(a)+str(b)+str(c))
while True:
    my=input()
    if py[0]==my[0]:
        print("byk")
    elif py[0]==my[1] or py[0]==my[2]:
        print("cow")
    if py[1]==my[1]:
        print("byk")
    elif py[1]==my[2] or py[1]==my[0]:
        print("cow")
    if py[2]==my[2]:
        print("byk")
    elif py[2]==my[0] or py[2]==my[1]:
        print("cow")
    if my==py:
        print("Verno")
        answer=input("Do u want to play again(yes\ no)? ")
        if answer=="no":
            print("Bye")
            break
        if answer=="yes":
            print("OK")
            print("Let's play!")
            while True:
                a=random.randint(1,9)
                b=random.randint(1,9)
                c=random.randint(1,9)
                
                if a!=b!=c:
                    break
            py=(str(a)+str(b)+str(c))
