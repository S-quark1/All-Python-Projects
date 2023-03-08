import tkinter

def Click11():
    btn11.config(bg="black")
def Click12():
    btn12.config(bg="black")
def Click13():
    btn13.config(bg="black")
def Click14():
    btn14.config(bg="black")
def Click15():
    btn15.config(bg="black")
def Click16():
    btn16.config(bg="black")
def Click17():
    btn17.config(bg="black")
def Click18():
    btn18.config(bg="black")
def Click21():
    btn21.config(bg="black")
def Click22():
    btn22.config(bg="black")
def Click23():
    btn23.config(bg="black")
def Click24():
    btn24.config(bg="black")
def Click25():
    btn25.config(bg="black")
def Click26():
    btn26.config(bg="black")
def Click27():
    btn27.config(bg="black")
def Click28():
    btn28.config(bg="black")
##def Click9():
##    btn9.config(text='X')

window=tkinter.Tk()
window.geometry("450x400")
window.title("The Military War")
window.config(bg="#36CEC6")

btn=tkinter.Button(text="Start", width=5, heigh=1)
btn.pack()

the_end=tkinter.Label(text="", font="Calibri 15", bg="#36CEC6", fg='black')
the_end.pack()

fr1=tkinter.Frame()

fr1.pack()

btn11=tkinter.Button(fr1, command=Click11, width=5, heigh=1)
btn11.grid(row=1,column=1)

btn12=tkinter.Button(fr1, command=Click12, width=5, heigh=1)
btn12.grid(row=1,column=2)

btn13=tkinter.Button(fr1, command=Click13, width=5, heigh=1)
btn13.grid(row=1,column=3)

btn14=tkinter.Button(fr1, command=Click14, width=5, heigh=1)
btn14.grid(row=1,column=4)

btn15=tkinter.Button(fr1, command=Click15, width=5, heigh=1)
btn15.grid(row=1,column=5)

btn16=tkinter.Button(fr1, command=Click16, width=5, heigh=1)
btn16.grid(row=1,column=6)

btn17=tkinter.Button(fr1, command=Click17, width=5, heigh=1)
btn17.grid(row=1,column=7)

btn18=tkinter.Button(fr1, command=Click18, width=5, heigh=1)
btn18.grid(row=1,column=8)

btn21=tkinter.Button(fr1, command=Click21, width=5, heigh=1)
btn21.grid(row=2,column=1)

btn22=tkinter.Button(fr1, command=Click22, width=5, heigh=1)
btn22.grid(row=2,column=2)

btn23=tkinter.Button(fr1, command=Click23, width=5, heigh=1)
btn23.grid(row=2,column=3)

btn24=tkinter.Button(fr1, command=Click24, width=5, heigh=1)
btn24.grid(row=2,column=4)

btn25=tkinter.Button(fr1, command=Click25, width=5, heigh=1)
btn25.grid(row=2,column=5)

btn26=tkinter.Button(fr1, command=Click26, width=5, heigh=1)
btn26.grid(row=2,column=6)

btn27=tkinter.Button(fr1, command=Click27, width=5, heigh=1)
btn27.grid(row=2,column=7)

btn28=tkinter.Button(fr1, command=Click28, width=5, heigh=1)
btn28.grid(row=2,column=8)


