import telebot
from telebot import types
import requests
import random

token="887177629:AAHB_yen-TKSq4fOMbpmneVdKj81kOExTVY"
bot=telebot.TeleBot(token)

link="https://opentdb.com/api.php?amount=3&category=32&difficulty=easy&type=multiple"
results=[]
qNum=0

@bot.message_handler(commands=["start"])
def Start(msg):
    name=msg.from_user.first_name
    bot.send_message(msg.chat.id, "Здравствуйте, "+name+"!")
    GetTrivia(msg)

def GetTrivia(msg):
    global qNum
    global results
    dataa=requests.get(link)
    data=dataa.json()
    results=data["results"]
    qNum=0
    Ask(msg)

def Ask(msg):
    global results
    global qNum
    question=results[qNum]["question"]
    incorrect=results[qNum]["incorrect_answers"]
    correct=results[qNum]["correct_answer"]
    print(correct)
    incorrect.append(correct)
    random.shuffle(incorrect)

    keyboard=types.ReplyKeyboardMarkup()
    btn1=types.KeyboardButton(incorrect[0]) #не пиши "A) "+, он на тебя наедет
    btn2=types.KeyboardButton(incorrect[1])
    btn3=types.KeyboardButton(incorrect[2])
    btn4=types.KeyboardButton(incorrect[3])

    keyboard.add(btn1)
    keyboard.add(btn2)
    keyboard.add(btn3)
    keyboard.add(btn4)
    answer=bot.send_message(msg.chat.id, question, reply_markup=keyboard)
    bot.register_next_step_handler(answer, Answer)
    
def Answer(msg):
    global qNum
    global results
    if msg.text==results[qNum]["correct_answer"]:
        bot.send_message(msg.chat.id, "МОЛОДЕЦ!")
    else:
        bot.send_message(msg.chat.id, "НЕ МОЛОДЕЦ!")
    qNum=qNum+1
    if qNum==3:
        keyboard=types.ReplyKeyboardRemove(selective=False)
        bot.send_message(msg.chat.id, """Конец игры!
Если хотите еще раз сыграть, напишите /start """, reply_markup=keyboard)
    else:
        Ask(msg)


bot.polling()
