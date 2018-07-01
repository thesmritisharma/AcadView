'''
#Question 1
import tkinter as tk

m = tk.Tk()
m.title('Hello')
label = tk.Label(m, text='Hello World: ')
button = tk.Button(m, text='EXIT', width=25, command=quit)
label.grid(row=1, column=0)
button.grid(row=1, column=1)
m.mainloop()

#Question 2
import tkinter as tk

def display():
    print('Example...')

m = tk.Tk()
m.title('Hello')
label = tk.Label(m, text='Hello World: ')
button = tk.Button(m, text='ACTION', width=25, command=display)
label.grid(row=1, column=0)
button.grid(row=1, column=1)
m.mainloop()


#Question 3
from tkinter import *

def labelchange():
    label.config(text='CHANGE...')

root=Tk()
frame=Frame(root)
frame.pack()
label=Label(root, text='Hello World: ')
label.pack()
exitButton=Button(frame,text='EXIT',highlightbackground='red',fg='red', command=exit)
exitButton.pack(side=LEFT)
changeButton=Button(frame,text='CHANGE',highlightbackground='green',fg='green', command=labelchange)
changeButton.pack(side=RIGHT)
root.mainloop()
'''

#Question 4
from tkinter import *

def call():
    print(e1.get())
    print(e2.get())

master =Tk()
Label(master,text='First name').grid(row=0)
Label(master,text='Second name').grid(row=1)
Button(master, text='ENTRY', command=call).grid(column=1)
e1 = Entry(master)
e2 = Entry(master)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
mainloop()