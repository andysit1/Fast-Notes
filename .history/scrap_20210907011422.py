from bs4.builder import SAXTreeBuilder
import requests
from bs4 import BeautifulSoup

import nltk
from nltk import tokenize



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

def filter_text(words):
    important = ['%', '!']
    return True if  in vowels else False

for y,i in enumerate(a):
    text = i.split()
    filter_text = ' '.join((filter(lambda val: val in important_words, text)))

print(filter_text)



#left and right scroll        
#if == "." stop iteraiting and save index into period index
#save the sentence into var
#reset all var == 0 so it will not affect next sentence.

# for index, s in enumerate(output):
#     for words in important_words:   
#         if words.lower() in s.lower():
#             percent += 1
#             location.append(index)



# for i in location: 
#     for output[i] in range(0, len(output)):
#         if output == '.':
#             left.append([i])
#         for output[i] in reversed(0, len(output)):
#             if output == '.':
#                 right.append([i]) 
#                 sentence = output[left: right] 


