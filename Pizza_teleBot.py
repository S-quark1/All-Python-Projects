import telebot
from telebot import types

token="887177629:AAHB_yen-TKSq4fOMbpmneVdKj81kOExTVY"
bot=telebot.TeleBot(token)

prices={"Маргарита-1000тг":1000, "Пеперони-1200тг":1200, "Оливковая-1100тг":1100, "Гавайская-1000тг":1000, "Чикен BBQ-1300тг":1300}

file=open("Orders.txt","w")
orders=[]
order=["Заказы: "]

@bot.message_handler(commands=["start"])
def Start(msg):
    name=msg.from_user.first_name
    bot.send_message(msg.chat.id, "Здравствуйте, "+name+"!")
    bot.send_message(msg.chat.id, "Вас приветсвует пиццерия Доширак!")
    Pizza(msg)

def Pizza(msg):
    #custom keyboard
    keyboard=types.ReplyKeyboardMarkup()
    btn1=types.KeyboardButton("Маргарита-1000тг")
    btn2=types.KeyboardButton("Пеперони-1200тг")
    btn3=types.KeyboardButton("Оливковая-1100тг")
    btn4=types.KeyboardButton("Гавайская-1000тг")
    btn5=types.KeyboardButton("Чикен BBQ-1300тг")

    keyboard.add(btn1)
    keyboard.add(btn2)
    keyboard.add(btn3)
    keyboard.add(btn4)
    keyboard.add(btn5)

    answer=bot.send_message(msg.chat.id, "Какую пиццу желаете?", reply_markup=keyboard)
    bot.register_next_step_handler(answer, Dough)

def Dough(msg): # dough-тесто
    global order
    order.append(msg.text)
    
    keyboard=types.ReplyKeyboardMarkup()
    btn1=types.KeyboardButton("Тонкое") # Он на меня орать не будет, т.к. эти переменные в функции, то есть локальные
    btn2=types.KeyboardButton("Пышное")

    keyboard.add(btn1)
    keyboard.add(btn2)

    answer=bot.send_message(msg.chat.id, "Какое тесто желаете?", reply_markup=keyboard)
    bot.register_next_step_handler(answer, Sauce)

def Sauce(msg):
    global order
    order.append(msg.text)
    
    keyboard=types.ReplyKeyboardMarkup()
    btn1=types.KeyboardButton("Сырный")
    btn2=types.KeyboardButton("Чесночный")
    btn3=types.KeyboardButton("Острый")
    btn4=types.KeyboardButton("Сладкий")

    keyboard.add(btn1)
    keyboard.add(btn2)
    keyboard.add(btn3)
    keyboard.add(btn4)

    answer=bot.send_message(msg.chat.id, "Какой соус желаете?", reply_markup=keyboard)
    bot.register_next_step_handler(answer, Check)
    
def Check(msg):
    global orders
    global order
    order.append(msg.text)
    orders.append(order)
    order=[] #незнает это глобальная или локальная переменная, по этому пишем global
    keyboard=types.ReplyKeyboardMarkup()
    btn1=types.KeyboardButton("Да")
    btn2=types.KeyboardButton("Нет")

    keyboard.add(btn1)
    keyboard.add(btn2)

    answer=bot.send_message(msg.chat.id, "Что-нибуть еще желаете?", reply_markup=keyboard)
    bot.register_next_step_handler(answer, Result)

def Result(msg):
    global file
    global orders
    global prices
    if msg.text=="Да":
        Pizza(msg)
    elif msg.text=="Нет":
        keyboard=types.ReplyKeyboardRemove(selective=False)
        bot.send_message(msg.chat.id, "Спасибо за ваш заказ!", reply_markup=keyboard)
        bot.send_message(msg.chat.id, "Вы заказали:")
        price=0
        for o in orders:
            bot.send_message(msg.chat.id, o[1]+", "+o[2]+", "+o[3])
            price=price+prices[o[1]]
##            file.write("1)",o[0]+", "+o[1]+", "+o[2])
##        quark="1) "+orders[0]+", "+ orders[1]+", "+orders[2]
##        file.write(quark)
        print(orders)
        bot.send_message(msg.chat.id, "Общая сумма заказа: "+str(price)+'тг')
        answerPhone=bot.send_message(msg.chat.id, "Пoжалуйста напишите свой номер телефона")
        bot.register_next_step_handler(answerPhone, Result2)

def Result2(msg):
    global orders
    orders.insert(0,"Номер: "+msg.text)
    print(msg.text)
    bot.send_message(msg.chat.id, "Спасибо")
    answerAdress=bot.send_message(msg.chat.id, "Пoжалуйста напишите свой адрес")
    bot.register_next_step_handler(answerAdress, Result3)
    
def Result3(msg):
    global orders
    global file
    orders.insert(1,"Адрес: "+msg.text)
    print(msg.text)
    quark=str(orders)
    bot.send_message(msg.chat.id, "Спасибо")
    bot.send_message(msg.chat.id, "Оператор свяжется с вами через неделю")
    bot.send_message(msg.chat.id, ":)")
    file.write(quark)
    orders=[]
    file=open("Orders.txt","r")
@bot.message_handler(content_types=['text']) #image, audio вместо text можно поставить
def Phone(msg):
    pass
bot.polling()

