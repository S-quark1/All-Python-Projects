import tkinter
import webbrowser

def Click():
    print("It's coool")
    quark.config(text="Yahoooooooo!")
def Click2():
    print("It's not coool")
    quark.config(text=":(")
def Click3():
    url=enter.get()
    webbrowser.open("https://www."+url)
window=tkinter.Tk() #create a window-переменная
window.geometry("450x400")
window.title("My first app!")
window.config(bg="#DB82F4") #bg-background, fg-forground, font-шрифт

quark=tkinter.Label(text="Do you wanna enter your site's url?", font="Calibri 20",bg="#DB82F4",fg='black')#text-это НЕ переменная
quark.pack()

enter=tkinter.Entry()
enter.pack()

btn=tkinter.Button(text="Yes", command=Click, width=5, heigh=1)
btn.pack()

btn2=tkinter.Button(text="No",command=Click2)
btn2.pack()

btn3=tkinter.Button(text="Go to browser", command=Click3)
btn3.pack()




