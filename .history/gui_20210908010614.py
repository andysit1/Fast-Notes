import tkinter as tk
from tkinter import *
from bs4.builder import SAXTreeBuilder
import requests
from bs4 import BeautifulSoup
import nltk
from nltk import tokenize


#https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2797383/

def get_link():
    link = entry.get()
    
    output = ''

    res = requests.get(link)
    html_page = res.content

    soup = BeautifulSoup(html_page, 'html.parser')
    text = soup.find_all(text=True)

    whitelist = [
        'p',
        'li',
    ]

    important_words = [
        '%',
    ]

    for t in text:
        if t.parent.name in whitelist:
            output += '{} '.format(t)
    
    a = tokenize.sent_tokenize(output)
    matching = [s for s in a if any(xs in s for xs in important_words)]
    
    for i in range(len(matching)):
        exec('Label%s=Label(window,text="%s")\nLabel%d.pack()' % (i,matching[i],i))

  



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



#Execute
window.mainloop()

