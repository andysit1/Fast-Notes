import tkinter as tk
from tkinter import *



def get_link():
    print(entry.get())



window = tk.Tk()

link = tk.StringVar()
#widgets 

window.title('Fast Notes')
window.geometry('600x600+60+60')

label = Label(window, text = 'Quick Notes!')
label.pack(side = TOP, pady = 5)

entry = Entry(window, width=500, textvariable=link, bd=5)
entry.pack(side = TOP, pady = 5)

button = Button(window , text = 'Generate Notes', command=get_link)
button.pack(side = TOP, pady = 5)

data_label = Label(window, textvariable=data )
label.pack(side = TOP, pady = 5)



#Execute
window.mainloop()

