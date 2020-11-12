import requests
from bs4 import BeautifulSoup

# Webページを取得して解析する
load_url = 'https://www.ymori.com/books/python2nen/test2.html'
html = requests.get(load_url)
soup = BeautifulSoup(html.content, 'html.parser')

# 全てのliタグを検索して、その文字列を表示する
for element in soup.find_all('li'):
    print(element.text)

    



