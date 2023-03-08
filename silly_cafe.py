menu=["burger","cola","toast","water","juice",'pizza',"lemonad"]
print("Hello")
print("if you are done print 'Ok,it's enough'")
while True:
    print("What would you like?")
    client=input()
    if client=="burger":
        print("Sorry,our burger run away")
    elif client=="cola":
        print("Ok")
    elif client=="toast":
        print("Sorry,our toast was eatten by us")
    elif client=="pizza":
        print("Ok")
    elif client=="water":
        print("Sorry, we are in Sahara")
    elif client=="juice":
        print("Sorry,our juice run away")
    elif client=="lemonad":
        print("Ok")
    elif client=="Ok,it's enough":
        print("Wait for 30 minut")
        break
    else:
        print("ERROR ERROR ERROR ERROR")
        print("Oficiant slomalsya")
        print("Perezagruzka")
        print("Please, try again")
        
