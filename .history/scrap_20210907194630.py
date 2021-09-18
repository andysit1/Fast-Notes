from bs4.builder import SAXTreeBuilder
import requests
from bs4 import BeautifulSoup
import nltk
from nltk import tokenize
import tkinter as tk
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



def scrapper(link):
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
    