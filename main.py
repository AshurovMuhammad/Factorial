#<<<<<factorial>>>>>>
from tkinter import *
oyna = Tk()
oyna.title("Factorialni hisoblovchi dasturcha :)")
oyna.geometry("400x400")


natija = Label(text="Natija", bg='white')
natija.place(x=110, y=250, width=200, height=50)


raqam1 = Entry()
raqam1.place(x=110, y=50, width=200, height=50)


def init():
    raqam = int(raqam1.get())
    fac = 1
    if raqam == 0:
        print(1)
    else:
        while raqam >= 1:
            fac = fac * raqam
            raqam -= 1
        natija.config(text=fac)

tugma = Button(text="Hisoblash", command=init)
tugma.place(x=110, y=150, width=200, height=50)

oyna.mainloop()