import random
print("Давай поиграем!")
python=random.randint(0,100)
print("Я загадал число от 0 до 100, отгадай")
while True:
    num=int(input())
    if python>num:
        print("НЕТ,БОООЛЬШЕЕЕ")
    if python<num:
        print("НЕТ,меньше")
    if python==num:
        print("МОЛОДЕЦ!")
        answer=input("Хочешь сыграть еще раз? (да/нет)")
        if answer=="нет":
            print("Пока")
            break
        if answer=="да":
            print("OK")
            python=random.randint(0,100)
            print("Я загадал число от 0 до 100, отгадай")
