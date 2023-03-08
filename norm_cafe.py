menu={"food":{"burger":1000,"toast":200,'pizza':500},
      "drink":{"water":100,"juice":200,"cola":170,"lemonad":200},
      "desserts":{"tiramisu":700,"cake":800}}
print("Hello")
print("There is our menu:")
for yedainapitok in menu.keys():
    print(yedainapitok,"-",menu[yedainapitok])
while True:
    print("What would you like?(food\drink\desserts)")
    answer=input()
    if answer=="food":
        yeda=input("Please,enter food name:")
    if answer=="drink":
        napitok=input("Please,enter drink name:")
    if answer=="desserts":
        dessert=input("Please,enter dessert name:")
        if yeda in menu['food'] and napitok in menu['drink'] and dessert in menu['desserts']:
            print("Ok")
        else:
            print("ERROR ERROR ERROR ERROR")
            print("Oficiant slomalsya")
        print("Если все,то нaпишите stop")
        if answer==stop:
            print("Ok")
            break
    #если у ключа только одно значение то пишем к примеру:
        # if dessert==menu['desserts']:
        #....
