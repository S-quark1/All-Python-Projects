import requests
import tkinter
import random

link="https://opentdb.com/api.php?amount=10&category=17&difficulty=easy&type=multiple"
dataa=requests.get(link)
data=dataa.json()

i = 0
correct = ""

def Click():
    global i
    global correct
    
    question.config(text=data["results"][i]["question"])
    
    correct=data["results"][i]["correct_answer"]
    incorrect=data["results"][i]["incorrect_answers"]
    incorrect.append(correct)
    random.shuffle(incorrect)
    
    btn.config(text="Next")
    A.config(text="A) "+incorrect[0])
    B.config(text="B) "+incorrect[1])
    C.config(text="C) "+incorrect[2])
    D.config(text="D) "+incorrect[3])

    i = i + 1
    
def Click2():
    global correct
    Answer=answer.get()
    if Answer==correct:
        Correct.config(text="Correct!")
        #counter=counter+1
    else:
        Correct.config(text="Incorrect!")
        Correct2.config(text="There is correct answer: "+correct)
    print("Хоть что-то получается")

window=tkinter.Tk()
window.geometry("450x400")
window.title("The game")
window.config(bg="#36CEC6")

btn=tkinter.Button(text="Start", command=Click, width=5, heigh=1)
btn.pack()

question=tkinter.Label(font="Calibri 15",bg="#36CEC6",fg='black')
question.pack()

fr1=tkinter.Frame()

fr1.pack()

answer=tkinter.Entry(fr1)
answer.grid(row=1,column=1)

btn2=tkinter.Button(fr1, text="Ok", command=Click2, width=5, heigh=1)
btn2.grid(row=1,column=2)

A=tkinter.Label(font="Calibri 15",bg="#36CEC6",fg='black')
A.pack()

B=tkinter.Label(font="Calibri 15",bg="#36CEC6",fg='black')
B.pack()

C=tkinter.Label(font="Calibri 15",bg="#36CEC6",fg='black')
C.pack()

D=tkinter.Label(font="Calibri 15",bg="#36CEC6",fg='black')
D.pack()

Correct=tkinter.Label(font="Calibri 15",bg="#36CEC6",fg='black')
Correct.pack()

Correct2=tkinter.Label(font="Calibri 15",bg="#36CEC6",fg='black')
Correct2.pack()
