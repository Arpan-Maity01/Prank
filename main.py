from tkinter import *
from tkinter import messagebox
import random

def no():
    messagebox.showinfo(' ','Hehe dummy')
    quit()

def motionMouse(event):
    btnYes.place(x=random.randint(0, 500), y=random.randint(0, 500))
root = Tk()

root.title('survey')
root.resizable (width=False, height=False)
root['bg'] = 'white'

label = Label(root, text='are you dumb ?', font="Arial 20 bold", bg='white').pack()

btnYes = Button(root, text='No', font="Arial 28 bold")

btnYes.place(x=176, y=100)
btnYes.bind('<Enter>', motionMouse)
btnNo=Button(root, text="Yes", font="Arial, 20 bold", command=no).place(x=550, y=100)
root.geometry('800x800')
root.mainloop()

