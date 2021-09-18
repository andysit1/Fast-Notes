import requests
from bs4 import BeautifulSoup

url = "https://www.cancer.gov/about-cancer/understanding/statistics"
res = requests.get(url)
html_page = res.content

soup = BeautifulSoup(html_page, 'html.parser')

text = soup.find_all(text=True)

output = ''
blacklist = [
    '[document]',
    'noscript',
    'header',
    'html',
    'meta',
    'head',
    'input',
    ''


]
