import random
print("Let's play")
while True: #while-infinity cycle
    print("Enter your choice (stone\scissors\paper): ")
    your_choise=input()
    num=random.randint(1,3) # randint это случайное рандомное число
    if num==1:
        print("I've choosen stone")
        python="stone"
    if num==2:
        print("I've choosen scissors")
        python="scissors"
    if num==3:
        print("I've choosen paper")
        python="paper"
    if your_choise==python:
        print('Draw')
    elif your_choise=="stone" and python=='scissors':
        print("You win")
    elif your_choise=="stone" and python=='paper':
        print("I win")
    elif your_choise=="paper" and python=='scissors':
        print("I win")
    elif your_choise=="paper" and python=='stone':
        print("You win")
    elif your_choise=="scissors" and python=='stone':
        print("I win")
    elif your_choise=="scissors" and python=='paper':
        print("You win")
    else:
        print("Э,ИГРАЙ ЧЕСТНО!!!")
    answer=input("Play again? (yes/no)")
    if answer=="no":
        print("Bye")
        break #breaks the programm
    
