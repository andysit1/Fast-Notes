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


print(output)
print(percent)

def sentence_finder(index, text):
