import tkinter

import win32api
import win32gui
import win32con
import random
import string
import pyperclip


def Password_Generator():
    password = ''
    for n in range(lenPassword.get()):
        password = password + random.choice(
            string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
    strPassword.set(password)

def CopyPassword():
    if strPassword.get() != '':
        pyperclip.copy(strPassword.get())
        tkinter.Label(win, text='Password copied', font='Lato 12 bold', width=15, foreground="#00D200",
                      background="#000000")
        lblmsg2 = tkinter.Label(win, text='Password copied', font='Lato 12 bold')
        lblmsg2.place(x=105, y=120)

    else:
        lblmsg2 = tkinter.Label(win, text='Nothing to copy', font='Lato 12 bold', width=15, foreground="#00D200",
                                background="#000000")
        lblmsg2.place(x=105, y=120)

win = tkinter.Tk()
win.title("Random Password Generator")
win.configure(bg='#000000')
win.iconbitmap('icon.ico')

win.geometry("350x220")
win.eval('tk::PlaceWindow . center')
win.grid_rowconfigure(0, weight=1)
win.grid_columnconfigure(0, weight=1)
lblPassword = tkinter.Label(win, text='Set Password Length', font='Lato 12', foreground="#00D200", background="#000000")
lblPassword.pack()
lenPassword = tkinter.IntVar()
length = tkinter.Spinbox(win, from_=5, to=200, textvariable=lenPassword, font='Lato 12', width=15,
                         background="#FCFCFC")
length.pack(pady=10)
lblmsg1 = tkinter.Label(win, text='Generated Password', font='Lato 12', foreground="#00D200", background="#000000")
lblmsg1.pack()

strPassword = tkinter.StringVar()
textData = tkinter.Entry(win, textvariable=strPassword, width=25, font='Lato 12', foreground="#00D200",
                         background="#000000")
textData.pack()

btnPassword = tkinter.Button(win, text="Generate Password", foreground="#00D200", background="#000000",
                             activeforeground='#00D200', activebackground='#161619', command=Password_Generator)
btnPassword.pack(padx=50, pady=5, side=tkinter.LEFT)

btnCopy = tkinter.Button(win, text='Copy', foreground="#00D200", background="#000000", activeforeground='#00D200',
                         activebackground='#161619', command=CopyPassword)
btnCopy.pack(side=tkinter.LEFT)
win.mainloop()
hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(hide, win32con.SW_HIDE)
