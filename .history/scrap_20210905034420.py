import requests
from bs4 import BeautifulSoup

url = "https://www.cancer.gov/about-cancer/understanding/statistics"
res = requests.get(url)
html_page = res.content

soup = BeautifulSoup(html_page, 'html.parser')

text = soup.find_all(text=True)

output = ''
key = ''
int

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


for s in output:
    for words in important_words:
        if s.find(words) != 0:
            print('There is valuable info!')
            
        else:
            print('This Article contains 0 statics')


