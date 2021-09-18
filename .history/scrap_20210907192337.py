from bs4.builder import SAXTreeBuilder
import requests
from bs4 import BeautifulSoup
import nltk
from nltk import tokenize
from tkinter import *


url = "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2797383/"
res = requests.get(url)
html_page = res.content

soup = BeautifulSoup(html_page, 'html.parser')

text = soup.find_all(text=True)

output = ''
key = {}
location = []
percent = 0
spot = []
sentence = []
left = []
right = []
bad = []

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

link = tk.StringVar(window)

for i in matching:
    print(i + '\n')


def get_link(entry):
    print(entry.get())



window = Tk()

#widgets 

window.title('Fast Notes')
window.geometry('600x600+60+60')
button = Button(window , text = 'Generate Notes')
button.pack(side = TOP, pady = 5)

entry = Entry(window, width=500, textvariable='LINK', bd=5)
entry.pack(side = TOP, pady = 5)



#Execute
window.mainloop()

