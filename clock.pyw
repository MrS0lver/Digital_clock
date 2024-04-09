from tkinter import *
from tkinter import ttk,messagebox
import datetime

win = Tk()
win.title("Clock")
win.minsize(width=420,height=300)
win.maxsize(width=420,height=300)
win.config(bg="lightgreen")

def display():
    time = datetime.datetime.now()
    hr = time.strftime("%I:")
    mn = time.strftime("%M:")
    sec = time.strftime("%S:")
    pm = time.strftime("%p")
    date = time.strftime("%d")
    day = time.strftime("%aday")
    mon = time.strftime("%m")
    yr = time.strftime("20%y")

    label.config(text=hr)
    label1.config(text=mn)
    label2.config(text=sec)
    label3.config(text=pm)
    labelo.config(text=date)
    labelp.config(text=day)
    labelq.config(text=mon)
    labelj.config(text=yr)
    label.after(200,display)


def sets():
    top = Toplevel()
    top.title("Settings")
    top.minsize(width=394,height=300)
    top.maxsize(width=300,height=300)
    top.config(bg="lightgrey")

    def textcolor():
        if comobox.get() == "Green":
            label.config(fg="green")
            label1.config(fg="green")
            label2.config(fg="green")
            label3.config(fg="green")
            labelo.config(fg="green")
            labelo.config(fg="green")
            labelp.config(fg="green")
            labelq.config(fg="green")
            labelj.config(fg="green")
            # labelins.config(fg="green")
            # labelins1.config(fg="green")
        elif comobox.get() == "Yellow":
            label.config(fg="yellow")
            label1.config(fg="yellow")
            label2.config(fg="yellow")
            label3.config(fg="yellow")
            labelo.config(fg="yellow")
            labelo.config(fg="yellow")
            labelp.config(fg="yellow")
            labelq.config(fg="yellow")
            labelj.config(fg="yellow")
            # labelins.config(fg="yellow")
            # labelins1.config(fg="yellow")
        elif comobox.get() == "Cyan":
            label.config(fg="Cyan")
            label1.config(fg="Cyan")
            label2.config(fg="Cyan")
            label3.config(fg="Cyan")
            labelo.config(fg="Cyan")
            labelo.config(fg="Cyan")
            labelp.config(fg="Cyan")
            labelq.config(fg="Cyan")
            labelj.config(fg="Cyan")
            # labelins.config(fg="Cyan")
            # labelins1.config(fg="Cyan")
        elif comobox.get() == "Defoult":
            label.config(fg="Black")
            label1.config(fg="Black")
            label2.config(fg="Black")
            label3.config(fg="Black")
            labelo.config(fg="Black")
            labelo.config(fg="Black")
            
            labelp.config(fg="Black")
            labelq.config(fg="Black")
            labelj.config(fg="Black")
            # labelins.config(fg="Black")
            # labelins1.config(fg="Black")
        elif comobox.get() == "Red":
            label.config(fg="Red")
            label1.config(fg="Red")
            label2.config(fg="Red")
            label3.config(fg="Red")
            labelo.config(fg="Red")
            labelo.config(fg="Red")
            labelp.config(fg="Red")
            labelq.config(fg="Red")
            labelj.config(fg="Red")
            # labelins.config(fg="Red")
            # labelins1.config(fg="Red")
        elif comobox.get() == "Pink":
            label.config(fg="Pink")
            label1.config(fg="Pink")
            label2.config(fg="Pink")
            label3.config(fg="Pink")
            labelo.config(fg="Pink")
            labelo.config(fg="Pink")
            labelp.config(fg="Pink")
            labelq.config(fg="Pink")
            labelj.config(fg="Pink")
            # labelins.config(fg="Pink")
            # labelins1.config(fg="Pink")
        elif comobox.get() == "Cyan":
            label.config(fg="cyan")
            label1.config(fg="cyan")
            label2.config(fg="cyan")
            label3.config(fg="cyan")
            labelo.config(fg="cyan")
            labelo.config(fg="cyan")
            labelp.config(fg="cyan")
            labelq.config(fg="cyan")
            labelj.config(fg="cyan")
            # labelins.config(fg="cyan")
            # labelins1.config(fg="cyan")
        elif comobox.get() == "Black":
            label.config(fg="Black")
            label1.config(fg="Black")
            label2.config(fg="Black")
            label3.config(fg="Black")
            labelo.config(fg="Black")
            labelo.config(fg="Black")
            labelp.config(fg="Black")
            labelq.config(fg="Black")
            labelj.config(fg="Black")
            # labelins.config(fg="Black")
            # labelins1.config(fg="Black")
        elif comobox.get() == "Orange":
            label.config(fg="Orange")
            label1.config(fg="Orange")
            label2.config(fg="Orange")
            label3.config(fg="Orange")
            labelo.config(fg="Orange")
            labelo.config(fg="Orange")
            labelp.config(fg="Orange")
            labelq.config(fg="Orange")
            labelj.config(fg="Orange")
            # labelins.config(fg="Orange")
            # labelins1.config(fg="Orange")
        else:
            messagebox.showinfo("Warning","Something went wrong")

    again = Button(top, text="Change Text Color", command=textcolor)
    again.place(y=66)

    labelom = Label(top,text="Change Background Color",font=('Times',10))
    labelom.pack()



    comobox = ttk.Combobox(top)
    comobox.place(x=1,y=90,width=108)
    comobox['values']=('Defoult',
                       'Green',
                       'Red',
                       'Yellow',
                       'Pink',
                       'Black',
                       'Grey',
                       'Cyan',
                       'Orange',
                       'lightgreen',
                       'lightgrey')
    comobox['state']='readonly'
    comobox.current(0)

    again1 = Button(top,text="Change Text Style",cursor="plus",relief=RAISED)
    again1.place(y=111,width=108)

    comobox1 = ttk.Combobox(top)
    comobox1.place(x=1,y=138,width=108)

    comobox1['values']=('Default',
                        'Times New Roman',
                        'Tmes',
                        'Bold',
                        'Italic',
                        'Caveat',
                        '',
                        '',
                        '',
                        '',
                        '',
                        '',
                        '',
                        '',
                        '')
    comobox1.current(0)

    def timecolor():
        if comobox2.get() == "Defoult":
            label.config(bg="white")
            label1.config(bg="white")
            label2.config(bg="white")
            label3.config(bg="white")
        elif comobox2.get() == "Green":
            label.config(bg="Green")
            label1.config(bg="Green")
            label2.config(bg="Green")
            label3.config(bg="Green")
        elif comobox2.get() == "Red":
            label.config(bg="red")
            label1.config(bg="red")
            label2.config(bg="red")
            label3.config(bg="red")
        elif comobox2.get() == "Yellow":
            label.config(bg="yellow")
            label1.config(bg="yellow")
            label2.config(bg="yellow")
            label3.config(bg="yellow")
        elif comobox2.get() == "Pink":
            label.config(bg="Pink")
            label1.config(bg="Pink")
            label2.config(bg="Pink")
            label3.config(bg="Pink")
        elif comobox2.get() == "Black":
            label.config(bg="Black")
            label1.config(bg="Black")
            label2.config(bg="Black")
            label3.config(bg="Black")
        elif comobox2.get() == "Grey":
            label.config(bg="Grey")
            label1.config(bg="Grey")
            label2.config(bg="Grey")
            label3.config(bg="Grey")
        elif comobox2.get() == "Cyan":
            label.config(bg="cyan")
            label1.config(bg="cyan")
            label2.config(bg="cyan")
            label3.config(bg="cyan")
        elif comobox2.get() == "Orange":
            label.config(bg="orange")
            label1.config(bg="orange")
            label2.config(bg="orange")
            label3.config(bg="orange")
        elif comobox2.get() == "lightgreen":
            label.config(bg="lightgreen")
            label1.config(bg="lightgreen")
            label2.config(bg="lightgreen")
            label3.config(bg="lightgreen")
        else:
            messagebox.showwarning("Warning","Something went wrong!!!")




    timecolor = Button(top,text="Change Time color",cursor="plus",relief=RAISED,command=timecolor)
    timecolor.place(x=1,y=160,width=108)

    comobox2 = ttk.Combobox(top)
    comobox2.place(x=1,y=187,width=108)
    comobox2['values']=('Defoult',
                       'Green',
                       'Red',
                       'Yellow',
                       'Pink',
                       'Black',
                       'Grey',
                       'Cyan',
                       'Orange',
                       'lightgreen',
                       'lightgrey')
    comobox2.current(0)
    comobox2['state']='readonly'

    def green():
        win.config(bg="green")
        labelo.config(bg="green")
        labelp.config(bg="green")
        labelq.config(bg="green")
        labelj.config(bg="green")
        displaying.config(bg="green")

    def yellow():
        win.config(bg="yellow")
        labelo.config(bg="yellow")
        labelp.config(bg="yellow")
        labelq.config(bg="yellow")
        labelj.config(bg="yellow")
        displaying.config(bg="yellow")

    def Cyan():
        win.config(bg="cyan")
        labelo.config(bg="cyan")
        labelp.config(bg="cyan")
        labelq.config(bg="cyan")
        labelj.config(bg="cyan")
        displaying.config(bg="cyan")

    def Blue():
        win.config(bg="blue")
        labelo.config(bg="blue")
        labelp.config(bg="blue")
        labelq.config(bg="blue")
        labelj.config(bg="blue")
        displaying.config(bg="blue")

    def Red():
        win.config(bg="red")
        labelo.config(bg="red")
        labelp.config(bg="red")
        labelq.config(bg="red")
        labelj.config(bg="red")
        displaying.config(bg="red")

    def Pink():
        win.config(bg="pink")
        labelo.config(bg="pink")
        labelp.config(bg="pink")
        labelq.config(bg="pink")
        labelj.config(bg="pink")
        displaying.config(bg="pink")

    def Grey():
        win.config(bg="grey")
        labelo.config(bg="grey")
        labelp.config(bg="grey")
        labelq.config(bg="grey")
        labelj.config(bg="grey")
        displaying.config(bg="grey")

    def Orange():
        win.config(bg="orange")
        labelo.config(bg="orange")
        labelp.config(bg="orange")
        labelq.config(bg="orange")
        labelj.config(bg="orange")
        displaying.config(bg="orange")

    def deflo():
        win.config(bg="lightgreen")
        labelo.config(bg="lightgreen")
        labelp.config(bg="lightgreen")
        labelq.config(bg="lightgreen")
        labelj.config(bg="lightgreen")
        displaying.config(bg="lightgreen")

    button = Button(top,text="Green ",relief=RAISED,cursor="cross",command=green)
    button.place(y=30 , width=40)

    button1 = Button(top,text="Yellow ",relief=RAISED,cursor="cross",command=yellow)
    button1.place(x=40,y=30)

    button2 = Button(top, text="Cyan ", relief=RAISED, cursor="cross", command=Cyan)
    button2.place(x=89, y=30 , width=40)

    button3 = Button(top, text="Blue ", relief=RAISED, cursor="cross", command=Blue)
    button3.place(x=129, y=30 , width=40)

    button4 = Button(top, text="Red ", relief=RAISED, cursor="cross", command=Red)
    button4.place(x=169, y=30 , width=40)

    button5 = Button(top, text="Pink ", relief=RAISED, cursor="cross", command=Pink)
    button5.place(x=209, y=30 , width=40)

    button6 = Button(top, text="Grey ", relief=RAISED, cursor="cross", command=Grey)
    button6.place(x=249, y=30, width=40)

    button7 = Button(top, text="Orange ", relief=RAISED, cursor="cross", command=Orange)
    button7.place(x=289, y=30)

    button8 = Button(top, text="Default", relief=RAISED, cursor="cross", command=deflo)
    button8.place(x=343, y=30)


label = Label(win,text="00",font=('Elephant','30'))
label.place(x=10,y=1,width=100,height=90)

label1 = Label(win,text="00",font=('Elephant','30'))
label1.place(x=110,y=1,width=100,height=90)

label2 = Label(win,text="00",font=('Elephant','30'))
label2.place(x=210,y=1,width=100,height=90)

label3 = Label(win,text="00",font=('Elephant','27'))
label3.place(x=310,y=1,width=100,height=90)

##########################################################################

labelo = Label(win,text="00",font=('Impact','20'),bg="lightgreen")
labelo.place(x=10,y=80,width=100,height=90)

labelp = Label(win,text="00",font=('Mv Boli','21'),bg="lightgreen")
labelp.place(x=110,y=80,width=100,height=90)

labelq = Label(win,text="00",font=('Impact','20'),bg="lightgreen")
labelq.place(x=210,y=80,width=100,height=90)

labelj = Label(win,text="00",font=('Impact','20'),bg="lightgreen")
labelj.place(x=310,y=80,width=100,height=90)

######################################################################

stopwatch = Button(win,text="Stopwatch")
stopwatch.place(x=295,y=268,width=63,height=30)

button = Button(win,text="Sittings",cursor="dotbox",relief=RAISED,font=('Times',10),command=sets)
button.place(x=360,y=268,width=50,height=30)

#######################################################################

def start():
    x = chalo.get()
    displaying.config(text=x)

displaying = Label(win,text="'Have A Nice Day'",font=('Informal Roman',30),bg="lightgreen",fg="black")
displaying.place(x=5,y=200)
display()

# jaldi = Button(win,text="Write")
# jaldi.place(x=320,y=269)

chalo = Entry(win,bd=3,width=46)
chalo.place(x=1,y=268,height=30)

line = Label(win,width=100,bg="grey")
line.place(y=150,height=3)

mainloop()

