import tkinter
import random
a=[]
py=[0,1,2,3,4,5,6,7,8]
def Check():
    c1=btn1["text"]
    c2=btn2["text"]
    c3=btn3["text"]
    c4=btn4["text"]
    c5=btn5["text"]
    c6=btn6["text"]
    c7=btn7["text"]
    c8=btn8["text"]
    c9=btn9["text"]
    if c1==c2 and c1==c3:
        if c1=="X":
            the_end.config(text="""YOU won the competition!
Would u like to play again?""")
            btn.config(text="YES!", bg="white")
        if c1=="O":
            the_end.config(text="""I won the competition!
Would u like to play again?""")
            btn.config(text="YES!", bg="white")
    if c4==c5 and c4==c6:
        if c4=="X":
            the_end.config(text="""YOU won the competition!
Would u like to play again?""")
            btn.config(text="YES!", bg="white")
        if c4=="O":
            the_end.config(text="""I won the competition!
Would u like to play again?""")
            btn.config(text="YES!", bg="white")
    if c7==c8 and c7==c9:
        if c7=="X":
            the_end.config(text="""YOU won the competition!
Would u like to play again?""")
            btn.config(text="YES!", bg="white")
        if c7=="O":
            the_end.config(text="""I won the competition!
Would u like to play again?""")
            btn.config(text="YES!", bg="white")
    if c1==c4 and c1==c7:
        if c1=="X":
            the_end.config(text="""YOU won the competition!
Would u like to play again?""")
            btn.config(text="YES!", bg="white")
        if c1=="O":
            the_end.config(text="""I won the competition!
Would u like to play again?""")
            btn.config(text="YES!", bg="white")
    if c2==c5 and c2==c8:
        if c2=="X":
            the_end.config(text="""YOU won the competition!
Would u like to play again?""")
            btn.config(text="YES!", bg="white")
        if c2=="O":
            the_end.config(text="""I won the competition!
Would u like to play again?""")
            btn.config(text="YES!", bg="white")
    if c3==c6 and c3==c9:
        if c3=="X":
            the_end.config(text="""YOU won the competition!
Would u like to play again?""")
            btn.config(text="YES!", bg="white")
        if c3=="O":
            the_end.config(text="""I won the competition!
Would u like to play again?""")
            btn.config(text="YES!", bg="white")
    if c1==c5 and c1==c9:
        if c1=="X":
            the_end.config(text="""YOU won the competition!
Would u like to play again?""")
            btn.config(text="YES!", bg="white")
        if c1=="O":
            the_end.config(text="""I won the competition!
Would u like to play again?""")
            btn.config(text="YES!", bg="white")
    if c3==c5 and c3==c7:
        if c3=="X":
            the_end.config(text="""YOU won the competition!
Would u like to play again?""")
            btn.config(text="YES!", bg="white")
        if c3=="O":
            the_end.config(text="""I won the competition!
Would u like to play again?""")
            btn.config(text="YES!", bg="white")
def Dostalo():
    a.sort()
    Py()
    Check()
def Py():
    while True:
        if a==[1,2,3,4,5,6,7,8,9]:
            the_end.config(text="Game over")
            break
        py=random.randint(0,8)
        if py==0 and 1 not in a:
            btn1.config(text='O')
            a.append(1)
            a.sort()
            break
        if py==1 and 2 not in a:
            btn2.config(text='O')
            a.append(2)
            a.sort()
            break
        if py==2 and 3 not in a:
            btn3.config(text='O')
            a.append(3)
            a.sort()
            break
        if py==3 and 4 not in a:
            btn4.config(text='O')
            a.append(4)
            a.sort()
            break
        if py==4 and 5 not in a:
            btn5.config(text='O')
            a.append(5)
            a.sort()
            break
        if py==5 and 6 not in a:
            btn6.config(text='O')
            a.append(6)
            a.sort()
            break
        if py==6 and 7 not in a:
            btn7.config(text='O')
            a.append(7)
            a.sort()
            break
        if py==7 and 8 not in a:
            btn8.config(text='O')
            a.append(8)
            a.sort()
            break
        if py==8 and 9 not in a:
            btn9.config(text='O')
            a.append(9)
            a.sort()
            break
def Click1():
    a.append(1)
    btn1.config(text='X')
    Dostalo()
def Click2():
    a.append(2)
    btn2.config(text='X')
    Dostalo()
def Click3():
    a.append(3)
    btn3.config(text='X')
    Dostalo()
def Click4():
    a.append(4)
    btn4.config(text='X')
    Dostalo()
def Click5():
    a.append(5)
    btn5.config(text='X')
    Dostalo()
def Click6():
    a.append(6)
    btn6.config(text='X')
    Dostalo()
def Click7():
    a.append(7)
    btn7.config(text='X')
    Dostalo()
def Click8():
    a.append(8)
    btn8.config(text='X')
    Dostalo()
def Click9():
    a.append(9)
    btn9.config(text='X')
    Dostalo()
def Next():
    a=[]
    print(a)
    the_end.config(text="")
    btn.config(text="", bg="#36CEC6")
    btn1.config(text='')
    btn2.config(text='')
    btn3.config(text='')
    btn4.config(text='')
    btn5.config(text='')
    btn6.config(text='')
    btn7.config(text='')
    btn8.config(text='')
    btn9.config(text='')
window=tkinter.Tk()
window.geometry("450x400")
window.title("X & O")
window.config(bg="#36CEC6")

the_end=tkinter.Label(text="", font="Calibri 15", bg="#36CEC6", fg='black')
the_end.pack()

btn=tkinter.Button(text="", command=Next, width=5, heigh=1, bg="#36CEC6")
btn.pack()

fr1=tkinter.Frame()

fr1.pack()

btn1=tkinter.Button(fr1, command=Click1, width=5, heigh=1)
btn1.grid(row=1,column=1)

btn2=tkinter.Button(fr1, command=Click2, width=5, heigh=1)
btn2.grid(row=1,column=2)

btn3=tkinter.Button(fr1, command=Click3, width=5, heigh=1)
btn3.grid(row=1,column=3)

btn4=tkinter.Button(fr1, command=Click4, width=5, heigh=1)
btn4.grid(row=2,column=1)

btn5=tkinter.Button(fr1, command=Click5, width=5, heigh=1)
btn5.grid(row=2,column=2)

btn6=tkinter.Button(fr1, command=Click6, width=5, heigh=1)
btn6.grid(row=2,column=3)

btn7=tkinter.Button(fr1, command=Click7, width=5, heigh=1)
btn7.grid(row=3,column=1)

btn8=tkinter.Button(fr1, command=Click8, width=5, heigh=1)
btn8.grid(row=3,column=2)

btn9=tkinter.Button(fr1, command=Click9, width=5, heigh=1)
btn9.grid(row=3,column=3)

