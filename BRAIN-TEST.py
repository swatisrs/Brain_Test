from tkinter import *
from PIL import ImageTk, Image
import time
root = Tk()
root.geometry('800x700')

root.title('HELLO WORLD')
img = ImageTk.PhotoImage(Image.open('assets/mascot.jpeg'))
c = Canvas(root, width=800, height=700,bg='#474545')
c.create_image(400, 300, image=img)
c.place(x=0, y=0)

l1 = Label(c)
l2 = Label(c)
l3 = Label(c)
l4 = Label(c)
i=0
Q1='How many letters are left if E and T leave the alphabet?'
Q2='If 2 hens lay 2 eggs in 2 days,\n'' then how many eggs would 20 hens lay in 20 days?'
Q3='I am a bird, I am a fruit and I am a person. What am I?'

r=[Q1,Q2,Q3]

def clear():
    e1.delete(0,'end')
def ans():
    global i
    if r[i]==Q1:
        if e1.get()=='6': //participating in hacktoberfest
            y()
        else:
            n()
    if r[i]==Q2:
        if e1.get() == '200':
            y()
        else:
            n()
    if r[i]==Q3:
        if e1.get() == 'kiwi':
            y()
        else:
            n()

def opt():
    global e1,A1,A2
    e1 = Entry(root)
    e1.pack(padx=80, pady=70)
    A1 = Button(root, text='ok', font=('New Times Roman', 15), bg='green', relief=SUNKEN, command=ans)
    A1.place(x=250, y=100)
    A2 = Button(root, text='clear', font=('New Times Roman', 15), bg='green', relief=SUNKEN, command=clear)
    A2.place(x=500, y=100)
def s2():
    global m,Q,i
    if i==3:
        dis=Label(root,text="WELL PLAYED",height=20, width=50, font=('New Times Roman', 50), bg='#e2bb03')
        dis.pack()
    root.after(500, None)
    root.update()
    c1.pack_forget()
    try:
         Q=Label(root,text=r[i], font=('New Times Roman', 20))
         Q.pack()
    except:
      print("")
    if r[i]==Q1:
        opt()
    if r[i]==Q2:
        opt()
    if r[i]==Q3:
        opt()
    

def y():
    global j,i
    j = Label(root, text='RIGHT ANSWER', height=20, width=50, font=('New Times Roman', 50), bg='#e2bb03')
    j.pack()
    root.after(1000,None)
    root.update()
    j.pack_forget()
    Q.pack_forget()
    A1.place_forget()
    A2.place_forget()
    e1.pack_forget()
    i=i+1
    s2()
def n():
    j = Label(root, text='WRONG ANSWER,TRY AGAIN!', height=20, width=50, font=('New Times Roman', 30), bg='#e2bb03')
    j.pack()
    root.update()
    root.after(1000,None)
    root.update()
    j.pack_forget()

def s1():
    global c1,h3
    root.after(500, None)
    root.update()
    c.place_forget()
    c1 = Canvas(root, width=800, height=700,bg='#FAA5A5')
    c1.pack()
    h2 = Label(c1, text='ARE YOU READY ', height=8, width=50, font=('New Times Roman', 50), bg='#FAA5A5')
    h2.pack()
    h3 = Button(c1, text='YES', height=5, width=15, font=('New Times Roman', 50), bg='Blue',relief=SUNKEN, command=s2)
    h3.pack(pady=10)



def logscreen():
    root.after(500, None)
    root.update()
    l1.configure(text='SMART BRAIN PRESENTS', height=0, width=25, font=('New Times Roman', 20), bg='#FAA5A5')
    l1.place(x=240, y=40)
    root.after(1000, None)
    root.update()
    l2.configure(text='TEST', font=('New Times Roman', 20), bg='#e2bb03')
    l2.place(x=140, y=310)
    root.after(1000, None)
    root.update()
    l3.configure(text='YOUR', font=('New Times Roman', 20), bg='#474545', fg='white')
    l3.place(x=440, y=200)
    root.after(1000, None)
    root.update()
    l4.configure(text='BRAIN', font=('New Times Roman', 20), bg='#e2bb03')
    l4.place(x=700, y=300)
    root.after(1000, None)
    root.update()
    s1()


logscreen()

root.mainloop()
