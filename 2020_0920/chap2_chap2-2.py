import requests
from bs4 import BeautifulSoup

# Webページを取得して解析する
load_url = 'https://www.ymori.com/books/python2nen/test1.html'
html = requests.get(load_url)
soup = BeautifulSoup(html.content, 'html.parser')

# title, h2, liタグを検索して表示する
print(soup.find('title'))
print(soup.find('h2'))
print(soup.find('li'))




