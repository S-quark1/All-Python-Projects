import tkinter
import requests

def Click():
    city=enCity.get()
    link="http://api.openweathermap.org/data/2.5/weather?&APPID=5e2620533f8da0deab17a137c456dbd0&units=metric&q="+city
    data=requests.get(link)
    d=data.json()
    b=0
    while question!="1111":
        if d["cod"]==200:
            quark.config(text=str(d["main"]["temp"])+"^C")
            quark2.config(text=str(d["wind"]["speed"])+"m/s")
            quark3.config(text=str(d["weather"][0]["description"]), font="Calibri 17")
            thanks.config(text="See you soon!")
            question.config(text="b"+"1")
        else:
            quark.config(text="-")
            quark2.config(text="-")
            quark3.config(text="This city is in parallel world", font="Calibri 20")
            thanks.config(text="")
##    quark.config(text=":(")
    
window=tkinter.Tk()
window.geometry("450x400")
window.title("Weather :)")
window.config(bg="#36CEC6")

question=tkinter.Label(text="Enter your city's name: ", font="Calibri 15",bg="#36CEC6",fg='black')
question.pack()

fr1=tkinter.Frame()
fr2=tkinter.Frame()
fr3=tkinter.Frame()

fr1.pack()
fr2.pack()
fr3.pack()

enCity=tkinter.Entry(fr1)
enCity.grid(row=1,column=1)

btn=tkinter.Button(fr1, text="Ok", command=Click, width=5, heigh=1)
btn.grid(row=1,column=2)

answer=tkinter.Label(fr2, text="Temp:", font="Calibri 15",bg="#36CEC6",fg='black')
answer.grid(row=1,column=1)

quark=tkinter.Label(fr2, font="Calibri 15",bg="#36CEC6",fg='black')
quark.grid(row=1,column=2)

answer2=tkinter.Label(fr3, text="Wind:", font="Calibri 15",bg="#36CEC6",fg='black')
answer2.grid(row=1,column=1)

quark2=tkinter.Label(fr3, font="Calibri 15",bg="#36CEC6",fg='black')
quark2.grid(row=1,column=2)

quark3=tkinter.Label(font="Calibri 17",bg="#36CEC6",fg='black')
quark3.pack()

thanks=tkinter.Label(font="Calibri 20",bg="#36CEC6",fg='black')
thanks.pack()
