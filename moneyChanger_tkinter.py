import tkinter
import requests
def Click():
    money=enMoney.get()
    link="https://openexchangerates.org/api/latest.json?app_id=60da2bd9b3064714b2c5f2e8b00fbd40"
    data=requests.get(link)
    d=data.json()
    money=round(int(money)/d["rates"]["KZT"], 2)
    answer.config(text=money)
    money2=round(money*d["rates"]["EUR"], 2)
    answer2.config(text=money2)
    money3=round(money*d["rates"]["RUB"], 2)
    answer3.config(text=money3)
window=tkinter.Tk()
window.geometry("450x400")
window.title("Exchange changer")
window.config(bg="green")

fr1=tkinter.Frame()
fr2=tkinter.Frame()
fr3=tkinter.Frame()
fr4=tkinter.Frame()

fr1.pack()
fr2.pack()
fr3.pack()
fr4.pack()

kz=tkinter.Label(fr1, text="KZT: ", font="Calibri 15",bg="green",fg='black')
kz.grid(row=1,column=1)

enMoney=tkinter.Entry(fr1)
enMoney.grid(row=1,column=2)

btn=tkinter.Button(fr1, text="Ok", command=Click, width=5, heigh=1)
btn.grid(row=1,column=3)

USD=tkinter.Label(fr2, text="USD:", font="Calibri 15",bg="green",fg='black')
USD.grid(row=1,column=1)

answer=tkinter.Label(fr2, font="Calibri 15",bg="green",fg='black')
answer.grid(row=1,column=2)

EUR=tkinter.Label(fr3, text="EUR:", font="Calibri 15",bg="green",fg='black')
EUR.grid(row=1,column=1)

answer2=tkinter.Label(fr3, font="Calibri 15",bg="green",fg='black')
answer2.grid(row=1,column=2)

RUB=tkinter.Label(fr4, text="RUB:", font="Calibri 15",bg="green",fg='black')
RUB.grid(row=1,column=1)

answer3=tkinter.Label(fr4, font="Calibri 15",bg="green",fg='black')
answer3.grid(row=1,column=2)
