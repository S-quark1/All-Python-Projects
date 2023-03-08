import telebot
token="992524029:AAEfRoU11Gipy9_bspGQfGGLqHc-oRDpvV0"
bot=telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def Start(msg): # после @ мы обязаны писать функции
    name=msg.from_user.first_name
    bot.reply_to(msg, "Hello "+name+"!") #именно msg-message, потому что мы получаем сообщение #тут мы не можем использовать ,
    #print(msg.from_user.first_name)# или просто name #в библиотеке telebot все достается через точку
    
    bot.send_message(msg.chat.id, "Hello "+name+"!")
    try:
        print(msg)
    except:
        print(":(")
@bot.message_handler(content_types=['text'])
def Text(msg):
    if msg.text=="Hi":
        bot.send_message(msg.chat.id, "Hi!") #msg.chat.id- напиши в определенный чат то-то то-то
        bot.send_message(msg.chat.id, "How 're u?")
    elif msg.text=="Good":
        bot.send_message(msg.chat.id, "Cool")
        bot.send_message(msg.chat.id, "10000 bacteria killed per minute")
        bot.send_message(msg.chat.id, "How 're u?")
    elif msg.text=="Bad":
        bot.send_message(msg.chat.id, "MoleCOOL")
        bot.send_message(msg.chat.id, "Do you wanna joke?")
    elif msg.text=="Yes":
        bot.send_message(msg.chat.id, "I wont tell you :)")
        bot.send_message(msg.chat.id, "Bye")
    elif msg.text=="No":
        bot.send_message(msg.chat.id, ":(")
    elif msg.text=="Go to hell":
        bot.send_message(msg.chat.id, "I'm also love u")
    else:
        bot.send_message(msg.chat.id, "GIANT MUSHROOM EATED A MOUSE")
#pass-пропустить прошлую строчку
##        try: #попытаться
##            gfjdsfsf
##        except: #если не получиться, то сделай это
##            dhkjwhrvh
bot.polling() #like while True, but in telebot
