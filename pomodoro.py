from tkinter import *
import time
from tkinter import messagebox
x = Tk() 
m=StringVar() 
n=StringVar()
c=StringVar()
m.set('00')
n.set('00')
c.set('00')
def timex():
    tim = time.strftime('%H %M %S %p')
    lbl0.config(text=tim)
    lbl0.after(1000,timex)

x.title('Pomodoro')
x.geometry('500x400')
lbl = Label(text='pomodoro',font=('Courier',12,'bold'),bg='red')
lbl.pack(fill=X)
lbl0 =Label(text='',font=('Courier',12,'bold'))
lbl0.pack()
pic = PhotoImage(file='C:\\Users\\HELAL\\Desktop\\tom.png')
img = Label(image=pic)
img.pack()
ent = Entry(width=10,textvariable=m)
ent.place(x=150,y=200)
ent1 = Entry(width=10,textvariable=n)
ent1.place(x=217,y=200)
ent2 = Entry(width=10,textvariable=c)
ent2.place(x=285,y=200)
x.config(bg='white')
def submit():
 try:
        temp = int(m.get())*3600 + int(n.get())*60 + int(c.get())
 except:
     print('please input right value: ')
 while temp >- 1:
        mins,secs = divmod(temp,60)
        hours = 0
        if mins > 60:
            hours,mins =divmod(mins,60) 
        m.set('{0:2d}'.format(hours))
        n.set('{0:2d}'.format(mins))
        c.set('{0:2d}'.format(secs))
        x.update()
        time.sleep(1)
        if (temp == 0):
            messagebox.showinfo("Time Countdown", "Time's up ")
        
        # after every one sec the value of temp will be decremented
        # by one
        temp-=1    

but= Button(text='set',bg='#6A1B9A',fg='white',width=10,height=1,command=submit)
but.pack()
lblh = Label(text='progammer:Hamoda Elemary',bg='#F57F17')
lblh.pack(fill=X,side=BOTTOM)
def study():
    m.set('00')
    n.set('15')
    c.set('00')
def breake():
    m.set('00')
    n.set('5')
    c.set('00')
def bigbr():
    m.set('00')
    n.set('25')
    c.set("00")
but1 = Button(text='study',width=10,bg='#303F9F',command=study)
but1.place(x=10,y=308)
but2 = Button(text='break',width=10,bg='#D500F9',command=breake)
but2.place(x=400,y=308)
but3 = Button(text='big break',width=10,bg='#7E57C2',command=bigbr)
but3.place(x=210,y=340)

timex()
x.mainloop()