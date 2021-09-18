import tkinter as tk
from tkinter import *
from bs4.builder import SAXTreeBuilder
import requests
from bs4 import BeautifulSoup
import nltk
from nltk import tokenize


#test sample: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2797383/

#function that gets the link that the user inputs and outputs notes of website
def get_link():

    #gets link
    link = entry.get()

    output = ''

    #by using beautiful soup and request we can access the website
    res = requests.get(link)
    html_page = res.content

    soup = BeautifulSoup(html_page, 'html.parser')
    text = soup.find_all(text=True)

    #finds only the specific elements on the html page
    whitelist = [
        'p',
        'li',
    ]

    #specfic characters that we look for
    important_words = [
        '%',
    ]

    #gets all the text from the p and li elements and formats into string
    for t in text:
        if t.parent.name in whitelist:
            output += '{} '.format(t)
    
    #uses nltk to make the str into a list of sentences
    a = tokenize.sent_tokenize(output)
    
    #if the sentence had the important_words it saves it into matching
    matching = [s for s in a if any(xs in s for xs in important_words)]
    
    #creates a 
    for i in range(len(matching)):
        exec('Label%s=Label(window,text="%s", anchor="w", width=720, wraplengt=1000)\nLabel%d.pack()' % (i,matching[i],i))




window = tk.Tk()

link = tk.StringVar()
#widgets 

window.title('Fast Notes')
window.geometry('1080x720+60+60')

label = Label(window, text = 'Quick Notes!')
label.pack(side = TOP, pady = 5)

entry = Entry(window, width=500, textvariable=link, bd=5)
entry.pack(side = TOP, pady = 5)

button = Button(window , text = 'Generate Notes', command=get_link)
button.pack(side = TOP, pady = 5)


#Execute
window.mainloop()

