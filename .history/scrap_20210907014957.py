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

for i in matching:
    print(i + '\n')


window = Tk()

#widgets 

window.title('Fast Notes')
window.geometry('300x300+10+20')
button = Button(window , text = 'Generate Notes')





