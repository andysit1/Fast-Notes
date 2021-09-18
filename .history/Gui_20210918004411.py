

window = tk.Tk()

link = tk.StringVar()

window.title('Fast Notes')
window.geometry('1080x720+60+60')

label = Label(window, text = 'Quick Notes!')
label.pack(side = TOP, pady = 5)

entry = Entry(window, width=500, textvariable=link, bd=5)
entry.pack(side = TOP, pady = 5)

button = Button(window , text = 'Generate Notes', command=get_link)
button.pack(side = TOP, pady = 5)

window.mainloop()
