from tkinter import *

t = Tk()

t.geometry("400x400+0+0")
t.title("3ak povedz ty nehehe")
l = Label(t, text="dyg more", )
l.pack()
l = Label(t, text="Povedz ty lol")
l.place(x=0, y=0)

b = Button(t, text="Nice cudlik")
b.pack()
b.bind("<Button-1>")


t.mainloop()