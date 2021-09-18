from bs4.builder import SAXTreeBuilder
import requests
from bs4 import BeautifulSoup

url = "https://www.cancer.gov/about-cancer/understanding/statistics"
res = requests.get(url)
html_page = res.content

soup = BeautifulSoup(html_page, 'html.parser')

text = soup.find_all(text=True)

output = ''
key = {}
location = []
percent = 0
spot = []

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



for index, s in enumerate(output):
    for words in important_words:   
        if words.lower() in s.lower():
            percent += 1
            location.append(index)

def sentence_finder(index, t):
    left_scroll = 0
    right_scroll = 0
    p = ''

    for i in index:
        while  p != '.':
            i
               
    #left and right scroll

    #if == "." stop iteraiting and save index into period index

    #save the sentence into var

    #reset all var == 0 so it will not affect next sentence.

print(location)

sentence_finder(location)


print(percent)

