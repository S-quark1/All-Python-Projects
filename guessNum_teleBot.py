import telebot
import random

token="992524029:AAEfRoU11Gipy9_bspGQfGGLqHc-oRDpvV0"
bot=telebot.TeleBot(token)
python=0
@bot.message_handler(commands=["start"])
def Start(msg):
    global python
    name=msg.from_user.first_name
    bot.send_message(msg.chat.id, "Let's play, my dear "+name+"!")
    python=random.randint(0,100) #или же тупо вытащить его внаружу
    bot.send_message(msg.chat.id, "Guess the number from 0 to 100")
    python=random.randint(0,100) #или же тупо вытащить его внаружу
    
@bot.message_handler(content_types=['text'])
def Text(msg):
    global python
    try:
        num=int(msg.text) #то что ты написал переведи в число
        if num==python:
            bot.send_message(msg.chat.id, "Молодецц")
        elif num < python:
            bot.send_message(msg.chat.id, "Bigger!")
        elif num > python:
            bot.send_message(msg.chat.id, "Less!")     
        else:
            bot.send_message(msg.chat.id, "GIANT MUSHROOM EATED A MOUSE")
    except:
        bot.send_message(msg.chat.id, ":(")
    
bot.polling()
