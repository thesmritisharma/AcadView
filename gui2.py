from tkinter import *

master = Frame ()
master.pack ()

dict = {"Sim": 15757, "Rad": 453336, "Pi": 34353543, "Nim": 34234374, "Shaf": 837438, "Sid": 44344443,
     "Shre": 23234, "Simran": 15757, "Radhika": 453336, "Piyush": 34353543, "Nimish": 34234374, "Shaffi": 837438, "Siddhant": 44344443,
     "Shreya": 23234}

label1 = Label (master, text="Dictionary")
label1.pack (side="top")
label2 = Label (master, text="This is an example")
label2.pack (side="bottom")

def handleList(event):
    label = list.get (ACTIVE)
    print(label)
    phone = dict.get (label)
    global label1, label2
    label1.config (text=label,)
    label2.config (text=phone)


list = Listbox (master)
sbar = Scrollbar (master)
sbar.config (command=list.yview)
list.config (yscrollcommand=sbar.set)
sbar.pack (side=RIGHT, fill=Y)
list.pack (side=LEFT, expand=YES, fill=BOTH)

list.bind ('<Double-1>', handleList)

for key, value in dict.items ():
    list.insert ('end', key)

master.mainloop ()